# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(599, 334)
        Frame.setMinimumSize(QtCore.QSize(599, 334))
        Frame.setMaximumSize(QtCore.QSize(599, 334))
        Frame.setStyleSheet("border:none")
        Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame = QtWidgets.QFrame(parent=Frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 599, 334))
        self.frame.setMinimumSize(QtCore.QSize(599, 334))
        self.frame.setMaximumSize(QtCore.QSize(599, 334))
        self.frame.setStyleSheet("QFrame{ \n"
"    background-color:rgb(108, 67, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Event_Button = QtWidgets.QPushButton(parent=self.frame)
        self.Event_Button.setGeometry(QtCore.QRect(90, 110, 131, 101))
        self.Event_Button.setMinimumSize(QtCore.QSize(131, 101))
        self.Event_Button.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setFamily("ascii")
        font.setPointSize(12)
        self.Event_Button.setFont(font)
        self.Event_Button.setStyleSheet("QPushButton {\n"
"    background-color:rgb(129, 80, 0);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(162, 100, 0);\n"
"}")
        self.Event_Button.setObjectName("Event_Button")
        self.Dristpunk_Button = QtWidgets.QPushButton(parent=self.frame)
        self.Dristpunk_Button.setGeometry(QtCore.QRect(390, 110, 131, 101))
        self.Dristpunk_Button.setMinimumSize(QtCore.QSize(131, 101))
        self.Dristpunk_Button.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setFamily("ascii")
        font.setPointSize(12)
        self.Dristpunk_Button.setFont(font)
        self.Dristpunk_Button.setStyleSheet("QPushButton {\n"
"    background-color:rgb(129, 80, 0);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(162, 100, 0);\n"
"}")
        self.Dristpunk_Button.setObjectName("Dristpunk_Button")
        self.nicknameEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.nicknameEdit.setGeometry(QtCore.QRect(242, 160, 121, 22))
        self.nicknameEdit.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.nicknameEdit.setObjectName("nicknameEdit")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(240, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("ascii")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Folder_Button = QtWidgets.QPushButton(parent=self.frame)
        self.Folder_Button.setGeometry(QtCore.QRect(544, 283, 41, 41))
        self.Folder_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Folder_Button.setIcon(icon)
        self.Folder_Button.setIconSize(QtCore.QSize(25, 25))
        self.Folder_Button.setObjectName("Folder_Button")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(18, 9, 571, 61))
        font = QtGui.QFont()
        font.setFamily("ascii")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setGeometry(QtCore.QRect(260, 187, 81, 81))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.ApplyNicknameButton = QtWidgets.QPushButton(parent=self.widget)
        self.ApplyNicknameButton.setGeometry(QtCore.QRect(0, 3, 81, 81))
        font = QtGui.QFont()
        font.setFamily("ascii")
        font.setPointSize(12)
        self.ApplyNicknameButton.setFont(font)
        self.ApplyNicknameButton.setObjectName("ApplyNicknameButton")
        self.RamButton = QtWidgets.QPushButton(parent=self.frame)
        self.RamButton.setGeometry(QtCore.QRect(14, 283, 41, 41))
        self.RamButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(129, 80, 0);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(162, 100, 0);\n"
"}\n"
"")
        self.RamButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ram.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.RamButton.setIcon(icon1)
        self.RamButton.setIconSize(QtCore.QSize(35, 35))
        self.RamButton.setObjectName("RamButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "DristLauncher"))
        self.Event_Button.setText(_translate("Frame", "Ивент"))
        self.Dristpunk_Button.setText(_translate("Frame", "DristPunk3"))
        self.label.setText(_translate("Frame", "NickName:"))
        self.label_2.setText(_translate("Frame", "DristLauncher"))
        self.ApplyNicknameButton.setText(_translate("Frame", "Ok"))