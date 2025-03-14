# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPrincipalAC.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_formPrincipalAC(object):
    def setupUi(self, formPrincipalAC):
        if not formPrincipalAC.objectName():
            formPrincipalAC.setObjectName(u"formPrincipalAC")
        formPrincipalAC.setWindowModality(Qt.WindowModality.ApplicationModal)
        formPrincipalAC.resize(1024, 550)
        formPrincipalAC.setStyleSheet(u"background-color: rgb(245, 245, 252);")
        formPrincipalAC.setModal(True)
        self.cmbContrato = QComboBox(formPrincipalAC)
        self.cmbContrato.addItem("")
        self.cmbContrato.setObjectName(u"cmbContrato")
        self.cmbContrato.setGeometry(QRect(10, 120, 131, 31))
        self.cmbContrato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_2 = QLabel(formPrincipalAC)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 61, 21))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(formPrincipalAC)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(850, 90, 121, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.label_4 = QLabel(formPrincipalAC)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 90, 121, 16))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.btnBuscar = QPushButton(formPrincipalAC)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(20, 500, 150, 41))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnBuscar.setFont(font1)
        self.btnBuscar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon = QIcon()
        icon.addFile(u"../iconos/Aha-Soft-Large-Seo-Search.512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QSize(30, 30))
        self.btnRegCob = QPushButton(formPrincipalAC)
        self.btnRegCob.setObjectName(u"btnRegCob")
        self.btnRegCob.setGeometry(QRect(240, 500, 150, 41))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.btnRegCob.setFont(font2)
        self.btnRegCob.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/Webiconset-Application-Invoice.128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegCob.setIcon(icon1)
        self.btnRegCob.setIconSize(QSize(30, 30))
        self.btnRegFact = QPushButton(formPrincipalAC)
        self.btnRegFact.setObjectName(u"btnRegFact")
        self.btnRegFact.setGeometry(QRect(450, 500, 150, 41))
        self.btnRegFact.setFont(font2)
        self.btnRegFact.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../iconos/icons8-factura-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegFact.setIcon(icon2)
        self.btnRegFact.setIconSize(QSize(30, 30))
        self.btnEdoCta = QPushButton(formPrincipalAC)
        self.btnEdoCta.setObjectName(u"btnEdoCta")
        self.btnEdoCta.setGeometry(QRect(660, 500, 150, 41))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.btnEdoCta.setFont(font3)
        self.btnEdoCta.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../iconos/descargar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdoCta.setIcon(icon3)
        self.btnEdoCta.setIconSize(QSize(30, 30))
        self.btnSalir = QPushButton(formPrincipalAC)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(860, 500, 150, 41))
        self.btnSalir.setFont(font1)
        self.btnSalir.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon4 = QIcon()
        icon4.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon4)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.label_5 = QLabel(formPrincipalAC)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 100, 81, 16))
        self.label_5.setFont(font)
        self.cmbAreaC = QComboBox(formPrincipalAC)
        self.cmbAreaC.addItem("")
        self.cmbAreaC.setObjectName(u"cmbAreaC")
        self.cmbAreaC.setGeometry(QRect(160, 120, 121, 30))
        self.cmbAreaC.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame = QFrame(formPrincipalAC)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 160, 1011, 331))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tblCarteraAC = QTableWidget(self.frame)
        if (self.tblCarteraAC.columnCount() < 10):
            self.tblCarteraAC.setColumnCount(10)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setWeight(QFont.ExtraBold)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignHCenter|Qt.AlignBottom);
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font5 = QFont()
        font5.setWeight(QFont.Medium)
        font5.setKerning(False)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setForeground(brush);
        self.tblCarteraAC.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tblCarteraAC.setObjectName(u"tblCarteraAC")
        self.tblCarteraAC.setGeometry(QRect(5, 0, 1001, 320))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblCarteraAC.sizePolicy().hasHeightForWidth())
        self.tblCarteraAC.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Arial Rounded MT"])
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setItalic(False)
        self.tblCarteraAC.setFont(font6)
        self.tblCarteraAC.setStyleSheet(u"background-color: rgb(255, 242, 222);\n"
"\n"
"font: 700 9pt \"Arial Rounded MT\";\n"
"border-radius:5px;")
        self.tblCarteraAC.setFrameShadow(QFrame.Shadow.Plain)
        self.tblCarteraAC.setLineWidth(2)
        self.tblCarteraAC.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.tblCarteraAC.setAlternatingRowColors(True)
        self.tblCarteraAC.setShowGrid(False)
        self.tblCarteraAC.setWordWrap(False)
        self.tblCarteraAC.setCornerButtonEnabled(True)
        self.tblCarteraAC.horizontalHeader().setMinimumSectionSize(20)
        self.tblCarteraAC.horizontalHeader().setDefaultSectionSize(100)
        self.frame_4 = QFrame(formPrincipalAC)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 1031, 81))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 40, 1041, 41))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.txtSaldo = QLineEdit(formPrincipalAC)
        self.txtSaldo.setObjectName(u"txtSaldo")
        self.txtSaldo.setGeometry(QRect(840, 120, 160, 30))
        font7 = QFont()
        font7.setFamilies([u"Comic Sans MS"])
        font7.setPointSize(12)
        self.txtSaldo.setFont(font7)
        self.txtSaldo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtSaldo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txtSaldo.setReadOnly(True)
        self.txtCliente = QLineEdit(formPrincipalAC)
        self.txtCliente.setObjectName(u"txtCliente")
        self.txtCliente.setGeometry(QRect(310, 109, 501, 41))
        font8 = QFont()
        font8.setFamilies([u"Comic Sans MS"])
        font8.setPointSize(16)
        self.txtCliente.setFont(font8)
        self.txtCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCliente.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCliente.setReadOnly(True)

        self.retranslateUi(formPrincipalAC)

        QMetaObject.connectSlotsByName(formPrincipalAC)
    # setupUi

    def retranslateUi(self, formPrincipalAC):
        formPrincipalAC.setWindowTitle("")
        self.cmbContrato.setItemText(0, QCoreApplication.translate("formPrincipalAC", u"--elige una opcion", None))

        self.label_2.setText(QCoreApplication.translate("formPrincipalAC", u"Contrato", None))
        self.label_3.setText(QCoreApplication.translate("formPrincipalAC", u"Saldo", None))
        self.label_4.setText(QCoreApplication.translate("formPrincipalAC", u"Cliente ", None))
        self.btnBuscar.setText(QCoreApplication.translate("formPrincipalAC", u"Buscar", None))
        self.btnRegCob.setText(QCoreApplication.translate("formPrincipalAC", u"Reg.Cobranza", None))
        self.btnRegFact.setText(QCoreApplication.translate("formPrincipalAC", u"Reg.Facturas", None))
        self.btnEdoCta.setText(QCoreApplication.translate("formPrincipalAC", u"Informacion", None))
        self.btnSalir.setText(QCoreApplication.translate("formPrincipalAC", u"Salir", None))
        self.label_5.setText(QCoreApplication.translate("formPrincipalAC", u"Area Comun", None))
        self.cmbAreaC.setItemText(0, QCoreApplication.translate("formPrincipalAC", u"--elije una opcion", None))

        ___qtablewidgetitem = self.tblCarteraAC.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("formPrincipalAC", u"Contrato", None));
        ___qtablewidgetitem1 = self.tblCarteraAC.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("formPrincipalAC", u"Tipo Cuota", None));
        ___qtablewidgetitem2 = self.tblCarteraAC.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("formPrincipalAC", u"Num Factura", None));
        ___qtablewidgetitem3 = self.tblCarteraAC.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("formPrincipalAC", u"Importe Adeudo", None));
        ___qtablewidgetitem4 = self.tblCarteraAC.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("formPrincipalAC", u"Importe Pago", None));
        ___qtablewidgetitem5 = self.tblCarteraAC.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("formPrincipalAC", u"Saldo", None));
        ___qtablewidgetitem6 = self.tblCarteraAC.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("formPrincipalAC", u"Fecha Pago/Cobro", None));
        ___qtablewidgetitem7 = self.tblCarteraAC.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("formPrincipalAC", u"Forma pago", None));
        ___qtablewidgetitem8 = self.tblCarteraAC.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("formPrincipalAC", u"Cta Bancaria", None));
        ___qtablewidgetitem9 = self.tblCarteraAC.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("formPrincipalAC", u"Status", None));
        self.label_10.setText(QCoreApplication.translate("formPrincipalAC", u" GESTOR CARTERA AREAS COMUNES", None))
    # retranslateUi

