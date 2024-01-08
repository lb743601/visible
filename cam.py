from ximea import xiapi
class visible_cam:
    # 初始化，img为类内帧数据
    def __init__(self):
        self.cam = xiapi.Camera()
        print('Opening first camera...')
        self.cam.open_device()
        self.img = xiapi.Image()
        self.data = self.img.get_image_data_numpy()
    #设置曝光时间
    def set_ex(self, ex):
        self.cam.set_exposure(ex)

    #设置分辨率：
    # ("··") 648*486
    # ("XI_DWN_2x2") 1296*972
    # ("XI_DWN_1x1") 2592*1944
    def set_ds(self, ds):
        self.cam.set_downsampling(ds)

    #设置图像格式 RAW16 RAW8 MONO8 MONO16
    def set_format(self,format):
        self.cam.set_imgdataformat(format)

    #开始捕获，使用线程，外部通过类的img进行调用
    def start(self):
        self.cam.start_acquisition()
        # while True:
        #     self.cam.get_image(self.img)
        #     self.data = self.img.get_image_data_numpy()


    #停止捕获
    def stop(self):
        self.cam.stop_acquisition()

    #关闭设备,程序结束前调用
    def close(self):
        self.cam.close_device()
