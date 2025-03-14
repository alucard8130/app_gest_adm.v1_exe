# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formContratos.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_formClientes(object):
    def setupUi(self, formClientes):
        if not formClientes.objectName():
            formClientes.setObjectName(u"formClientes")
        formClientes.setWindowModality(Qt.WindowModality.ApplicationModal)
        formClientes.resize(572, 455)
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
        self.frame_2.setGeometry(QRect(0, 70, 681, 331))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.txtNumContrato = QLineEdit(self.frame_2)
        self.txtNumContrato.setObjectName(u"txtNumContrato")
        self.txtNumContrato.setGeometry(QRect(10, 30, 121, 30))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(11)
        self.txtNumContrato.setFont(font1)
        self.txtNumContrato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtNumContrato.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtNumContrato.setReadOnly(True)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 91, 16))
        self.cmbCliente = QComboBox(self.frame_2)
        self.cmbCliente.addItem("")
        self.cmbCliente.setObjectName(u"cmbCliente")
        self.cmbCliente.setEnabled(True)
        self.cmbCliente.setGeometry(QRect(10, 90, 261, 30))
        self.cmbCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 111, 21))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 70, 111, 21))
        self.cmbTipoContrato = QComboBox(self.frame_2)
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.addItem("")
        self.cmbTipoContrato.setObjectName(u"cmbTipoContrato")
        self.cmbTipoContrato.setEnabled(True)
        self.cmbTipoContrato.setGeometry(QRect(340, 90, 191, 30))
        self.cmbTipoContrato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dateInicial = QDateEdit(self.frame_2)
        self.dateInicial.setObjectName(u"dateInicial")
        self.dateInicial.setGeometry(QRect(340, 180, 110, 30))
        self.dateInicial.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dateInicial.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.dateInicial.setCalendarPopup(True)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 160, 71, 21))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(340, 240, 71, 21))
        self.dateFinal = QDateEdit(self.frame_2)
        self.dateFinal.setObjectName(u"dateFinal")
        self.dateFinal.setGeometry(QRect(340, 260, 110, 30))
        self.dateFinal.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.dateFinal.setCalendarPopup(True)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(420, 0, 141, 61))
        self.groupBox.setStyleSheet(u"")
        self.checkBActivo = QCheckBox(self.groupBox)
        self.checkBActivo.setObjectName(u"checkBActivo")
        self.checkBActivo.setGeometry(QRect(10, 30, 61, 16))
        self.checkBActivo.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 140, 231, 171))
        self.cmbAreaComun = QComboBox(self.groupBox_2)
        self.cmbAreaComun.addItem("")
        self.cmbAreaComun.setObjectName(u"cmbAreaComun")
        self.cmbAreaComun.setEnabled(True)
        self.cmbAreaComun.setGeometry(QRect(10, 40, 201, 30))
        self.cmbAreaComun.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 111, 21))
        self.txtDG = QLineEdit(self.groupBox_2)
        self.txtDG.setObjectName(u"txtDG")
        self.txtDG.setGeometry(QRect(120, 110, 91, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.txtDG.setFont(font2)
        self.txtDG.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtDG.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.txtDG.setReadOnly(True)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(140, 90, 61, 16))
        self.txtCuota = QLineEdit(self.groupBox_2)
        self.txtCuota.setObjectName(u"txtCuota")
        self.txtCuota.setGeometry(QRect(10, 110, 101, 30))
        self.txtCuota.setFont(font2)
        self.txtCuota.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCuota.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.txtCuota.setReadOnly(True)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 90, 41, 16))
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 400, 654, 51))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btnGuardar = QPushButton(self.frame_3)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(10, 12, 140, 35))
        self.btnGuardar.setMaximumSize(QSize(150, 100))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.btnGuardar.setFont(font3)
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
        self.btnSalir = QPushButton(self.frame_3)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(400, 10, 140, 35))
        self.btnSalir.setMaximumSize(QSize(150, 100))
        self.btnSalir.setFont(font3)
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QSize(20, 20))
        self.btnSalir.setFlat(True)

        self.retranslateUi(formClientes)

        QMetaObject.connectSlotsByName(formClientes)
    # setupUi

    def retranslateUi(self, formClientes):
        formClientes.setWindowTitle("")
        self.label_6.setText(QCoreApplication.translate("formClientes", u" REGISTRO CONTRATOS", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Num Contrato", None))
        self.cmbCliente.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))

        self.label_3.setText(QCoreApplication.translate("formClientes", u"Cliente", None))
        self.label_5.setText(QCoreApplication.translate("formClientes", u"Tipo Contrato", None))
        self.cmbTipoContrato.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))
        self.cmbTipoContrato.setItemText(1, QCoreApplication.translate("formClientes", u"Arrendamiento", None))
        self.cmbTipoContrato.setItemText(2, QCoreApplication.translate("formClientes", u"Comodato", None))
        self.cmbTipoContrato.setItemText(3, QCoreApplication.translate("formClientes", u"Uso o Goce", None))

        self.label_4.setText(QCoreApplication.translate("formClientes", u"Fecha Inicio", None))
        self.label_8.setText(QCoreApplication.translate("formClientes", u"Fecha Fin", None))
        self.groupBox.setTitle(QCoreApplication.translate("formClientes", u"Status", None))
        self.checkBActivo.setText(QCoreApplication.translate("formClientes", u"Activo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("formClientes", u"Area", None))
        self.cmbAreaComun.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))

        self.label_12.setText(QCoreApplication.translate("formClientes", u"Numero", None))
        self.label_13.setText(QCoreApplication.translate("formClientes", u"Deposito", None))
        self.label_7.setText(QCoreApplication.translate("formClientes", u"Cuota", None))
        self.btnGuardar.setText(QCoreApplication.translate("formClientes", u"Guardar", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
    # retranslateUi

