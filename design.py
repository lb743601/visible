# Form implementation generated from reading ui file 'visible.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 663)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video = QtWidgets.QLabel(parent=self.centralwidget)
        self.video.setEnabled(True)
        self.video.setGeometry(QtCore.QRect(0, 50, 852, 639))
        self.video.setText("")
        self.video.setPixmap(QtGui.QPixmap("C:/Users/awu/Desktop/大雁塔/IMG_0813.JPG"))
        self.video.setScaledContents(True)
        self.video.setObjectName("video")
        self.connect_cam = QtWidgets.QPushButton(parent=self.centralwidget)
        self.connect_cam.setGeometry(QtCore.QRect(490, 0, 100, 50))
        self.connect_cam.setObjectName("connect_cam")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 0, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.resolution_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.resolution_cb.setGeometry(QtCore.QRect(60, 10, 80, 30))
        self.resolution_cb.setEditable(False)
        self.resolution_cb.setObjectName("resolution_cb")
        self.resolution_cb.addItem("")
        self.resolution_cb.addItem("")
        self.resolution_cb.addItem("")
        self.resolution_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.resolution_label.setGeometry(QtCore.QRect(0, 10, 50, 30))
        self.resolution_label.setObjectName("resolution_label")
        self.format_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.format_label.setGeometry(QtCore.QRect(160, 10, 70, 30))
        self.format_label.setObjectName("format_label")
        self.format_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.format_cb.setGeometry(QtCore.QRect(230, 10, 80, 30))
        self.format_cb.setEditable(False)
        self.format_cb.setObjectName("format_cb")
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.ex_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ex_label.setGeometry(QtCore.QRect(320, 10, 60, 30))
        self.ex_label.setObjectName("ex_label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 10, 80, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(600, 0, 100, 50))
        self.stop.setObjectName("stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resolution_cb.setCurrentIndex(0)
        self.format_cb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connect_cam.setText(_translate("MainWindow", "启动视频流"))
        self.pushButton.setText(_translate("MainWindow", "拍照"))
        self.resolution_cb.setCurrentText(_translate("MainWindow", "XI_DWN_4x4"))
        self.resolution_cb.setItemText(0, _translate("MainWindow", "XI_DWN_1x1"))
        self.resolution_cb.setItemText(1, _translate("MainWindow", "XI_DWN_2x2"))
        self.resolution_cb.setItemText(2, _translate("MainWindow", "XI_DWN_4x4"))
        self.resolution_label.setText(_translate("MainWindow", "分辨率"))
        self.format_label.setText(_translate("MainWindow", "图像格式"))
        self.format_cb.setCurrentText(_translate("MainWindow", "XI_RAW8"))
        self.format_cb.setItemText(0, _translate("MainWindow", "XI_RAW8"))
        self.format_cb.setItemText(1, _translate("MainWindow", "XI_RAW16"))
        self.format_cb.setItemText(2, _translate("MainWindow", "XI_MONO8"))
        self.format_cb.setItemText(3, _translate("MainWindow", "XI_MONO16"))
        self.ex_label.setText(_translate("MainWindow", "曝光时间"))
        self.lineEdit.setText(_translate("MainWindow", "50000"))
        self.stop.setText(_translate("MainWindow", "停止"))