# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Strapongo\Projects\Hw PyQt\Lab2\flag.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 271, 209))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.firstGroup = QtWidgets.QButtonGroup(MainWindow)
        self.firstGroup.setObjectName("firstGroup")
        self.firstGroup.addButton(self.radioButton_4)
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.firstGroup.addButton(self.radioButton_5)
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.firstGroup.addButton(self.radioButton_6)
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.secondGroup = QtWidgets.QButtonGroup(MainWindow)
        self.secondGroup.setObjectName("secondGroup")
        self.secondGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.secondGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.secondGroup.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.thirdGroup = QtWidgets.QButtonGroup(MainWindow)
        self.thirdGroup.setObjectName("thirdGroup")
        self.thirdGroup.addButton(self.radioButton_7)
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.thirdGroup.addButton(self.radioButton_8)
        self.verticalLayout_3.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.thirdGroup.addButton(self.radioButton_9)
        self.verticalLayout_3.addWidget(self.radioButton_9)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_4.setText(_translate("MainWindow", "Белый"))
        self.radioButton_5.setText(_translate("MainWindow", "Синий"))
        self.radioButton_6.setText(_translate("MainWindow", "Красный"))
        self.radioButton.setText(_translate("MainWindow", "Белый"))
        self.radioButton_2.setText(_translate("MainWindow", "Синий"))
        self.radioButton_3.setText(_translate("MainWindow", "Красный"))
        self.radioButton_7.setText(_translate("MainWindow", "Белый"))
        self.radioButton_8.setText(_translate("MainWindow", "Синий"))
        self.radioButton_9.setText(_translate("MainWindow", "Красный"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать"))