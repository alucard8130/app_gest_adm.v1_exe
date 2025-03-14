# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPrincipalCM.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_formPrincipalCM(object):
    def setupUi(self, formPrincipalCM):
        if not formPrincipalCM.objectName():
            formPrincipalCM.setObjectName(u"formPrincipalCM")
        formPrincipalCM.setWindowModality(Qt.WindowModality.ApplicationModal)
        formPrincipalCM.resize(1022, 557)
        formPrincipalCM.setStyleSheet(u"background-color: rgb(245, 245, 252);")
        formPrincipalCM.setModal(True)
        self.cmblocal = QComboBox(formPrincipalCM)
        self.cmblocal.addItem("")
        self.cmblocal.setObjectName(u"cmblocal")
        self.cmblocal.setGeometry(QRect(10, 120, 201, 31))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        self.cmblocal.setFont(font)
        self.cmblocal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.label_2 = QLabel(formPrincipalCM)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 151, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(formPrincipalCM)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(860, 100, 121, 21))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(formPrincipalCM)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 90, 121, 16))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnBuscar = QPushButton(formPrincipalCM)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(20, 500, 150, 41))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.btnBuscar.setFont(font2)
        self.btnBuscar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon = QIcon()
        icon.addFile(u"../iconos/Aha-Soft-Large-Seo-Search.512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QSize(30, 30))
        self.btnRegCob = QPushButton(formPrincipalCM)
        self.btnRegCob.setObjectName(u"btnRegCob")
        self.btnRegCob.setGeometry(QRect(230, 500, 150, 41))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.btnRegCob.setFont(font3)
        self.btnRegCob.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/Webiconset-Application-Invoice.128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegCob.setIcon(icon1)
        self.btnRegCob.setIconSize(QSize(30, 30))
        self.btnRegFact = QPushButton(formPrincipalCM)
        self.btnRegFact.setObjectName(u"btnRegFact")
        self.btnRegFact.setGeometry(QRect(430, 500, 150, 41))
        self.btnRegFact.setFont(font3)
        self.btnRegFact.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../iconos/icons8-factura-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRegFact.setIcon(icon2)
        self.btnRegFact.setIconSize(QSize(30, 30))
        self.btnEdoCta = QPushButton(formPrincipalCM)
        self.btnEdoCta.setObjectName(u"btnEdoCta")
        self.btnEdoCta.setGeometry(QRect(640, 500, 150, 41))
        self.btnEdoCta.setFont(font3)
        self.btnEdoCta.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../iconos/imprimir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdoCta.setIcon(icon3)
        self.btnEdoCta.setIconSize(QSize(30, 30))
        self.btnSalir = QPushButton(formPrincipalCM)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(850, 500, 150, 41))
        self.btnSalir.setFont(font2)
        self.btnSalir.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.btnSalir.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        icon4 = QIcon()
        icon4.addFile(u"../iconos/salir.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSalir.setIcon(icon4)
        self.btnSalir.setIconSize(QSize(30, 30))
        self.tblCarteraCM = QTableWidget(formPrincipalCM)
        if (self.tblCarteraCM.columnCount() < 10):
            self.tblCarteraCM.setColumnCount(10)
        brush = QBrush(QColor(8, 8, 8, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tblCarteraCM.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setForeground(brush1);
        self.tblCarteraCM.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tblCarteraCM.setObjectName(u"tblCarteraCM")
        self.tblCarteraCM.setGeometry(QRect(10, 170, 1001, 316))
        self.tblCarteraCM.setMaximumSize(QSize(16777215, 16777214))
        self.tblCarteraCM.setStyleSheet(u"background-color: rgb(255, 242, 222);\n"
"\n"
"font: 700 9pt \"Arial Rounded MT\";\n"
"border-radius:5px;")
        self.tblCarteraCM.setShowGrid(False)
        self.tblCarteraCM.setGridStyle(Qt.PenStyle.DashLine)
        self.frame_5 = QFrame(formPrincipalCM)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 1031, 81))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(8, 14, 91);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 40, 1041, 41))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.txtSaldo = QLineEdit(formPrincipalCM)
        self.txtSaldo.setObjectName(u"txtSaldo")
        self.txtSaldo.setGeometry(QRect(840, 120, 160, 30))
        font4 = QFont()
        font4.setFamilies([u"Comic Sans MS"])
        font4.setPointSize(12)
        self.txtSaldo.setFont(font4)
        self.txtSaldo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtSaldo.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.txtSaldo.setReadOnly(True)
        self.cmbCliente = QComboBox(formPrincipalCM)
        self.cmbCliente.addItem("")
        self.cmbCliente.setObjectName(u"cmbCliente")
        self.cmbCliente.setEnabled(False)
        self.cmbCliente.setGeometry(QRect(279, 110, 501, 40))
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.cmbCliente.setFont(font5)
        self.cmbCliente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cmbCliente.setAutoFillBackground(False)
        self.cmbCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")

        self.retranslateUi(formPrincipalCM)

        QMetaObject.connectSlotsByName(formPrincipalCM)
    # setupUi

    def retranslateUi(self, formPrincipalCM):
        formPrincipalCM.setWindowTitle("")
        self.cmblocal.setItemText(0, QCoreApplication.translate("formPrincipalCM", u"---seleccione una opcion---", None))

        self.label_2.setText(QCoreApplication.translate("formPrincipalCM", u"Local Comercial", None))
        self.label_3.setText(QCoreApplication.translate("formPrincipalCM", u"Saldo Adeudo", None))
        self.label_4.setText(QCoreApplication.translate("formPrincipalCM", u"Cliente ", None))
        self.btnBuscar.setText(QCoreApplication.translate("formPrincipalCM", u"Buscar", None))
        self.btnRegCob.setText(QCoreApplication.translate("formPrincipalCM", u"Reg.Cobranza", None))
        self.btnRegFact.setText(QCoreApplication.translate("formPrincipalCM", u"Reg.Facturas", None))
        self.btnEdoCta.setText(QCoreApplication.translate("formPrincipalCM", u"Imp.Edo Cta", None))
        self.btnSalir.setText(QCoreApplication.translate("formPrincipalCM", u"Salir", None))
        ___qtablewidgetitem = self.tblCarteraCM.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("formPrincipalCM", u"Tipo Cuota", None));
        ___qtablewidgetitem1 = self.tblCarteraCM.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("formPrincipalCM", u"Num Factura", None));
        ___qtablewidgetitem2 = self.tblCarteraCM.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("formPrincipalCM", u"Importe Adeudo", None));
        ___qtablewidgetitem3 = self.tblCarteraCM.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("formPrincipalCM", u"Importe Pago", None));
        ___qtablewidgetitem4 = self.tblCarteraCM.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("formPrincipalCM", u"Importe Saldo", None));
        ___qtablewidgetitem5 = self.tblCarteraCM.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("formPrincipalCM", u"Fecha Cobro/Pago", None));
        ___qtablewidgetitem6 = self.tblCarteraCM.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("formPrincipalCM", u"Forma Pago", None));
        ___qtablewidgetitem7 = self.tblCarteraCM.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("formPrincipalCM", u"Num Cheque", None));
        ___qtablewidgetitem8 = self.tblCarteraCM.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("formPrincipalCM", u"Cta Bancaria", None));
        ___qtablewidgetitem9 = self.tblCarteraCM.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("formPrincipalCM", u"Status", None));
        self.label_11.setText(QCoreApplication.translate("formPrincipalCM", u" GESTOR CARTERA LOCALES COMERCIALES", None))
        self.cmbCliente.setItemText(0, QCoreApplication.translate("formPrincipalCM", u"------seleccione una opcion------", None))

    # retranslateUi

