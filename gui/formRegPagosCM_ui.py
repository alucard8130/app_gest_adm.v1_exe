# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formRegPagosCM.ui'
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
        Dialog.resize(672, 498)
        Dialog.setStyleSheet(u"background-color: rgb(245, 245, 252);")
        Dialog.setModal(True)
        self.btnRegistrar = QPushButton(Dialog)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(50, 450, 150, 40))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(False)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRegistrar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        icon = QIcon()
        icon.addFile(u"../iconos/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegistrar.setIcon(icon)
        self.btnRegistrar.setIconSize(QSize(40, 40))
        self.btnSalir = QPushButton(Dialog)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(490, 450, 150, 40))
        self.btnSalir.setFont(font)
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon1)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 681, 71))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 40, 832, 31))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 70, 681, 361))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txtCheque = QLineEdit(self.frame)
        self.txtCheque.setObjectName(u"txtCheque")
        self.txtCheque.setGeometry(QRect(30, 310, 71, 30))
        self.txtCheque.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCheque.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtLocal = QLineEdit(self.frame)
        self.txtLocal.setObjectName(u"txtLocal")
        self.txtLocal.setGeometry(QRect(10, 60, 121, 30))
        self.txtLocal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtLocal.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtLocal.setReadOnly(True)
        self.cmbTipoCuota = QComboBox(self.frame)
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.addItem("")
        self.cmbTipoCuota.setObjectName(u"cmbTipoCuota")
        self.cmbTipoCuota.setGeometry(QRect(210, 60, 181, 30))
        self.cmbTipoCuota.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 101, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 290, 81, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 160, 81, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 160, 91, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 40, 81, 16))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(210, 40, 91, 16))
        self.txtComentarios = QTextEdit(self.frame)
        self.txtComentarios.setObjectName(u"txtComentarios")
        self.txtComentarios.setGeometry(QRect(390, 280, 261, 61))
        self.txtComentarios.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(460, 160, 111, 16))
        self.cmbFactura = QComboBox(self.frame)
        self.cmbFactura.addItem("")
        self.cmbFactura.setObjectName(u"cmbFactura")
        self.cmbFactura.setGeometry(QRect(440, 60, 171, 30))
        self.cmbFactura.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtImporte = QLineEdit(self.frame)
        self.txtImporte.setObjectName(u"txtImporte")
        self.txtImporte.setGeometry(QRect(10, 180, 131, 30))
        self.txtImporte.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtImporte.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.boxDate = QDateEdit(self.frame)
        self.boxDate.setObjectName(u"boxDate")
        self.boxDate.setGeometry(QRect(210, 310, 101, 30))
        self.boxDate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.boxDate.setCalendarPopup(True)
        self.cmbFormaPago = QComboBox(self.frame)
        self.cmbFormaPago.addItem("")
        self.cmbFormaPago.addItem("")
        self.cmbFormaPago.addItem("")
        self.cmbFormaPago.addItem("")
        self.cmbFormaPago.addItem("")
        self.cmbFormaPago.setObjectName(u"cmbFormaPago")
        self.cmbFormaPago.setGeometry(QRect(190, 180, 211, 30))
        self.cmbFormaPago.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 260, 71, 16))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 290, 81, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 0, 151, 16))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(7)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(85, 0, 0);")
        self.cmbCtaBancaria = QComboBox(self.frame)
        self.cmbCtaBancaria.addItem("")
        self.cmbCtaBancaria.setObjectName(u"cmbCtaBancaria")
        self.cmbCtaBancaria.setGeometry(QRect(450, 180, 171, 30))
        self.cmbCtaBancaria.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.btnSalir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"  COBRANZA CUOTAS LOCALES COMERCIALES", None))
        self.cmbTipoCuota.setItemText(0, QCoreApplication.translate("Dialog", u"--seleccione una opcion", None))
        self.cmbTipoCuota.setItemText(1, QCoreApplication.translate("Dialog", u"pago mensual", None))
        self.cmbTipoCuota.setItemText(2, QCoreApplication.translate("Dialog", u"pago atrasado", None))
        self.cmbTipoCuota.setItemText(3, QCoreApplication.translate("Dialog", u"pago anticipado", None))
        self.cmbTipoCuota.setItemText(4, QCoreApplication.translate("Dialog", u"pago no identificado", None))
        self.cmbTipoCuota.setItemText(5, QCoreApplication.translate("Dialog", u"pago parcial o a cuenta", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Local Comercial", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Fecha Pago *", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Importe Pago *", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Forma de Pago *", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Num. Factura *", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Tipo Pago*", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Cta Bancaria Pago *", None))
        self.cmbFactura.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))

        self.cmbFormaPago.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))
        self.cmbFormaPago.setItemText(1, QCoreApplication.translate("Dialog", u"Transferencia SPEI", None))
        self.cmbFormaPago.setItemText(2, QCoreApplication.translate("Dialog", u"Cheque", None))
        self.cmbFormaPago.setItemText(3, QCoreApplication.translate("Dialog", u"Deposito Bancario", None))
        self.cmbFormaPago.setItemText(4, QCoreApplication.translate("Dialog", u"Transferencia Interna", None))

        self.label_10.setText(QCoreApplication.translate("Dialog", u"Comentarios", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Num. Cheque", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"* campos obligatorios", None))
        self.cmbCtaBancaria.setItemText(0, QCoreApplication.translate("Dialog", u"--selecciona una opcion--", None))

    # retranslateUi

