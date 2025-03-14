# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBcontratos.ui'
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
        formClientes.resize(572, 454)
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
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 20, 91, 16))
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(380, 10, 191, 51))
        self.groupBox.setStyleSheet(u"")
        self.checkBActivo = QCheckBox(self.groupBox)
        self.checkBActivo.setObjectName(u"checkBActivo")
        self.checkBActivo.setGeometry(QRect(10, 20, 61, 16))
        self.checkBActivo.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.checkBvencido = QCheckBox(self.groupBox)
        self.checkBvencido.setObjectName(u"checkBvencido")
        self.checkBvencido.setGeometry(QRect(110, 20, 71, 16))
        self.checkBvencido.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.cmbContrato = QComboBox(self.frame_2)
        self.cmbContrato.addItem("")
        self.cmbContrato.setObjectName(u"cmbContrato")
        self.cmbContrato.setEnabled(True)
        self.cmbContrato.setGeometry(QRect(10, 40, 201, 30))
        self.cmbContrato.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtArea = QLineEdit(self.frame_2)
        self.txtArea.setObjectName(u"txtArea")
        self.txtArea.setGeometry(QRect(330, 120, 191, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.txtArea.setFont(font1)
        self.txtArea.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtArea.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtArea.setReadOnly(False)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 71, 21))
        self.txtCuota = QLineEdit(self.frame_2)
        self.txtCuota.setObjectName(u"txtCuota")
        self.txtCuota.setGeometry(QRect(330, 190, 191, 30))
        self.txtCuota.setFont(font1)
        self.txtCuota.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCuota.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCuota.setReadOnly(False)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 240, 71, 21))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 71, 21))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(330, 240, 61, 16))
        self.txtCliente = QLineEdit(self.frame_2)
        self.txtCliente.setObjectName(u"txtCliente")
        self.txtCliente.setGeometry(QRect(10, 120, 271, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.txtCliente.setFont(font2)
        self.txtCliente.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtCliente.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtCliente.setReadOnly(False)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 170, 41, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 100, 111, 21))
        self.txtDG = QLineEdit(self.frame_2)
        self.txtDG.setObjectName(u"txtDG")
        self.txtDG.setGeometry(QRect(330, 260, 191, 30))
        self.txtDG.setFont(font1)
        self.txtDG.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.txtDG.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtDG.setReadOnly(False)
        self.txtfecha_ini = QLineEdit(self.frame_2)
        self.txtfecha_ini.setObjectName(u"txtfecha_ini")
        self.txtfecha_ini.setGeometry(QRect(10, 190, 211, 30))
        self.txtfecha_ini.setFont(font1)
        self.txtfecha_ini.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtfecha_ini.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtfecha_ini.setReadOnly(False)
        self.txtfecha_fin = QLineEdit(self.frame_2)
        self.txtfecha_fin.setObjectName(u"txtfecha_fin")
        self.txtfecha_fin.setGeometry(QRect(10, 260, 211, 30))
        self.txtfecha_fin.setFont(font1)
        self.txtfecha_fin.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.txtfecha_fin.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.txtfecha_fin.setReadOnly(False)
        self.frame_3 = QFrame(formClientes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 400, 654, 51))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.btnSalir = QPushButton(self.frame_3)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(400, 10, 140, 35))
        self.btnSalir.setMaximumSize(QSize(150, 100))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.btnSalir.setFont(font3)
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
        self.btnEditar = QPushButton(self.frame_3)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setGeometry(QRect(20, 10, 140, 35))
        self.btnEditar.setMaximumSize(QSize(150, 100))
        self.btnEditar.setFont(font3)
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnEditar.setStyleSheet(u"background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../iconos/Custom-Icon-Design-Pretty-Office-9-Edit-file.256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditar.setIcon(icon1)
        self.btnEditar.setIconSize(QSize(30, 30))
        self.btnEditar.setFlat(True)

        self.retranslateUi(formClientes)

        QMetaObject.connectSlotsByName(formClientes)
    # setupUi

    def retranslateUi(self, formClientes):
        formClientes.setWindowTitle("")
        self.label_6.setText(QCoreApplication.translate("formClientes", u" BUSCAR CONTRATOS", None))
        self.label_10.setText(QCoreApplication.translate("formClientes", u"Num Contrato", None))
        self.groupBox.setTitle(QCoreApplication.translate("formClientes", u"Status", None))
        self.checkBActivo.setText(QCoreApplication.translate("formClientes", u"Activo", None))
        self.checkBvencido.setText(QCoreApplication.translate("formClientes", u"Vencido", None))
        self.cmbContrato.setItemText(0, QCoreApplication.translate("formClientes", u"--seleccione una opcion--", None))

        self.cmbContrato.setPlaceholderText(QCoreApplication.translate("formClientes", u"selecciona una opcion", None))
        self.label_4.setText(QCoreApplication.translate("formClientes", u"Fecha Inicio", None))
        self.label_8.setText(QCoreApplication.translate("formClientes", u"Fecha Fin", None))
        self.label_3.setText(QCoreApplication.translate("formClientes", u"Cliente", None))
        self.label_13.setText(QCoreApplication.translate("formClientes", u"Deposito", None))
        self.label_7.setText(QCoreApplication.translate("formClientes", u"Cuota", None))
        self.label_9.setText(QCoreApplication.translate("formClientes", u"Area", None))
        self.btnSalir.setText(QCoreApplication.translate("formClientes", u"Salir", None))
        self.btnEditar.setText(QCoreApplication.translate("formClientes", u"Editar", None))
    # retranslateUi

