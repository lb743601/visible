from ctypes import *
import platform
from time import sleep
from usb_device import *
from usb2pwm import *
class device:
    def __init__(self):
        self.DevIndex=0
        self.DevHandles=(c_int*20)()
        self.ret=None
        self.USB2XXXInfo = DEVICE_INFO()
        self.USB2XXXFunctionString = (c_char * 256)()
        self.PWMConfig = PWM_CONFIG()
        self.PWMConfig.ChannelMask = 0xFF  # 初始化所有通道
    def scan_device(self):
        self.ret=USB_ScanDevice(byref(self.DevHandles))
        return self.ret
    def connect_device(self):
        self.ret=USB_OpenDevice(self.DevHandles[self.DevIndex])
        return self.ret
    def print_information(self):
        self.ret=DEV_GetDeviceInfo(self.DevHandles[self.DevIndex],byref(self.USB2XXXInfo),byref(self.USB2XXXFunctionString))
        if (bool(self.ret)):
            print("USB2XXX device infomation:")
            print("--Firmware Name: %s" % bytes(self.USB2XXXInfo.FirmwareName).decode('ascii'))
            print("--Firmware Version: v%d.%d.%d" % (
            (self.USB2XXXInfo.FirmwareVersion >> 24) & 0xFF, (self.USB2XXXInfo.FirmwareVersion >> 16) & 0xFF,
            self.USB2XXXInfo.FirmwareVersion & 0xFFFF))
            print("--Hardware Version: v%d.%d.%d" % (
            (self.USB2XXXInfo.HardwareVersion >> 24) & 0xFF, (self.USB2XXXInfo.HardwareVersion >> 16) & 0xFF,
            self.USB2XXXInfo.HardwareVersion & 0xFFFF))
            print("--Build Date: %s" % bytes(self.USB2XXXInfo.BuildDate).decode('ascii'))
            print("--Serial Number: ", end='')
            for i in range(0, len(self.USB2XXXInfo.SerialNumber)):
                print("%08X" % self.USB2XXXInfo.SerialNumber[i], end='')
            print("")
            print("--Function String: %s" % bytes(self.USB2XXXFunctionString.value).decode('ascii'))
        else:
            print("Get device infomation faild!")
    def set_pwm(self,Polarity,Precision,Prescaler,Pulse,Phase):
        for i in range(0, 8):
            self.PWMConfig.Polarity[i] =Polarity  # 将所有PWM通道都设置为正极性
            self.PWMConfig.Precision[i] =Precision # 将所有通道的占空比调节精度都设置为1%
            self.PWMConfig.Prescaler[i] =Prescaler  # 将所有通道的预分频器都设置为10，则PWM输出频率为200MHz/(PWMConfig.Precision*PWMConfig.Prescaler)
            self.PWMConfig.Pulse[i] = self.PWMConfig.Precision[i] * Pulse // 100  # 将所有通道的占空比都设置为30%
            self.PWMConfig.Phase[i] = Phase
        # 初始化PWM
        self.ret = PWM_Init(self.DevHandles[self.DevIndex], byref(self.PWMConfig));
        if self.ret != PWM_SUCCESS:
            print("Initialize pwm faild!")
        else:
            print("Initialize pwm sunccess!")
    def start_pwm(self,RunTimeOfUs):
        self.ret=PWM_Start(self.DevHandles[self.DevIndex],self.PWMConfig.ChannelMask,RunTimeOfUs)
        if (self.ret != PWM_SUCCESS):
            print("Start pwm faild!")
            exit()
        else:
            print("Start pwm sunccess!")
    def stop_pwm(self):
        self.ret = PWM_Stop(self.DevHandles[self.DevIndex],self.PWMConfig.ChannelMask)
        if(self.ret != PWM_SUCCESS):
            print("Stop pwm faild!");
            exit()
        else:
            print("Stop pwm sunccess!")