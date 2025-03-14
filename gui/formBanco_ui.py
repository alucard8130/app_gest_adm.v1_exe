# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBanco.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_formClientes(object):
    def setupUi(self, formClientes):
        if not formClientes.objectName():
            formClientes.setObjectName(u"formClientes")
        formClientes.setWindowModality(Qt.WindowModality.ApplicationModal)
        formClientes.resize(672, 333)
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
        self.frame_2.setGeometry(QRect(0, 70, 681, 211))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.txtNombreBanco = QLineEdit(self.frame_2)
        self.txtNombreBanco.setObjectName(u"txtNombreBanco")
        self.txtNombreBanco.setGeometry(QRect(20, 60, 291, 30))
        self.txtNombreBanco.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtNombreBanco.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 120, 81, 21))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 120, 111, 16))
        self.txtNumCta = QLineEdit(self.frame_2)
        self.txtNumCta.setObjectName(u"txtNumCta")
        self.txtNumCta.setGeometry(QRect(380, 60, 181, 30))
        self.txtNumCta.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtNumCta.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 40, 111, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(390, 40, 101, 16))
        self.cmbTipoCta = QComboBox(self.frame_2)
        self.cmbTipoCta.addItem("")
        self.cmbTipoCta.addItem("")
        self.cmbTipoCta.addItem("")
        self.cmbTipoCta.addItem("")
        self.cmbTipoCta.setObjectName(u"cmbTipoCta")
        self.cmbTipoCta.setGeometry(QRect(20, 140, 180, 30))
        self.cmbTipoCta.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmbTipoMoneda = QComboBox(self.frame_2)
        self.cmbTipoMoneda.addItem("")
        self.cmbTipoMoneda.addItem("")
        self.cmbTipoMoneda.addItem("")
        self.cmbTipoMoneda.addItem("")
        self.cmbTipoMoneda.setObjectName(u"cmbTipoMoneda")
        self.cmbTipoMoneda.setGeometry(QRect(380, 140, 171, 30))
        self.cmbTipoMoneda.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 280, 654, 51))
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
        self.label_6.setText(QCoreApplication.translate("formClientes", u"  REGISTRO CUENTAS BANCARIAS", None))
        self.label_5.setText(QCoreApplication.translate("formClientes", u"Tipo Cuenta", None))
        self.label_9.setText(QCoreApplication.translate("formClientes", u"Moneda", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Nombre Banco", None))
        self.label_11.setText(QCoreApplication.translate("formClientes", u"Numero Cuenta", None))
        self.cmbTipoCta.setItemText(0, QCoreApplication.translate("formClientes", u"--selecciona una opcion---", None))
        self.cmbTipoCta.setItemText(1, QCoreApplication.translate("formClientes", u"Principal", None))
        self.cmbTipoCta.setItemText(2, QCoreApplication.translate("formClientes", u"Inversion", None))
        self.cmbTipoCta.setItemText(3, QCoreApplication.translate("formClientes", u"Ahorro", None))

        self.cmbTipoMoneda.setItemText(0, QCoreApplication.translate("formClientes", u"--selecciona una opcion---", None))
        self.cmbTipoMoneda.setItemText(1, QCoreApplication.translate("formClientes", u"Pesos", None))
        self.cmbTipoMoneda.setItemText(2, QCoreApplication.translate("formClientes", u"Dolares", None))
        self.cmbTipoMoneda.setItemText(3, QCoreApplication.translate("formClientes", u"Euros", None))

        self.btnGuardar.setText(QCoreApplication.translate("formClientes", u"Guardar", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
    # retranslateUi

