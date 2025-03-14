# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formLocales.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_formClientes(object):
    def setupUi(self, formClientes):
        if not formClientes.objectName():
            formClientes.setObjectName(u"formClientes")
        formClientes.setWindowModality(Qt.WindowModality.ApplicationModal)
        formClientes.resize(609, 468)
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
        self.frame_2.setGeometry(QRect(0, 70, 681, 341))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.txtLocal = QLineEdit(self.frame_2)
        self.txtLocal.setObjectName(u"txtLocal")
        self.txtLocal.setGeometry(QRect(20, 110, 181, 30))
        self.txtLocal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtLocal.setEchoMode(QLineEdit.EchoMode.Normal)
        self.txtLocal.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 250, 49, 21))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 250, 111, 21))
        self.groupBoxStatus = QGroupBox(self.frame_2)
        self.groupBoxStatus.setObjectName(u"groupBoxStatus")
        self.groupBoxStatus.setGeometry(QRect(30, 10, 111, 61))
        self.groupBoxStatus.setStyleSheet(u"")
        self.checkBoxStatus = QCheckBox(self.groupBoxStatus)
        self.checkBoxStatus.setObjectName(u"checkBoxStatus")
        self.checkBoxStatus.setGeometry(QRect(10, 40, 93, 16))
        self.checkBoxStatus.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 170, 91, 21))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 20, 71, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 90, 111, 16))
        self.txtSuperficie = QLineEdit(self.frame_2)
        self.txtSuperficie.setObjectName(u"txtSuperficie")
        self.txtSuperficie.setGeometry(QRect(20, 190, 101, 30))
        self.txtSuperficie.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtSuperficie.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCuota = QLineEdit(self.frame_2)
        self.txtCuota.setObjectName(u"txtCuota")
        self.txtCuota.setGeometry(QRect(330, 190, 131, 30))
        self.txtCuota.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCuota.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtRFC_p = QLineEdit(self.frame_2)
        self.txtRFC_p.setObjectName(u"txtRFC_p")
        self.txtRFC_p.setGeometry(QRect(330, 110, 131, 30))
        self.txtRFC_p.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtRFC_p.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtPropietario = QLineEdit(self.frame_2)
        self.txtPropietario.setObjectName(u"txtPropietario")
        self.txtPropietario.setGeometry(QRect(330, 40, 251, 30))
        self.txtPropietario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtPropietario.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtGiro = QLineEdit(self.frame_2)
        self.txtGiro.setObjectName(u"txtGiro")
        self.txtGiro.setGeometry(QRect(20, 270, 250, 30))
        self.txtGiro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtGiro.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 90, 111, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 170, 61, 16))
        self.cmbClientes = QComboBox(self.frame_2)
        self.cmbClientes.addItem("")
        self.cmbClientes.setObjectName(u"cmbClientes")
        self.cmbClientes.setGeometry(QRect(330, 270, 251, 30))
        self.cmbClientes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtLocal.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.groupBoxStatus.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.txtSuperficie.raise_()
        self.txtCuota.raise_()
        self.txtRFC_p.raise_()
        self.txtGiro.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.cmbClientes.raise_()
        self.txtPropietario.raise_()
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 410, 654, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btnGuardar = QPushButton(self.frame_3)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(20, 12, 150, 40))
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
"border-radius:10px;\n"
"")
        icon = QIcon()
        icon.addFile(u"../iconos/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QSize(40, 40))
        self.btnGuardar.setFlat(True)
        self.btnSalir = QPushButton(self.frame_3)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(440, 10, 150, 40))
        self.btnSalir.setMaximumSize(QSize(150, 100))
        self.btnSalir.setFont(font1)
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.btnSalir.setFlat(True)

        self.retranslateUi(formClientes)

        QMetaObject.connectSlotsByName(formClientes)
    # setupUi

    def retranslateUi(self, formClientes):
        formClientes.setWindowTitle("")
        self.label_6.setText(QCoreApplication.translate("formClientes", u"  REGISTRO LOCALES COMERCIALES", None))
        self.txtLocal.setText("")
        self.txtLocal.setPlaceholderText(QCoreApplication.translate("formClientes", u"ejemplo: L-01", None))
        self.label_4.setText(QCoreApplication.translate("formClientes", u"Giro", None))
        self.label_3.setText(QCoreApplication.translate("formClientes", u"Cliente Facturacion", None))
        self.groupBoxStatus.setTitle(QCoreApplication.translate("formClientes", u"Status", None))
        self.checkBoxStatus.setText(QCoreApplication.translate("formClientes", u"Disponible", None))
        self.label_5.setText(QCoreApplication.translate("formClientes", u"Cuota Mensual", None))
        self.label_7.setText(QCoreApplication.translate("formClientes", u"Propietario", None))
        self.label_9.setText(QCoreApplication.translate("formClientes", u"RFC Propietario", None))
        self.txtRFC_p.setText(QCoreApplication.translate("formClientes", u"XAXX010101000", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Numero Local", None))
        self.label_11.setText(QCoreApplication.translate("formClientes", u"Superficie", None))
        self.cmbClientes.setItemText(0, QCoreApplication.translate("formClientes", u"---selecciona una opccion---", None))

        self.btnGuardar.setText(QCoreApplication.translate("formClientes", u"Guardar", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
    # retranslateUi

