# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Strapongo\Projects\Hw PyQt\Lab2\diary.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(10, 350, 392, 236))
        self.calendar.setObjectName("calendar")
        self.event = QtWidgets.QLineEdit(self.centralwidget)
        self.event.setGeometry(QtCore.QRect(10, 10, 391, 31))
        self.event.setObjectName("event")
        self.eventList = QtWidgets.QListWidget(self.centralwidget)
        self.eventList.setGeometry(QtCore.QRect(10, 130, 391, 211))
        self.eventList.setObjectName("eventList")
        self.timer = QtWidgets.QTimeEdit(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(10, 50, 391, 31))
        self.timer.setObjectName("timer")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 90, 191, 28))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(210, 90, 191, 28))
        self.removeButton.setObjectName("removeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diary"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.removeButton.setText(_translate("MainWindow", "Удалить"))