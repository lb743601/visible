import time
import numpy as np
from datetime import datetime
import cv2
from ximea import xiapi
from cam import *
from pwm import *
import threading
from time import sleep
from PyQt6.QtGui import QImage, QPixmap
import sys
from PyQt6.QtCore import QTimer,Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow  # 从 design.py 导入 UI 类
from cam import *  # 从 cam.py 导入相机控制类
import threading
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.current_frame = None
        self.setupUi(self)  # 设置UI界面

        self.camera = visible_cam()  # 实例化相机控制类

        # 连接界面控件的信号与槽
        # 例如，如果您有一个按钮来启动相机，您可以这样做：
        self.connect_cam.clicked.connect(self.start_camera)
        self.pushButton.clicked.connect(self.save)
        self.stop.clicked.connect(self.stop_acq)
        # 注意：您需要根据您的实际界面控件名称来替换 startCameraButton
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
          # 设置定时器时间间隔（例如，30ms）
    def stop_acq(self):
        self.connect_cam.setEnabled(True)
        if self.timer.isActive():
            self.timer.stop()
        self.camera.stop()
        self.current_frame=None
    def update_frame(self):
        # 获取最新帧
        self.camera.cam.get_image(self.camera.img)
        self.current_frame=self.camera.img.get_image_data_numpy()
        if self.current_frame is not None:
            self.display_image()
    def adjust_image(self,image):
        if image.dtype == np.uint16:
            # 使用 min-max 归一化映射到 [0, 255]
            min_val = np.min(image)
            max_val = np.max(image)
            scaled_image = ((image - min_val) / (max_val - min_val)) * 255
            return scaled_image.astype(np.uint8)
        elif image.dtype == np.uint8:
            # 对于 uint8 数据，直接返回
            return image
        else:
            raise ValueError("Unsupported image data type")
        return image
    def display_image(self):
        # 假设 frame 是灰度图像
        adjusted_frame = self.adjust_image(self.current_frame)
        h, w = adjusted_frame.shape
        bytes_per_line = w
        q_img = QImage(adjusted_frame.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)

        # 将 QImage 转换为 QPixmap 并缩放到 QLabel 的大小
        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(self.video.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.video.setPixmap(scaled_pixmap)
    def save(self):
        #存储照片
        if self.current_frame is not None:
            # 为保存的文件指定文件名
            now = datetime.now()
            file_name = now.strftime('%Y-%m-%d %H-%M-%S') + '.raw'
            #filename = "saved_frame.raw"  # RAW 格式文件名
            # 以二进制形式保存原始图像数据
            self.current_frame.tofile(file_name)
            print("sucess")
    def start_camera(self):
        # 启动相机的逻辑
        self.connect_cam.setEnabled(False)
        exposure = self.lineEdit.text()
        resolution=self.resolution_cb.currentText()
        format=self.format_cb.currentText()
        self.camera.set_ds(resolution)
        self.camera.set_ex(int(exposure))
        self.camera.set_format(format)

        self.camera.start()
        time.sleep(0.05)

        self.timer.start(30)
        #self.camera.some_start_method()  # 替换为相机类中的启动方法
        # 更新UI或其他操作

    # 您可以根据需要添加更多方法，例如停止相机、设置参数等

if __name__ == "__main__":
    # d=device()
    # d.scan_device()
    # d.connect_device()
    # d.print_information()
    # d.set_pwm(0,2000,100,50,0)
    # d.start_pwm(10000)
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
