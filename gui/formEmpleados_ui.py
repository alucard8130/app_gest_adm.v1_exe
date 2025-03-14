# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formEmpleados.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_formClientes(object):
    def setupUi(self, formClientes):
        if not formClientes.objectName():
            formClientes.setObjectName(u"formClientes")
        formClientes.setWindowModality(Qt.WindowModality.ApplicationModal)
        formClientes.resize(672, 501)
        formClientes.setStyleSheet(u"background-color: rgb(245, 245, 252);")
        self.frame = QFrame(formClientes)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 681, 71))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 40, 832, 31))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame_2 = QFrame(formClientes)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 70, 681, 383))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.txtNombreCliente = QLineEdit(self.frame_2)
        self.txtNombreCliente.setObjectName(u"txtNombreCliente")
        self.txtNombreCliente.setGeometry(QRect(20, 110, 250, 30))
        self.txtNombreCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtNombreCliente.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 310, 49, 21))
        self.txtDireccion = QTextEdit(self.frame_2)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setGeometry(QRect(370, 310, 281, 51))
        self.txtDireccion.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbTipoContribuyente = QComboBox(self.frame_2)
        self.cmbTipoContribuyente.addItem("")
        self.cmbTipoContribuyente.addItem("")
        self.cmbTipoContribuyente.addItem("")
        self.cmbTipoContribuyente.setObjectName(u"cmbTipoContribuyente")
        self.cmbTipoContribuyente.setEnabled(True)
        self.cmbTipoContribuyente.setGeometry(QRect(20, 250, 201, 30))
        self.cmbTipoContribuyente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 230, 111, 21))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 290, 49, 16))
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 111, 61))
        self.groupBox.setStyleSheet(u"")
        self.checkBoxStatus = QCheckBox(self.groupBox)
        self.checkBoxStatus.setObjectName(u"checkBoxStatus")
        self.checkBoxStatus.setGeometry(QRect(10, 40, 93, 16))
        self.checkBoxStatus.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 20, 49, 21))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 160, 31, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(370, 90, 111, 16))
        self.txtRFC = QLineEdit(self.frame_2)
        self.txtRFC.setObjectName(u"txtRFC")
        self.txtRFC.setGeometry(QRect(20, 180, 181, 30))
        self.txtRFC.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtRFC.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtEmail = QLineEdit(self.frame_2)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(370, 40, 201, 30))
        self.txtEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtEmail.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCel = QLineEdit(self.frame_2)
        self.txtCel.setObjectName(u"txtCel")
        self.txtCel.setGeometry(QRect(370, 110, 151, 30))
        self.txtCel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtGiro = QLineEdit(self.frame_2)
        self.txtGiro.setObjectName(u"txtGiro")
        self.txtGiro.setGeometry(QRect(370, 180, 231, 30))
        self.txtGiro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtGiro.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCURP = QLineEdit(self.frame_2)
        self.txtCURP.setObjectName(u"txtCURP")
        self.txtCURP.setGeometry(QRect(20, 330, 250, 30))
        self.txtCURP.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCURP.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 90, 111, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 160, 31, 16))
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(370, 230, 111, 21))
        self.cmbTipoCliente = QComboBox(self.frame_2)
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.addItem("")
        self.cmbTipoCliente.setObjectName(u"cmbTipoCliente")
        self.cmbTipoCliente.setEnabled(True)
        self.cmbTipoCliente.setGeometry(QRect(370, 250, 201, 30))
        self.cmbTipoCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 454, 654, 51))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btnGuardar = QPushButton(self.frame_3)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(25, 12, 150, 30))
        self.btnGuardar.setMaximumSize(QSize(150, 100))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.btnGuardar.setFont(font1)
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnGuardar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon = QIcon()
        icon.addFile(u"../iconos/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QSize(30, 30))
        self.btnGuardar.setFlat(True)
        self.btnEditar = QPushButton(self.frame_3)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setGeometry(QRect(255, 10, 150, 30))
        self.btnEditar.setMaximumSize(QSize(150, 100))
        self.btnEditar.setFont(font1)
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEditar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/Custom-Icon-Design-Pretty-Office-9-Edit-file.256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditar.setIcon(icon1)
        self.btnEditar.setIconSize(QSize(20, 20))
        self.btnEditar.setFlat(True)
        self.btnSalir = QPushButton(self.frame_3)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(485, 10, 150, 30))
        self.btnSalir.setMaximumSize(QSize(150, 100))
        self.btnSalir.setFont(font1)
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon2)
        self.btnSalir.setIconSize(QSize(20, 20))
        self.btnSalir.setFlat(True)

        self.retranslateUi(formClientes)

        QMetaObject.connectSlotsByName(formClientes)
    # setupUi

    def retranslateUi(self, formClientes):
        formClientes.setWindowTitle("")
        self.label_6.setText(QCoreApplication.translate("formClientes", u" REGISTRO TRABAJADORES ", None))
        self.label_4.setText(QCoreApplication.translate("formClientes", u"CURP", None))
        self.cmbTipoContribuyente.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))
        self.cmbTipoContribuyente.setItemText(1, QCoreApplication.translate("formClientes", u"Persona Fisica", None))
        self.cmbTipoContribuyente.setItemText(2, QCoreApplication.translate("formClientes", u"Persona Moral", None))

        self.label_3.setText(QCoreApplication.translate("formClientes", u"Tipo Contribuyente", None))
        self.label_8.setText(QCoreApplication.translate("formClientes", u"Direccion", None))
        self.groupBox.setTitle(QCoreApplication.translate("formClientes", u"Status", None))
        self.checkBoxStatus.setText(QCoreApplication.translate("formClientes", u"Cliente Activo", None))
        self.label_5.setText(QCoreApplication.translate("formClientes", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("formClientes", u"Giro", None))
        self.label_9.setText(QCoreApplication.translate("formClientes", u"Numero Telefonico", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Razon Social", None))
        self.label_11.setText(QCoreApplication.translate("formClientes", u"RFC", None))
        self.label_12.setText(QCoreApplication.translate("formClientes", u"Tipo Cliente", None))
        self.cmbTipoCliente.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))
        self.cmbTipoCliente.setItemText(1, QCoreApplication.translate("formClientes", u"Areas Comunes", None))
        self.cmbTipoCliente.setItemText(2, QCoreApplication.translate("formClientes", u"Locales Comerciales", None))
        self.cmbTipoCliente.setItemText(3, QCoreApplication.translate("formClientes", u"Espacios Publicitarios", None))
        self.cmbTipoCliente.setItemText(4, QCoreApplication.translate("formClientes", u"Recuperacion Servicios", None))

        self.btnGuardar.setText(QCoreApplication.translate("formClientes", u"Guardar", None))
        self.btnEditar.setText(QCoreApplication.translate("formClientes", u"Editar", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
    # retranslateUi

