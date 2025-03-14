# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formFactMasiva.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_formClientes(object):
    def setupUi(self, formClientes):
        if not formClientes.objectName():
            formClientes.setObjectName(u"formClientes")
        formClientes.setWindowModality(Qt.WindowModality.ApplicationModal)
        formClientes.resize(347, 291)
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
        self.frame_2.setGeometry(QRect(0, 70, 681, 171))
        self.frame_2.setMaximumSize(QSize(16777215, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 10, 91, 16))
        self.cmbTcartera = QComboBox(self.frame_2)
        self.cmbTcartera.addItem("")
        self.cmbTcartera.addItem("")
        self.cmbTcartera.addItem("")
        self.cmbTcartera.setObjectName(u"cmbTcartera")
        self.cmbTcartera.setEnabled(True)
        self.cmbTcartera.setGeometry(QRect(70, 30, 191, 30))
        self.cmbTcartera.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.fechaPeriodo = QDateEdit(self.frame_2)
        self.fechaPeriodo.setObjectName(u"fechaPeriodo")
        self.fechaPeriodo.setGeometry(QRect(70, 110, 151, 30))
        self.fechaPeriodo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.fechaPeriodo.setCalendarPopup(False)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 90, 121, 20))
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 240, 654, 51))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btnSalir = QPushButton(self.frame_3)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(220, 10, 100, 35))
        self.btnSalir.setMaximumSize(QSize(150, 100))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.btnSalir.setFont(font1)
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon = QIcon()
        icon.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon)
        self.btnSalir.setIconSize(QSize(20, 20))
        self.btnSalir.setFlat(True)
        self.btnEjecutar = QPushButton(self.frame_3)
        self.btnEjecutar.setObjectName(u"btnEjecutar")
        self.btnEjecutar.setGeometry(QRect(20, 10, 111, 35))
        self.btnEjecutar.setMaximumSize(QSize(150, 100))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.btnEjecutar.setFont(font2)
        self.btnEjecutar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEjecutar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEjecutar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/icon_menu.gif", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEjecutar.setIcon(icon1)
        self.btnEjecutar.setIconSize(QSize(20, 20))
        self.btnEjecutar.setFlat(True)

        self.retranslateUi(formClientes)

        QMetaObject.connectSlotsByName(formClientes)
    # setupUi

    def retranslateUi(self, formClientes):
        formClientes.setWindowTitle("")
        self.label_6.setText(QCoreApplication.translate("formClientes", u" CARGA MASIVA DE CUOTAS", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Tipo Cartera", None))
        self.cmbTcartera.setItemText(0, QCoreApplication.translate("formClientes", u"---seleccione una opcion...", None))
        self.cmbTcartera.setItemText(1, QCoreApplication.translate("formClientes", u"locales comerciales", None))
        self.cmbTcartera.setItemText(2, QCoreApplication.translate("formClientes", u"areas comunes", None))

        self.cmbTcartera.setPlaceholderText(QCoreApplication.translate("formClientes", u"selecciona una opcion", None))
        self.fechaPeriodo.setDisplayFormat(QCoreApplication.translate("formClientes", u"MM/yyyy", None))
        self.label_11.setText(QCoreApplication.translate("formClientes", u"Periodo (mes/a\u00f1o)", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
        self.btnEjecutar.setText(QCoreApplication.translate("formClientes", u"EJECUTAR", None))
    # retranslateUi

