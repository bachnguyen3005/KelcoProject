# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIver2.0.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter


import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 480)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../Documents/PlatformIO/Projects/kelco_test_001/beta.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.centralwidget.setStyleSheet("selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 87, 83, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 650, 344))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kpaLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.kpaLabel.setFont(font)
        self.kpaLabel.setStyleSheet("background-color: rgb(252, 233, 79);\n"
"")
        self.kpaLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.kpaLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.kpaLabel.setLineWidth(1)
        self.kpaLabel.setScaledContents(False)
        self.kpaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kpaLabel.setObjectName("kpaLabel")
        self.gridLayout_2.addWidget(self.kpaLabel, 2, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 0, 3, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.kpaLCDNumber = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.kpaLCDNumber.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.kpaLCDNumber.setSmallDecimalPoint(False)
        self.kpaLCDNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.kpaLCDNumber.setProperty("value", 0.0)
        self.kpaLCDNumber.setProperty("intValue", 0)
        self.kpaLCDNumber.setObjectName("kpaLCDNumber")
        self.gridLayout_2.addWidget(self.kpaLCDNumber, 3, 1, 1, 3)
        self.calLCDNumber = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.calLCDNumber.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.calLCDNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.calLCDNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.calLCDNumber.setProperty("intValue", 0)
        self.calLCDNumber.setObjectName("calLCDNumber")
        self.gridLayout_2.addWidget(self.calLCDNumber, 2, 1, 1, 3)
        self.calLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.calLabel.setFont(font)
        self.calLabel.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.calLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.calLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.calLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.calLabel.setObjectName("calLabel")
        self.gridLayout_2.addWidget(self.calLabel, 3, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setAutoFillBackground(False)
        self.resetButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.resetButton.setObjectName("resetButton")
        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setAutoFillBackground(False)
        self.stopButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 650, 344))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.viewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.viewButton.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.viewButton.setObjectName("viewButton")
        self.gridLayout_5.addWidget(self.viewButton, 2, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.closeButton.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_5.addWidget(self.closeButton, 2, 1, 1, 1)
        self.webcamFrame = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.webcamFrame.setText("")
        self.webcamFrame.setObjectName("webcamFrame")
        self.gridLayout_5.addWidget(self.webcamFrame, 0, 0, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuMain_layout = QtWidgets.QMenu(self.menubar)
        self.menuMain_layout.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.menuMain_layout.setObjectName("menuMain_layout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMain_layout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.cap = cv2.VideoCapture(0)

        self.viewButton.clicked.connect(self.startWebcam)

        self.closeButton.clicked.connect(self.stop_webcam)

        self.resetButton.clicked.connect(self.resetWindow)

        self.exitButton.clicked.connect(self.confirmExit)

        self.startButton.clicked.connect(self.confirmStart)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automated Calibration System GUI"))
        self.kpaLabel.setText(_translate("MainWindow", "Kpa"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.calLabel.setText(_translate("MainWindow", "Cal"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.stopButton.setText(_translate("MainWindow", "Estop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Control GUI"))
        self.viewButton.setText(_translate("MainWindow", "View"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Webcam"))
        self.menuMain_layout.setTitle(_translate("MainWindow", "Main GUI"))

    def startWebcam(self):
        # Set up timer for updating the frame
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30 ms

    def stop_webcam(self):
        self.timer.stop()
        self.cap.release()

    def exitWindow(self):
        MainWindow.close()


    def resetWindow(self):
        self.new_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.new_window)
        self.new_window.showFullScreen()        

    def confirmExit(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        font = QtGui.QFont()
        font.setPointSize(20)  # Set a larger font size
        msgBox.setFont(font)
        msgBox.setStyleSheet(""" QMessageBox {
                                    min-width: 400px;  /* Set the minimum width */
                                    min-height: 200px;  /* Set the minimum height */
                                }
                                QPushButton {
                                    font-size: 14px;  /* Increase font size of buttons */
                                    padding: 10px;     /* Add padding to make buttons larger */
                                }
                                QLabel {
                                    font-size: 16px;  /* Increase font size of the label text */
                                }""")
        msgBox.setWindowTitle('Confirm Exit')
        msgBox.setText('Are you sure you want to exit?')



        
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)

        response = msgBox.exec_()

        if response == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()

    def confirmStart(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        font = QtGui.QFont()
        font.setPointSize(20)  # Set a larger font size
        msgBox.setFont(font)
        msgBox.setStyleSheet(""" QMessageBox {
                                    min-width: 400px;  /* Set the minimum width */
                                    min-height: 200px;  /* Set the minimum height */
                                }
                                QPushButton {
                                    font-size: 14px;  /* Increase font size of buttons */
                                    padding: 10px;     /* Add padding to make buttons larger */
                                }
                                QLabel {
                                    font-size: 16px;  /* Increase font size of the label text */
                                }""")
        msgBox.setWindowTitle('Confirm Start')
        msgBox.setText('Are you sure you want to start?')



        
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)

        response = msgBox.exec_()

        if response == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
