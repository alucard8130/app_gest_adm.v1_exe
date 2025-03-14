# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formRegFacturasCM.ui'
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
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog.resize(521, 488)
        Dialog.setModal(True)
        self.btnRegistrar = QPushButton(Dialog)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(20, 440, 150, 40))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon = QIcon()
        icon.addFile(u"../iconos/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegistrar.setIcon(icon)
        self.btnRegistrar.setIconSize(QSize(40, 40))
        self.btnSalir = QPushButton(Dialog)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(350, 440, 150, 40))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.btnSalir.setFont(font1)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 681, 71))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 40, 832, 31))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 70, 671, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cmbTipoCuota = QComboBox(self.frame)
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.setObjectName(u"cmbTipoCuota")
        self.cmbTipoCuota.setGeometry(QRect(30, 130, 231, 30))
        self.cmbTipoCuota.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtComentarios = QTextEdit(self.frame)
        self.txtComentarios.setObjectName(u"txtComentarios")
        self.txtComentarios.setGeometry(QRect(30, 290, 231, 61))
        self.txtComentarios.setStyleSheet(u"border-radius:5px;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 81, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 190, 81, 16))
        self.boxDate = QDateEdit(self.frame)
        self.boxDate.setObjectName(u"boxDate")
        self.boxDate.setGeometry(QRect(310, 210, 111, 30))
        self.boxDate.setStyleSheet(u"border-radius:5px;")
        self.boxDate.setCalendarPopup(True)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 270, 71, 16))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(310, 30, 101, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 190, 81, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 110, 111, 16))
        self.txtLocal = QLineEdit(self.frame)
        self.txtLocal.setObjectName(u"txtLocal")
        self.txtLocal.setGeometry(QRect(30, 50, 113, 30))
        self.txtLocal.setStyleSheet(u"border-radius:5px;")
        self.txtLocal.setReadOnly(True)
        self.txtImporte = QLineEdit(self.frame)
        self.txtImporte.setObjectName(u"txtImporte")
        self.txtImporte.setGeometry(QRect(30, 210, 113, 30))
        self.txtImporte.setStyleSheet(u"border-radius:5px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 0, 151, 16))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(7)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(85, 0, 0);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 110, 91, 16))
        self.cmbTipoFact = QComboBox(self.frame)
        self.cmbTipoFact.addItem("")
        self.cmbTipoFact.addItem("")
        self.cmbTipoFact.addItem("")
        self.cmbTipoFact.addItem("")
        self.cmbTipoFact.setObjectName(u"cmbTipoFact")
        self.cmbTipoFact.setGeometry(QRect(310, 130, 161, 30))
        self.cmbTipoFact.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtNumFact = QLineEdit(self.frame)
        self.txtNumFact.setObjectName(u"txtNumFact")
        self.txtNumFact.setGeometry(QRect(310, 50, 131, 30))
        self.txtNumFact.setStyleSheet(u"border-radius:5px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.btnSalir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"  FACTURAS LOCALES COMERCIALES", None))
        self.cmbTipoCuota.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))
        self.cmbTipoCuota.setItemText(1, QCoreApplication.translate("Dialog", u"cuota ordinaria", None))
        self.cmbTipoCuota.setItemText(2, QCoreApplication.translate("Dialog", u"cuota anual", None))
        self.cmbTipoCuota.setItemText(3, QCoreApplication.translate("Dialog", u"cuota extraordinaria", None))
        self.cmbTipoCuota.setItemText(4, QCoreApplication.translate("Dialog", u"cuota anticipada", None))
        self.cmbTipoCuota.setItemText(5, QCoreApplication.translate("Dialog", u"cuota publicidad", None))
        self.cmbTipoCuota.setItemText(6, QCoreApplication.translate("Dialog", u"cuota recuperacion servicios", None))
        self.cmbTipoCuota.setItemText(7, QCoreApplication.translate("Dialog", u"cuota garantia", None))
        self.cmbTipoCuota.setItemText(8, "")

        self.label.setText(QCoreApplication.translate("Dialog", u"Local *", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Importe Fact *", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Comentarios", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Num Factura*", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Periodo Fact *", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tipo Cuota/Ingreso*", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"* campos obligatorios", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Tipo Factura *", None))
        self.cmbTipoFact.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))
        self.cmbTipoFact.setItemText(1, QCoreApplication.translate("Dialog", u"Ingreso", None))
        self.cmbTipoFact.setItemText(2, QCoreApplication.translate("Dialog", u"Nota Credito", None))
        self.cmbTipoFact.setItemText(3, QCoreApplication.translate("Dialog", u"Egreso", None))

    # retranslateUi

