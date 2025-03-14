from datetime import datetime
import csv
import sys
import os 
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QFileDialog, QLineEdit, QApplication
from data import ctasbancos
from data.cartera import CarteraDataAC, CarteraDataCM
from data.clientes import BuscarCliente, ClientesData
from data.contratos import ContratosData
from data.editcontrato import EditContratoData
from data.facturas import FacturasData
from data.periodo import PeriodosCargaData
from data.regareac import RegACData
from data.regcliente import RegClienteData
from data.regcontrato import RegContratoData
from data.proveedores import ProveedoresData
from data.regctabancos import RegCtasBancoData
from data.regempleado import RegEmpleadoData
from data.regfacturas import RegFacturaData
from data.reggastos import RegGastoData
from data.reglocal import RegLocalData
from data.regpagos import  RegCarteraData, RegCobranzaData
from data.ubicaciones import  AreasData, ListaAreasData, ListaCuotasData, UbicacionesData
from data.usuario import UsuarioData
from model.ctasbancos import Cuentas
from model.editcontrato import EditContrato
from model.operaciones import Reg_Cartera, Reg_Cobranza, Reg_Factura, Reg_Gasto
from model.regProveedor import RegProveedor
from model.regareac import RegAC
from model.regcliente import RegCliente
from model.regcontrato import RegContrato
from model.regempleado import RegEmpleado
from model.reglocal import RegLocal
from model.regperiodofacturacion import RegPeriodoFacturacion
from model.user import Usuario 
import xlsxwriter
from PyQt6.QtGui import QIcon

current_datetime = datetime.today()

###############################################PANTALLA PRINCIPAL####################################################################################

class PantallaPrincipal():
    def __init__(self):
        icon_pp= QIcon("iconos/cartera.ico")  
        self.pp = uic.loadUi("gui/formMain.ui")
        self.pp.setWindowIcon(icon_pp)
        self.pp.setWindowTitle("Gestor Administrativo Condominal")
        self.pp.show()
        self.pp.resize(1132,805)
        self.pp.lblImagen.setGeometry(9,9,1200,690)
        self.pp.btnInvisible.setGeometry(130,410,211,20)
        self.pp.btnInvisible.setFlat(True)
        self.pp.btnInvisible.clicked.connect(self.mostrar_recuperar_pass)
        self.pp.btnRecuperar.setVisible(False) 
        self.pp.menubar.setVisible(False)
        self.pp.txtNameUser.setVisible(False)
        self.pp.btnReiniciar.setVisible(False)
        self.pp.btnEntrar.clicked.connect(self.validar_acceso)
        self.pp.btnNewUser.clicked.connect(self.reg_new_user)
        self.pp.btnIngresar.clicked.connect(self.mostrar_panel)
        self.pp.btnRegresar.clicked.connect(self.ocultar_panel)
        self.pp.actionRegMovCM.triggered.connect(self.abrir_form_PPCM)
        self.pp.actionRegMovAC.triggered.connect(self.abrir_form_PPAC)    
        self.pp.actionRegistrar_cliente.triggered.connect(self.abrir_form_clientes)
        self.pp.btnReiniciar.clicked.connect(self.reiniciar_sistema)
        self.pp.btnRecuperar.clicked.connect(self.recuperar_pass)
        self.pp.actionAltaLocal.triggered.connect(self.abrir_form_alta_local)
        self.pp.actionAltaAC.triggered.connect(self.abrir_form_alta_AC)
        self.pp.actionCarga_Clientes.triggered.connect(self.carga_clientes_bd)
        self.pp.actionCarga_Locales.triggered.connect(self.carga_ubicaciones_bd)
        self.pp.actionCarga_Areas_Comunes.triggered.connect(self.carga_areasC_bd)
        self.pp.actionCarga_Contratos.triggered.connect(self.carga_contratos_bd)
        self.pp.actionCarga_Saldos_Iniciales.triggered.connect(self.carga_saldos_iniciales_cartera)
        self.pp.toolButton.clicked.connect(self.mostrar_password)
        self.pp.actionRegCuentas.triggered.connect(self.abrir_form_banco)
        self.pp.actionRegContrato.triggered.connect(self.abrir_form_contratos)
        self.pp.actionBuscar_Contratos.triggered.connect(self.abrir_form_buscar_contratos)
        self.pp.actionFacturacion_Masiva.triggered.connect(self.abrir_form_cmasiva)
        self.pp.actionRegistrar_Gastos.triggered.connect(self.abrir_form_gastos)
        self.pp.actionAlta_Prest_Serv.triggered.connect(self.abrir_form_alta_proveedor)
        self.pp.actionAlta_Empleado.triggered.connect(self.abrir_form_alta_empleado)
        self.pp.btnSalirPP.clicked.connect(self.salir_pp) 
    
            
    def carga_clientes_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Clientes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 14:
                            m.setText("El archivo CSV no tiene el formato correcto")
                            m.exec()
                            return
                        carga_clientes = RegCliente(
                            nombre=row[1],
                            rfc=row[2],
                            tContribuyente=row[3],
                            curp=row[4],
                            num_area_o_local=row[5],
                            tCliente=row[6],
                            giro=row[7],
                            direccion=row[8],
                            numcel=row[9],
                            email=row[10],
                            fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            status_cliente=row[12],
                            usuario=row[13]
                        )
                        objData = RegClienteData()
                        if objData.registrar(carga_clientes):
                            m.setText("info clientes cargada con exito")
                        else:
                            m.setText("clientes no registrados")
                except Exception as e:
                    m.setText(f"Error en la carga de clientes  : {e}")        
        m.exec()               
                        
    def carga_ubicaciones_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Locales")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 12:
                            m.setText("El archivo CSV no tiene el formato correcto")
                            m.exec()
                            return
                        carga_locales = RegLocal(
                            num_local=row[1],
                            superficie=row[2],
                            cuota=row[3],
                            dg=row[4],
                            nom_propietario=row[5],
                            rfc_propietario=row[6],
                            cliente=row[7],
                            giro=row[8],
                            status=False,
                            usuario=self.pp.lblName_User.text(),
                            fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData = RegLocalData()
                        if objData.registrar(carga_locales):
                            m.setText("Ubicaciones cargadas con exito")
                        else:
                            m.setText("base datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de ubicaciones: {e}")        
        m.exec()                           
                
    def carga_areasC_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Areas Comunes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 13:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_areas = RegAC(
                            num_area=row[1],
                            cliente_fact=row[2],
                            cuota=row[3],
                            dg=row[4],
                            tipo_area=row[5],
                            cantidad=row[6],
                            sup=row[7],
                            giro=row[8],
                            contrato=row[9],
                            status=False,
                            fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            usuario=self.pp.lblName_User.text()
                            )
                        objData = RegACData()
                        if objData.registrar(carga_areas):
                            m.setText("Areas Comunes cargadas con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de areas comunes: {e}")
        m.exec()             
    
    def carga_contratos_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Contratos")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 13:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_contratos = RegContrato(
                            n_contrato=row[1],
                            c_facturacion=row[2],
                            n_area=row[3],
                            f_inicio=row[4],
                            f_fin=row[5],
                            m_cuota=row[6],
                            m_dg=row[7],
                            t_contrato=row[8],
                            s_contrato=row[9],
                            s_vigencia=row[10],
                            r_usuario=self.pp.lblName_User.text(),
                            f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData = RegContratoData()
                        if objData.registrar(carga_contratos):
                            m.setText("Contratos cargados con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de contratos : {e}")
        m.exec()             
        
    def carga_saldos_iniciales_cartera(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Saldos Iniciales")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 18:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_carteraini = Reg_Cartera(
                            local_o_area=row[1],
                            clienteFact=row[2],
                            tipoCartera=row[3],
                            tipoCuota=row[4],
                            tipo_factura=row[5],
                            numFact=row[6],
                            importeAdeudo=row[7],
                            importePago=row[8],
                            fPago_Cobro=row[9],
                            ctaBanco=row[10],
                            formaPago=row[11],
                            cheque=row[12],
                            numContrato=row[13],
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios=row[17]
                            )
                        objData = RegCarteraData()
                        if objData._registrar(carga_carteraini):
                            m.setText("Saldos Iniciales cargados con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de saldos iniciales: {e}")
        m.exec()                                      
        
    def mostrar_panel(self):
        self.pp.lblImagen.setGeometry(9,9,680,690)
        self.pp.btnNewUser.setGeometry(110, 490, 250, 30)
        self.pp.btnIngresar.setVisible(False)
        self.pp.btnNewUser.setText("Nuevo Usuario")
        self.pp.btnInvisible.setVisible(True)
        self.pp.lblRecPassword.setVisible(True) 
        self.pp.btnEntrar.setVisible(True)
        self.pp.btnNewUser.setVisible(True)
        self.pp.txtPassword.setVisible(True)
        #self.pp.txtUsuario.setText("")
        #self.pp.txtPassword.setText("")
        self.pp.txtNameUser.setText("")
        self.pp.toolButton.setVisible(True)
        self.pp.txtUsuario.setText("administrador")
        self.pp.txtPassword.setText("adMin_81@")
        
    def ocultar_panel(self):
        self.pp.btnIngresar.setVisible(True)
        self.pp.lblImagen.setGeometry(9,9,1200,690) 
        self.pp.txtNameUser.setVisible(False)
        self.pp.btnNewUser.setVisible(False)
        self.pp.btnRecuperar.setVisible(False)
        self.pp.txtUsuario.setText("")
        self.pp.txtPassword.setText("")
                      
    def mostrar_password(self):
        self.pp.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)    
            
    def salir_pp(self):
        self.pp.close()  
 
 
 ##############################################LOG IN###################################################       
    def validar_acceso(self):
        self.pp.actionCarga_Clientes.setEnabled(False)
        self.pp.actionCarga_Locales.setEnabled(False)
        self.pp.actionCarga_Areas_Comunes.setEnabled(False)
        self.pp.actionCarga_Contratos.setEnabled(False)
        self.pp.actionCarga_Saldos_Iniciales.setEnabled(False)
        self.pp.actionRegCuentas.setEnabled(False)
        self.pp.actionAltaLocal.setEnabled(False)
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Log In")
        
        if  self.pp.txtUsuario.text()=="":
            m.setText("Ingrese un Usuario")    
            self.pp.txtUsuario.setFocus()
            
        elif self.pp.txtPassword.text()=="":
            m.setText("Ingrese una contraseña")
            self.pp.txtPassword.setFocus()        
        else:
            user_info= Usuario(usuario=self.pp.txtUsuario.text(),clave=self.pp.txtPassword.text())
            usuData= UsuarioData()
            res= usuData.login(user_info)
            if res:
                self.pp.menubar.setVisible(True)
                nom_user=self.pp.txtUsuario.text()
                self.pp.lblImagen.setGeometry(9,9,1200,690) 
                m.setText("Hola""  " + nom_user)
                self.pp.btnIngresar.setVisible(True)
                self.pp.btnReiniciar.setVisible(True)
                self.pp.statusBar.showMessage("Bienvenido" " "+ nom_user,0)
                self.pp.lblName_User.setText(nom_user)
                if nom_user == "administrador":
                    self.pp.actionCarga_Clientes.setEnabled(True)
                    self.pp.actionCarga_Locales.setEnabled(True)
                    self.pp.actionCarga_Areas_Comunes.setEnabled(True)
                    self.pp.actionCarga_Contratos.setEnabled(True)
                    self.pp.actionCarga_Saldos_Iniciales.setEnabled(True)
                    self.pp.actionRegCuentas.setEnabled(True)
                    self.pp.actionAltaLocal.setEnabled(True)
                else:
                    self.pp.actionRegCuentas.setEnabled(True)       
            else:
                m.setText("Usuario o Contraseña no validos")
                m.setIcon(QMessageBox.Icon.Warning)
                self.pp.btnNewUser.setVisible(True)
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                self.pp.txtUsuario.setFocus()
        m.exec()        
        
    def reg_new_user(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setWindowTitle("Registrar Usuario")
        self.pp.btnEntrar.setVisible(False)
        self.pp.btnInvisible.setVisible(False)
        self.pp.btnNewUser.setGeometry(110, 440, 250, 31)
        self.pp.txtNameUser.setGeometry(110,250,250,30)
        self.pp.btnNewUser.setText("Registrar")
        self.pp.txtNameUser.setVisible(True)
        self.pp.lblRecPassword.setVisible(False)
        self.pp.txtNameUser.setFocus()
        # self.pp.txtUsuario.setText("")
        # self.pp.txtPassword.setText("")
        
        nombre= self.pp.txtNameUser.text()
        usuario = self.pp.txtUsuario.text()
        password = self.pp.txtPassword.text()
    
        if nombre=="":
            mensaje.setText("Ingrese un Nombre")
            self.pp.txtNameUser.setFocus()  
        elif usuario == "":
            mensaje.setText("Ingrese un Usuario")
            self.pp.txtUsuario.setFocus()
            
        elif len(usuario)<5:
            mensaje.setText("El usuario debe tener al menos 5 caracteres")
            self.pp.txtUsuario.setFocus() 
               
        elif password == "":
            mensaje.setText("Ingrese una Contraseña")
            self.pp.txtPassword.setFocus()
                    
        elif len(password)<8:
            mensaje.setText("La contraseña debe tener al menos 8 caracteres")
            self.pp.txtPassword.setFocus()
            
        elif not any(char in "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" for char in password):
            mensaje.setText("La contraseña debe contener al menos una letra mayuscula")
            self.pp.txtPassword.setFocus()    
            
        elif not any(char in "@ # $ % & *" for char in password):
            mensaje.setText("La contraseña debe contener al menos un carácter especial: @ # $ % & * ")
            self.pp.txtPassword.setFocus()
        else:
            usuData = UsuarioData()
            nuevo_usuario = Usuario(nombre=nombre,usuario=usuario, clave=password,usuario_reg=self.pp.lblName_User.text())
            res = usuData.registrar(nuevo_usuario)
            
            if res:
                mensaje.setText("Usuario registrado exitosamente")
                self.pp.txtNameUser.setText("")
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                self.pp.txtNameUser.setVisible(False)
                self.pp.btnEntrar.setVisible(True)
                self.ocultar_panel()
            else:
                self.pp.txtNameUser.setText("")
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                mensaje.setIcon(QMessageBox.Icon.Warning)
                mensaje.setText("Usuario ya Registrado") 
        mensaje.exec()    
        
    def mostrar_recuperar_pass(self):
        self.pp.btnInvisible.setVisible(False)
        self.pp.lblRecPassword.setVisible(False)
        self.pp.txtPassword.setVisible(False)
        self.pp.btnEntrar.setVisible(False)
        self.pp.btnNewUser.setVisible(False)
        self.pp.btnRecuperar.setVisible(True)
        self.pp.toolButton.setVisible(False)
        self.pp.btnRecuperar.setGeometry(110,440,250,31)
        self.pp.txtUsuario.setText("")
        self.pp.txtPassword.setText("")
        self.pp.txtUsuario.setFocus()
        
    def recuperar_pass(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Recuperar Contraseña")
        
        usuario = self.pp.txtUsuario.text()
        
        if usuario == "":
            m.setText("Ingrese un Usuario")
            self.pp.txtUsuario.setFocus()
        else:
            usuData = UsuarioData()
            res = usuData.recuperar(usuario)
            
            if res:
                m.setText(f"Su contraseña es :  {res}")
                self.pp.txtUsuario.setText("")
            else:
                m.setText("Usuario no encontrado")
                m.setIcon(QMessageBox.Icon.Warning)
                self.pp.txtUsuario.setText("")
                
        m.exec()
    
 
 #################################ALTA LOCALES COMERCIALES###############################################   
    def abrir_form_alta_local(self):
        self.fal=uic.loadUi("gui/formLocales.ui")
        self.fal.setWindowTitle("Alta Local Comercial")
        self.fal.show()
        self.fal.txtLocal.setText("L-")
        self.set_cmb_clientes()
        self.fal.btnGuardar.clicked.connect(self.registrar_local)
        self.fal.btnSalir.clicked.connect(self.salir_form_local) 
            
    def registrar_local(self):       
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Alta Local Comercial")
            m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
            if self.fal.txtLocal.text()=="":       
                m.setText("Capture numero de Local")
                self.fal.txtLocal.setFocus()
            
            elif len(self.fal.txtLocal.text())<4:
                m.setText("Numero de local incorrecto")
                self.fal.txtLocal.setFocus()
                    
            elif self.fal.txtSuperficie.text()=="":
                m.setText(" Capture superficie m2")
                self.fal.txtSuperficie.setFocus()
            
            elif not self.fal.txtSuperficie.text().replace('.','',1).isnumeric():   
                m.setText("Captura solo numeros")
                self.fal.txtSuperficie.setText('0.00')
                self.fal.txtSuperficie.setFocus()    
                                
            elif self.fal.cmbClientes.currentIndex()==0:
                m.setText("Selecciona una opcion")
                self.fal.cmbClientes.setFocus()
        
            elif self.fal.txtGiro.text()=="":
                m.setText("Capture Giro del Local")
                self.fal.txtGiro.setFocus()
            
            elif  self.fal.txtCuota.text()=="":
                m.setText("Capture Cuota Mensual")        
                self.fal.txtCuota.setFocus()
                 
            elif not self.fal.txtCuota.text().replace('.',"" ,1).isnumeric():   
                m.setText("Captura solo numeros")
                self.fal.txtCuota.setText('0.00')
                self.fal.txtCuota.setFocus()
            
            elif self.fal.txtRFC_p.text()=="":
                m.setText("Capture RFC Propietario")
                self.fal.txtRFC_p.setFocus()
                
            elif self.fal.txtPropietario.text()=="":
                m.setText("Capture Nombre Propietario")
                self.fal.txtPropietario.setFocus()
                
            else:
                reg_local=RegLocal(
                    num_local=self.fal.txtLocal.text().upper(),
                    superficie=self.fal.txtSuperficie.text(),
                    cuota=self.fal.txtCuota.text(),
                    dg=0,
                    nom_propietario=self.fal.txtPropietario.text().upper(),
                    rfc_propietario=self.fal.txtRFC_p.text().upper(),
                    cliente=self.fal.cmbClientes.currentText().upper(),
                    giro=self.fal.txtGiro.text().upper(),
                    status=False,
                    usuario=self.pp.lblName_User.text(),
                    fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=RegLocalData() 
                if  objData.registrar(info=reg_local):
                    m.setText("Local registrado con exito")
                    self.limpiar_campos_fal()
                else:
                    m.setText("El Local  " + self.fal.txtLocal.text() + "   ya esta registrado")
                    self.limpiar_campos_fal()  
            m.exec()
    
    def set_cmb_clientes(self):
        obj=ClientesData()
        datos=obj.lista_clientes()
        for item in datos:
            self.fal.cmbClientes.addItem(item[1])
          
    def limpiar_campos_fal(self):
        self.fal.txtLocal.setText("")
        self.fal.txtSuperficie.setText("")
        self.fal.txtCuota.setText("")
        self.fal.txtPropietario.setText("")
        self.fal.txtRFC_p.setText("")
        self.fal.cmbClientes.setCurrentIndex(0)
        self.fal.txtGiro.setText("")        
     
    def salir_form_local(self):
        self.fal.close()        
     
          
 #################################ALTA AREAS COMUNES##############################################   
    def abrir_form_alta_AC(self):
        self.fac=uic.loadUi("gui/formAreasComunes.ui")
        self.fac.setWindowTitle("Alta area comun")
        self.fac.show()
        self.set_cmb_cliente()
        self.fac.btnGuardar.clicked.connect(self.registrar_area)
        self.fac.btnSalir.clicked.connect(self.salir_form_area)
        
    def set_cmb_cliente(self):
        obj=ClientesData()
        datos=obj.lista_clientes()
        for item in datos:
            self.fac.cmbClientes.addItem(item[1])    
 
    def registrar_area(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Alta area comun")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fac.txtArea.text()=="":       
            m.setText("Capture numero de Area Comun")
            self.fac.txtArea.setFocus()
            
        elif len(self.fac.txtArea.text())<4:
            m.setText("Numero de Area Comun incorrecto")
            self.fac.txtArea.setFocus()
                
        elif self.fac.txtSuperficie.text()=="":
            m.setText(" Capture superficie m2")
            self.fac.txtSuperficie.setFocus()
        
        elif not self.fac.txtSuperficie.text().replace('.','',1).isnumeric():   
            m.setText("Captura solo numeros")
            self.fac.txtSuperficie.setText('0.00')
            self.fac.txtSuperficie.setFocus()    
                        
        elif self.fac.cmbClientes.currentIndex()==0:
            m.setText("Seleccione una opcion")
            self.fac.cmbClientes.setFocus()
    
        elif self.fac.txtGiro.text()=="":
            m.setText("Capture Giro del Area Comun")
            self.fac.txtGiro.setFocus()
        
        elif  self.fac.txtCuota.text()=="":
            m.setText("Capture Cuota Mensual")        
            self.fac.txtCuota.setFocus()
            
        elif not self.fac.txtCuota.text().replace('.',"" ,1).isnumeric():   
            m.setText("Captura solo numeros")
            self.fac.txtCuota.setText('0.00')
            self.fac.txtCuota.setFocus()
        
        elif self.fac.cmbTipoArea.currentIndex()==0:
            m.setText("Selecione una opcion")
            self.fac.txtRFC_p.setFocus()
            
        elif self.fac.txtDG.text()=="":
            m.setText("Capture Deposito Garantia")
            self.fac.txtDG.setFocus()
            
        else:
            reg_area=RegAC(
                num_area=self.fac.txtArea.text().upper(),
                cliente_fact=self.fac.cmbClientes.currentText().upper(),
                cuota=self.fac.txtCuota.text(),
                dg=self.fac.txtDG.text(),
                tipo_area=self.fac.cmbTipoArea.currentText(),
                cantidad=1,
                sup=self.fac.txtSuperficie.text(),
                giro=self.fac.txtGiro.text().upper(),
                contrato="",
                status=False,
                fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                usuario=self.pp.lblName_User.text()
                )
            objData=RegACData()
            if  objData.registrar(info=reg_area):
                m.setText("Area Comun registrada con exito")
                self.limpiar_campos_fac()
            else:
                m.setText("El Area Comun  " + self.fac.txtArea.text() + "   ya esta registrado")
                self.limpiar_campos_fac()
        m.exec()
     
    def limpiar_campos_fac(self):
        self.fac.txtArea.setText("")
        self.fac.txtSuperficie.setText("")
        self.fac.txtCuota.setText("")
        self.fac.cmbClientes.setCurrentIndex(0)
        self.fac.txtGiro.setText("")  
        self.fac.txtDG.setText("") 
        self.fac.cmbTipoArea.setCurrentIndex(0)    
        
    def salir_form_area(self):
        self.fac.close()   
  
               
 #######################   PANTALLA PRINCIPAL GESTOR LOCALES COMERCIALES#############################################         
    def abrir_form_PPCM(self):
        self.ppcm = uic.loadUi("gui/formPrincipalCM.ui")
        self.ppcm.setWindowTitle("Cartera Locales Comerciales")
        self.ppcm.show()
        self.set_cmb_locales_ppcm()
        self.ppcm.cmblocal.currentIndexChanged.connect(self.set_cmb_cliente_ppcm)
        self.ppcm.btnBuscar.clicked.connect(self.mostrar_informacionCM)
        self.ppcm.btnRegCob.clicked.connect(self.validar_campos_PPCM)
        self.ppcm.btnRegFact.clicked.connect(self.abrir_form_facturacionCM)
        self.ppcm.btnEdoCta.clicked.connect(self.exportar_info_a_excelCM)
        self.ppcm.btnSalir.clicked.connect(self.salir_form_PPCM)
                  
    def set_cmb_locales_ppcm(self):
        obj= UbicacionesData()   
        datos=obj.lista_ubicaciones()
        for item in datos:
            self.ppcm.cmblocal.addItem(item[1])
            
    def set_cmb_cliente_ppcm(self,cliente):
        search=BuscarCliente()
        data=search.buscar_cliente(self.ppcm.cmblocal.currentText())
        self.ppcm.tblCarteraCM.clearContents()
        self.ppcm.tblCarteraCM.setRowCount(0)
        self.ppcm.txtSaldo.setText("")
        self.ppcm.txtCliente.setText("")   
        for item in data:
            self.ppcm.txtCliente.setText(item[7])          
                                
    def validar_campos_PPCM(self): 
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("registro cobranza cuotas")
            m.setText("Seleccione una opcion")
            m.exec()
        else:
            self.abrir_form_pagosCM()
            
    def salir_form_PPCM(self):
        self.ppcm.close()         
    
    
################################## PAGOS---COBRANZA---LC --######################################        
    def abrir_form_pagosCM(self):
        self.fpcm=uic.loadUi("gui/formRegPagosCM.ui")
        self.fpcm.setWindowTitle("registro cobranza cuotas")
        self.fpcm.show()
        self.set_cmb_factura_fpcm()
        self.set_cmb_cta_banco_fpcm()
        self.fpcm.btnRegistrar.clicked.connect(self.registrar_cobranzaCM)
        self.fpcm.btnSalir.clicked.connect(self.salir_form_pagosCM) 
        self.fpcm.txtLocal.setText(self.ppcm.cmblocal.currentText())
        
    def set_cmb_factura_fpcm(self):
        search=FacturasData()
        data=search.lista_facturas(self.ppcm.cmblocal.currentText(),self.ppcm.txtCliente.text())
        for item in data:
            self.fpcm.cmbFactura.addItem(item[6])
            
    def set_cmb_cta_banco_fpcm(self):
        obj=ctasbancos.CuentasData()
        datos=obj.lista_ctas()
        for item in datos:
            self.fpcm.cmbCtaBancaria.addItem(item[2])
              
    def registrar_cobranzaCM(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro cobranza")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fpcm.cmbFactura.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.fpcm.cmbFactura.setFocus()        
        
        elif self.fpcm.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbTipoCuota.setFocus()
                            
        elif self.fpcm.txtImporte.text()=="":
            m.setText("captura un importe")
            self.fpcm.txtImporte.setFocus()
        elif not self.fpcm.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.fpcm.txtImporte.setText('0')
            self.fpcm.txtImporte.setFocus()
              
        elif self.fpcm.cmbFormaPago.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbFormaPago.setFocus()        
        
        elif self.fpcm.cmbCtaBancaria.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbCtaBancaria.setFocus()
             
        else:
            regpago=Reg_Cobranza(   
                num_fact=self.fpcm.cmbFactura.currentText(),
                fecha_pago=self.fpcm.boxDate.date().toString("yyyy-MM-dd"),
                importe_pago=self.fpcm.txtImporte.text(),
                forma_pago=self.fpcm.cmbFormaPago.currentText(),
                cta_banco=self.fpcm.cmbCtaBancaria.currentText(),
                num_cheque=self.fpcm.txtCheque.text(),
                tipoCuota=self.fpcm.cmbTipoCuota.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpcm.txtComentarios.toPlainText()
                )
            objData=RegCobranzaData()
            if  objData._registrar(info=regpago):
                m.setText("pago registrado con exito")
            
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.fpcm.txtLocal.text(),
                    clienteFact=self.ppcm.txtCliente.text(),
                    tipoCartera="locales comerciales",
                    tipoCuota=self.fpcm.cmbTipoCuota.currentText(),
                    tipo_factura="pago",
                    numFact=self.fpcm.cmbFactura.currentText(),
                    importeAdeudo=0,
                    importePago=self.fpcm.txtImporte.text(),
                    fPago_Cobro=self.fpcm.boxDate.date().toString("yyyy-MM-dd"),
                    ctaBanco=self.fpcm.cmbCtaBancaria.currentText(),    
                    formaPago=self.fpcm.cmbFormaPago.currentText(),
                    cheque=self.fpcm.txtCheque.text(),
                    numContrato="",
                    statusPago="",
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.fpcm.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_fpcm()
                else:
                    m.setText("registro cartera no exitoso")
                    self.limpiar_campos_fpcm() 
            else:
                m.setText("pago no registrado")
                self.limpiar_campos_fpcm()  
        m.exec()
    
    def limpiar_campos_fpcm(self):
        self.fpcm.cmbFactura.setCurrentIndex(0)
        self.fpcm.cmbTipoCuota.setCurrentIndex(0)
        self.fpcm.txtImporte.setText("")
        self.fpcm.cmbFormaPago.setCurrentIndex(0)
        self.fpcm.cmbCtaBancaria.setCurrentIndex(0)
        self.fpcm.txtCheque.setText("")
        self.fpcm.txtComentarios.setText("")
    
    def salir_form_pagosCM(self):
        self.fpcm.close() 
    
    
####################################### ---FACTURACION INDIVIDUAL--LC--######################################          
    def abrir_form_facturacionCM(self):
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setWindowTitle("registro facturas cuotas")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppcm.cmblocal.setFocus()
        else:    
            self.ffcm=uic.loadUi("gui/formRegFacturasCM.ui")
            self.ffcm.setWindowTitle("registro facturas cuotas")
            self.ffcm.show()
            self.ffcm.txtNumFact.setText("F-")
            self.ffcm.txtLocal.setText(self.ppcm.cmblocal.currentText())
            self.ffcm.btnRegistrar.clicked.connect(self.registrar_facturacionCM) 
            self.ffcm.btnSalir.clicked.connect(self.salir_form_facturacionCM)   
        
    def registrar_facturacionCM(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro facturas")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
            
        if self.ffcm.txtLocal.text()=="":
            m.setText("captura numero local")
            self.ffcm.txtLocal.setFocus()
                        
        elif self.ffcm.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.ffcm.cmbTipoCuota.setFocus()
        
        elif self.ffcm.txtNumFact.text()=="":
            m.setText("captura una factura")
            self.ffcm.txtNumFact.setFocus()
                
        elif self.ffcm.txtImporte.text()=="":
            m.setText("captura un importe")
            self.ffcm.txtImporte.setFocus()
        elif not self.ffcm.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.ffcm.txtImporte.setText('0')
            self.ffcm.txtImporte.setFocus()
                
        else:
            regfact=Reg_Factura(   
                num_factura=self.ffcm.txtNumFact.text().upper(),
                cliente=self.ppcm.txtCliente.text(),
                local_o_area=self.ffcm.txtLocal.text().upper(),
                fecha_factura=self.ffcm.boxDate.date().toString("yyyy-MM-dd"),
                tipo_cuota=self.ffcm.cmbTipoCuota.currentText(),
                importe_factura=self.ffcm.txtImporte.text(),
                tipo_factura=self.ffcm.cmbTipoFact.currentText(),
                tipo_cartera="locales comerciales",
                status_pago=False,
                usuario=self.pp.lblName_User.text(),
                fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegFacturaData()
            if  objData._registrar(info=regfact):
                m.setText("factura registrada con exito")
    
                if self.ffcm.cmbTipoFact.currentIndex() == 2 or self.ffcm.cmbTipoFact.currentIndex() == 3:
                    importeAdeudo = -1 * float(self.ffcm.txtImporte.text())
                else:
                    importeAdeudo = float(self.ffcm.txtImporte.text())
                
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.ffcm.txtLocal.text().upper(),
                    clienteFact=self.ppcm.txtCliente.text(),
                    tipoCartera="locales comerciales",
                    tipoCuota=self.ffcm.cmbTipoCuota.currentText(),
                    tipo_factura=self.ffcm.cmbTipoFact.currentText(),
                    numFact=self.ffcm.txtNumFact.text().upper(),
                    importeAdeudo=importeAdeudo,
                    importePago=0,
                    fPago_Cobro=self.ffcm.boxDate.date().toString("yyyy-MM-dd"), 
                    ctaBanco="",
                    formaPago="",
                    cheque="",
                    numContrato="",
                    statusPago=False,
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.ffcm.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_ffcm()
                else:
                    m.setText("registro cartera no exitoso")   
                    self.limpiar_campos_ffcm()
            else:
                m.setText("factura no registrada")
                self.limpiar_campos_ffcm()
        m.exec()
        
    def limpiar_campos_ffcm(self):
        self.ffcm.cmbTipoCuota.setCurrentIndex(0)
        self.ffcm.txtNumFact.setText("")
        self.ffcm.txtImporte.setText("")
        self.ffcm.cmbTipoFact.setCurrentIndex(0)
        self.ffcm.txtComentarios.setText("")

    def salir_form_facturacionCM(self):
        self.ffcm.close()   
   
   
#############################PANTALLA PRINCIPAL GESTOR AREAS COMUNES#############################################    
    def abrir_form_PPAC(self):
        self.ppac = uic.loadUi("gui/formPrincipalAC.ui")
        self.ppac.setWindowTitle("Cartera Areas Comunes")
        self.ppac.show()   
        self.set_cmb_contratos_PPAC()
        self.ppac.cmbContrato.currentIndexChanged.connect(self.set_cmb_area_PPAC)
        self.ppac.btnBuscar.clicked.connect(self.mostrar_informacionAC)
        self.ppac.btnRegCob.clicked.connect(self.validar_campos_PPAC)
        self.ppac.btnRegFact.clicked.connect(self.abrir_form_facturacionAC)
        self.ppac.btnEdoCta.clicked.connect(self.exportar_info_a_excelAC)
        self.ppac.btnSalir.clicked.connect(self.salir_form_PPAC)
  
    def validar_campos_PPAC(self): 
        if self.ppac.cmbContrato.currentIndex()==0: 
            m=QMessageBox()
            m.setWindowTitle("registrar cobranza")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una opcion")
            m.exec()
        else:
            self.abrir_form_pagosAC()
            
    def set_cmb_contratos_PPAC(self):
        search=ContratosData()
        data=search.lista_contratos()
        for item in data:
            self.ppac.cmbContrato.addItem(item[1]) 
            
    def set_cmb_area_PPAC(self,contrato):
        search=AreasData()
        data=search.lista_areas_x_contrato(self.ppac.cmbContrato.currentText())
        self.ppac.cmbAreaC.clear()
        self.ppac.txtCliente.setText("")
        self.ppac.tblCarteraAC.clearContents()
        self.ppac.tblCarteraAC.setRowCount(0)
        self.ppac.txtSaldo.setText("")   
        for item in data:
            self.ppac.cmbAreaC.addItem(item[3])
            self.ppac.txtCliente.setText(item[2])
                  
    def salir_form_PPAC(self):
        self.ppac.close()    
    
    
################################## PAGOS---COBRANZA--AC --######################################        
    def abrir_form_pagosAC(self):
        self.fpac=uic.loadUi("gui/formRegPagosAC.ui")
        self.fpac.setWindowTitle("registro cobranza cuotas")
        self.fpac.show()
        self.set_cmb_factura_fpac()
        self.set_cmb_cta_banco_fpac()
        self.fpac.txtAreaC.setText(self.ppac.cmbAreaC.currentText())
        self.fpac.btnRegistrar.clicked.connect(self.registrar_cobranzaAC)
        self.fpac.btnSalir.clicked.connect(self.salir_form_pagosAC)
        
    def set_cmb_factura_fpac(self):
        search=FacturasData()
        data=search.lista_facturas(self.ppac.cmbAreaC.currentText(),self.ppac.txtCliente.text())
        for item in data:
            self.fpac.cmbFactura.addItem(item[6])
            
    def set_cmb_cta_banco_fpac(self):
        obj=ctasbancos.CuentasData()
        datos=obj.lista_ctas()
        for item in datos:
            self.fpac.cmbCtaBancaria.addItem(item[2])        
             
    def registrar_cobranzaAC(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro cobranza")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
                
        if self.fpac.txtAreaC.text()=="":
            m.setText("captura numero area")
            self.fpac.txtAreaC.setFocus()
                        
        elif self.fpac.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.fpac.cmbTipoCuota.setFocus()
        
        elif self.fpac.cmbFactura.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbFactura.setFocus()
                
        elif self.fpac.txtImporte.text()=="":
            m.setText("captura un importe")
            self.fpac.txtImporte.setFocus()
        elif not self.fpac.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.fpac.txtImporte.setText('0')
            self.fpac.txtImporte.setFocus()
              
        elif self.fpac.cmbFormaPago.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbFormaPago.setFocus()        
        
        elif self.fpac.cmbCtaBancaria.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbCtaBancaria.setFocus()
                
        else:
            regpago=Reg_Cobranza(   
                num_fact=self.fpac.cmbFactura.currentText(),
                fecha_pago=self.fpac.boxDate.date().toString("yyyy-MM-dd"),
                importe_pago=self.fpac.txtImporte.text(),
                forma_pago=self.fpac.cmbFormaPago.currentText(),
                cta_banco=self.fpac.cmbCtaBancaria.currentText(),
                num_cheque=self.fpac.txtCheque.text(),
                tipoCuota=self.fpac.cmbTipoCuota.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpac.txtComentarios.toPlainText()
                )
            objData=RegCobranzaData()
            if  objData._registrar(info=regpago):
                m.setText("pago registrado con exito")
            
                carga=Reg_Cartera(
                local_o_area=self.fpac.txtAreaC.text(),
                clienteFact=self.ppac.txtCliente.text(),
                tipoCartera="areas comunes",
                tipo_factura="pago",
                tipoCuota=self.fpac.cmbTipoCuota.currentText(),
                numFact=self.fpac.cmbFactura.currentText(),
                importeAdeudo=0,
                importePago=self.fpac.txtImporte.text(),
                fPago_Cobro=self.fpac.boxDate.date().toString("yyyy-MM-dd"), 
                ctaBanco=self.fpac.cmbCtaBancaria.currentText(),
                formaPago=self.fpac.cmbFormaPago.currentText(),
                cheque=self.fpac.txtCheque.text(),
                numContrato=self.ppac.cmbContrato.currentText(),
                statusPago="",
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpac.txtComentarios.toPlainText()
                )
                objData=RegCarteraData()
                if  objData._registrar(info=carga):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_fpac()
                else:
                    m.setText("registro cartera no exitoso") 
                    self.limpiar_campos_fpac()
            else:
                m.setText("pago no registrado")  
                self.limpiar_campos_fpac()
        m.exec()
        
    def limpiar_campos_fpac(self):
        self.fpac.cmbFactura.setCurrentIndex(0)
        self.fpac.cmbTipoCuota.setCurrentIndex(0)
        self.fpac.txtImporte.setText("")
        self.fpac.cmbFormaPago.setCurrentIndex(0)
        self.fpac.cmbCtaBancaria.setCurrentIndex(0)
        self.fpac.txtCheque.setText("")
        self.fpac.txtComentarios.setText("")
                
    def salir_form_pagosAC(self):
        self.fpac.close() 

        
################################## ---FACTURACION INDIVIDUAL--AC --######################################           
    def abrir_form_facturacionAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setWindowTitle("registro facturas")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppac.cmbContrato.setFocus()
        else:
            self.ffac=uic.loadUi("gui/formRegFacturasAC.ui")
            self.ffac.setWindowTitle("registro facturas cuotas")
            self.ffac.show()
            self.ffac.txtNumFact.setText("F-")
            self.ffac.txtAreaC.setText(self.ppac.cmbAreaC.currentText())
            self.ffac.btnRegistrar.clicked.connect(self.registrar_facturacionAC) 
            self.ffac.btnSalir.clicked.connect(self.salir_form_facturacionAC)   
            
    def registrar_facturacionAC(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("registro facturacion")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
                
        if self.ffac.txtAreaC.text()=="":
            m.setText("captura numero area")
            self.ffac.txtAreaC.setFocus()
                    
        elif self.ffac.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.ffac.cmbTipoCuota.setFocus()
        
        elif self.ffac.txtNumFact.text()=="":
            m.setText("captura una factura")
            self.ffac.txtNumFact.setFocus()
                
        elif self.ffac.txtImporte.text()=="":
            m.setText("captura un importe")
            self.ffac.txtImporte.setFocus()
        elif not self.ffac.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.ffac.txtImporte.setText('0')
            self.ffac.txtImporte.setFocus()
                
        else:
            regpago=Reg_Factura(   
                num_factura=self.ffac.txtNumFact.text().upper(),
                cliente=self.ppac.txtCliente.text(),
                local_o_area=self.ffac.txtAreaC.text().upper(),
                fecha_factura=self.ffac.boxDate.date().toString("yyyy-MM-dd"),
                tipo_cuota=self.ffac.cmbTipoCuota.currentText(),
                importe_factura=self.ffac.txtImporte.text(),
                tipo_factura=self.ffac.cmbTipoFact.currentText(),
                tipo_cartera="areas comunes",
                status_pago=False,
                usuario=self.pp.lblName_User.text(),
                fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegFacturaData()
            if  objData._registrar(info=regpago):
                m.setText("factura registrada con exito")

                if self.ffac.cmbTipoFact.currentIndex() == 2 or self.ffac.cmbTipoFact.currentIndex() == 3:
                    importe_Adeudo = -1 * float(self.ffac.txtImporte.text())
                else:
                    importe_Adeudo = float(self.ffac.txtImporte.text())
                
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.ffac.txtAreaC.text().upper(),
                    clienteFact=self.ppac.txtCliente.text(),
                    tipoCartera="areas comunes",
                    tipoCuota=self.ffac.cmbTipoCuota.currentText(),
                    tipo_factura=self.ffac.cmbTipoFact.currentText(),
                    numFact=self.ffac.txtNumFact.text().upper(),
                    importeAdeudo=importe_Adeudo,
                    importePago=0,
                    fPago_Cobro=self.ffac.boxDate.date().toString("yyyy-MM-dd"), 
                    ctaBanco="",
                    formaPago="",
                    cheque="",
                    numContrato=self.ppac.cmbContrato.currentText(),
                    statusPago=False,
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.ffac.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_ffac()
                else:
                    m.setText("registro cartera no exitoso")
                    self.limpiar_campos_ffac()
            else:
                m.setText("factura no registrada")           
                self.limpiar_campos_ffac()
        m.exec()
        
    def limpiar_campos_ffac(self):
        self.ffac.cmbTipoCuota.setCurrentIndex(0)
        self.ffac.txtNumFact.setText("")
        self.ffac.txtImporte.setText("")
        self.ffac.cmbTipoFact.setCurrentIndex(0)
        self.ffac.txtComentarios.setText("")        
   
    def salir_form_facturacionAC(self):
        self.ffac.close()   
   
                 
##########################  CLIENTES #########################################   
    def abrir_form_clientes(self):
        self.fcl=uic.loadUi("gui/formClientes.ui")
        self.fcl.setWindowTitle("Registro Clientes")
        self.fcl.show()
        self.fcl.checkBoxStatus.setChecked(True)
        self.fcl.btnGuardar.clicked.connect(self.registrar_cliente)
        self.fcl.btnSalir.clicked.connect(self.salir_form_clientes)  
       
    def registrar_cliente(self):      
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("registro clientes")
            m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
            if self.fcl.txtNombreCliente.text()=="":       
                m.setText("Captura un Nombre")
                self.fcl.txtNombreCliente.setFocus()
                    
            elif self.fcl.txtRFC.text()=="":
                m.setText(" Captura RFC")
                self.fcl.txtRFC.setFocus()
                            
            elif self.fcl.cmbTipoCliente.currentIndex()==0:
                m.setText("Selecciona una Opcion")     
                self.fcl.cmbTipoCliente.setFocus()
                
            elif self.fcl.txtEmail.text()=="":
                m.setText("Captura Email")
                self.fcl.txtEmail.setFocus()
        
            elif self.fcl.txtGiro.text()=="":
                m.setText("Captura Giro")
                self.fcl.txtGiro.setFocus()
            
            elif  self.fcl.txtCel.text()=="":
                m.setText("Captura un numero")        
                self.fcl.txtCel.setFocus()
                
            elif not self.fcl.txtCel.text().isnumeric():      
                m.setText("Captura solo numeros")
                self.fcl.txtCel.setText('5')
                self.fcl.txtCel.setFocus()
            
            elif len(self.fcl.txtCel.text())<10:
                m.setText("Captura un numero correcto")
                self.fcl.txtCel.setFocus()
            else:
                regcliente=RegCliente(
                    nombre=self.fcl.txtNombreCliente.text().upper(),
                    rfc= self.fcl.txtRFC.text().upper(),
                    tContribuyente=self.fcl.cmbTipoCliente.currentText(),
                    curp=self.fcl.txtCURP.text().upper(),
                    num_area_o_local="",
                    giro=self.fcl.txtGiro.text(),
                    direccion=self.fcl.txtDireccion.toPlainText(),
                    numcel=self.fcl.txtCel.text(),
                    email=self.fcl.txtEmail.text().lower(),
                    fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    usuario=self.pp.lblName_User.text(),
                    status_cliente=self.fcl.checkBoxStatus.isChecked(),
                    tCliente=self.fcl.cmbTipoCliente.currentText()
                    )
                objData=RegClienteData()
                if  objData.registrar(info=regcliente):
                    m.setText("cliente registrado con exito")
                    self.limpiar_campos_fcl()
                else:
                    m.setText("cliente no registrado")       
                    self.limpiar_campos_fcl()
            m.exec()
            
    def limpiar_campos_fcl(self):
        self.fcl.txtNombreCliente.setText("")
        self.fcl.txtRFC.setText("")
        self.fcl.cmbTipoCliente.setCurrentIndex(0)
        self.fcl.txtCURP.setText("")
        self.fcl.txtGiro.setText("")
        self.fcl.txtDireccion.setText("")
        self.fcl.txtCel.setText("")
        self.fcl.txtEmail.setText("")
        #self.fcl.checkBoxStatus.setChecked(True)        

    def salir_form_clientes(self):
        self.fcl.close()     
  
        
#########################CTA BANCARIA#################################################
    def abrir_form_banco(self):
        self.fban=uic.loadUi("gui/formBanco.ui")
        self.fban.setWindowTitle("Registro Cuentas Bancarias")
        self.fban.btnGuardar.clicked.connect(self.registrar_cta_banco)
        self.fban.btnSalir.clicked.connect(self.salir_form_banco)
        self.fban.show()
        
    def registrar_cta_banco(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Cuenta Bancaria")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fban.txtNombreBanco.text()=="":       
            m.setText("Captura nombre del banco")
            self.fban.txtNombreBanco.setFocus()
                
        elif self.fban.txtNumCta.text()=="":
            m.setText(" Captura numero de cta bancaria")
            self.fban.txtNumCta.setFocus()
                        
        elif self.fban.cmbTipoCta.currentIndex()==0:
            m.setText("Seleccona una opcion")
            self.fban.cmbTipoCta.setFocus()
        
        elif self.fban.cmbTipoMoneda.currentIndex()==0:
            m.setText("Capture Clabe")
            self.fban.cmbTipoMoneda.setFocus()
        else:    
            regCta=Cuentas(
                nombre_banco=self.fban.txtNombreBanco.text().upper(),
                num_cta=self.fban.txtNumCta.text(),
                tipo_cta=self.fban.cmbTipoCta.currentText(),
                tipo_moneda=self.fban.cmbTipoMoneda.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegCtasBancoData()
            if  objData.registrar(info=regCta):
                m.setText("Cuenta Bancaria registrada con exito")
                self.limpiar_campos_fban()
            else:
                m.setText("Cuenta Bancaria ya registrada")
                self.limpiar_campos_fban()
        m.exec()
        
    def limpiar_campos_fban(self):
        self.fban.txtNombreBanco.setText("")
        self.fban.txtNumCta.setText("")
        self.fban.cmbTipoCta.setCurrentIndex(0)
        self.fban.cmbTipoMoneda.setCurrentIndex(0) 
                          
    def salir_form_banco(self):
        self.fban.close()
        
 
##################################REGISTRAR CONTRATOS#############################################
    def abrir_form_contratos(self):
        self.fcon=uic.loadUi("gui/formContratos.ui")
        self.fcon.setWindowTitle("Registro Contratos Areas Comunes")
        self.fcon.show()
        self.set_cmb_ac()
        self.set_cmb_clientes_c()
        self.numeros_contratos()
        self.fcon.checkBActivo.setChecked(True)
        self.fcon.cmbAreaComun.currentIndexChanged.connect(self.set_cuota)
        self.fcon.btnGuardar.clicked.connect(self.registrar_contrato)
        self.fcon.btnSalir.clicked.connect(self.salir_form_contratos)
        
    def set_cmb_ac(self):
        obj=ListaAreasData()
        datos=obj.lista_areas_reg_cont()   
        for item in datos:
            self.fcon.cmbAreaComun.addItem(item[1])
       
    def set_cuota(self,area):
        obj=ListaCuotasData()
        datos=obj.lista_cuotas_x_area(self.fcon.cmbAreaComun.currentText())
        self.fcon.txtCuota.setText("")
        for item in datos:
            self.fcon.txtCuota.setText(str(item[3]))
            self.fcon.txtDG.setText(str(item[4]))
            
    def set_cmb_clientes_c(self):
        search=ClientesData()
        data=search.lista_clientes()
        for item in data:
            self.fcon.cmbCliente.addItem(item[1])        
           
    def registrar_contrato(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("contratos areas comunes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        fecha_ini=self.fcon.dateInicial.date().toString("yyyy-MM-dd")
        fecha_fin=self.fcon.dateFinal.date().toString("yyyy-MM-dd")
        area_comun=self.fcon.cmbAreaComun.currentText()
        cliente=self.fcon.cmbCliente.currentText()
        
        if self.fcon.cmbAreaComun.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbAreaComun.setFocus()
        elif self.fcon.cmbCliente.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbCliente.setFocus()
        elif self.fcon.cmbTipoContrato.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbTipoContrato.setFocus()
        elif fecha_ini == fecha_fin:
            m.setText("Fecha inicial igual a la final")
            self.fcon.dateInicial.setFocus()  
        elif fecha_ini > fecha_fin:
            m.setText("Fecha inicial mayor a la final")
            self.fcon.dateInicial.setFocus()            
        else:       
            regContrato=RegContrato(
                n_contrato=self.fcon.txtNumContrato.text(),
                c_facturacion=cliente,
                n_area=area_comun,
                f_inicio=fecha_ini,
                f_fin=fecha_fin,
                m_cuota=self.fcon.txtCuota.text(),
                m_dg=self.fcon.txtDG.text(),
                t_contrato=self.fcon.cmbTipoContrato.currentText(),
                s_contrato=True,
                s_vigencia=self.vigencia(),
                r_usuario=self.pp.lblName_User.text(),
                f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegContratoData()
            if objData.obtener_contrato_x_fechaInio_fechaFinal(fecha_ini,fecha_fin,area_comun):
                m.setText("el area comun:  "  + area_comun +  "   tiene contrato en ese periodo")
                self.limpiar_campos_fcon()
            else:
                if  objData.registrar(info=regContrato):
                    m.setText("Contrato registrado con exito")
                    self.limpiar_campos_fcon()
                else:
                    m.setText("Contrato no registrado")
                    self.limpiar_campos_fcon()
        m.exec()
    
    def vigencia(self):
        fechaFin=self.fcon.dateFinal.date().toString("yyyy-MM-dd")
        if fechaFin < current_datetime.strftime("%Y-%m-%d"):
            return True
        else:
            return False
        
    def numeros_contratos(self):
            objData = RegContratoData()
            last_contract = objData.obtener_ultimo_contrato()                
            if last_contract:
                last_contract_number = str(last_contract[0][0])
                if '-' in last_contract_number:
                    last_number = int(last_contract_number.split('-')[1])
                else:
                    last_number = int(last_contract_number)
                new_number = last_number + 1
                new_contract_number = f"C-{new_number:04d}"  #04d = 0001
                self.fcon.txtNumContrato.setText(new_contract_number)
            else:
                new_contract_number = "C-0001"
                self.fcon.txtNumContrato.setText(new_contract_number)
            
    def limpiar_campos_fcon(self):
        self.fcon.cmbAreaComun.setCurrentIndex(0)
        self.fcon.cmbCliente.setCurrentIndex(0)
        self.fcon.cmbTipoContrato.setCurrentIndex(0)
        self.fcon.txtCuota.setText("")
        self.fcon.txtDG.setText("")  
            
    def salir_form_contratos(self):
        self.fcon.close()        

   
##################################BUSCAR Y EDITAR CONTRATOS#############################################           
    def abrir_form_buscar_contratos(self):
        self.fbc=uic.loadUi("gui/formBcontratos.ui")
        self.fbc.setWindowTitle("Buscar y Editar Contratos Areas Comunes")
        self.fbc.show()
        self.set_lista_contratos()
        self.fbc.cmbContrato.setCurrentIndex(0)
        self.fbc.cmbContrato.currentIndexChanged.connect(self.get_info_contrato)
        self.fbc.btnEditar.clicked.connect(self.guardar_edicion)
        self.fbc.btnSalir.clicked.connect(self.salir_fbc)
        
    def set_lista_contratos(self):
        search=RegContratoData()
        data=search.lista_contratos()
        for item in data:
            self.fbc.cmbContrato.addItem(item[1])   
     
    def get_info_contrato(self,contrato):
        search=RegContratoData()
        data=search.info_contratos(self.fbc.cmbContrato.currentText())
        if data==[]:
                m=QMessageBox()
                m.setWindowTitle("buscar contrato")
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("No hay informacion")
                m.exec()
        else:
            for item in data:
                self.fbc.txtCliente.setText(item[0])
                self.fbc.txtArea.setText(item[1])
                self.fbc.txtfecha_ini.setText(item[2])
                self.fbc.txtfecha_fin.setText(item[3])
                self.fbc.txtCuota.setText(f"{item[4]:.2f}")
                self.fbc.txtDG.setText(f"{item[5]:.2f}")
                self.fbc.checkBActivo.setChecked(item[6].lower()=='true')
                self.fbc.checkBvencido.setChecked(item[7].lower() == 'true')
                             
    def guardar_edicion(self):
        if self.fbc.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Edicion Contratos")
            m.setText("Selecciona una Opcion")
            m.exec()
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Edicion Contratos")
            m.setText("Se editaran los datos del contrato,\ncontinuar...?")
            m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            res=m.exec()
            
            if res == QMessageBox.StandardButton.Ok:
                editContrato=EditContrato(
                    n_contrato=self.fbc.cmbContrato.currentText(),
                    c_facturacion=self.fbc.txtCliente.text(),
                    n_area=self.fbc.txtArea.text(),
                    f_inicio=self.fbc.txtfecha_ini.text(),
                    f_fin=self.fbc.txtfecha_fin.text(),
                    m_cuota=self.fbc.txtCuota.text(),
                    m_dg=self.fbc.txtDG.text(),
                    s_contrato=self.fbc.checkBActivo.isChecked(),
                    s_vigencia=self.fbc.checkBvencido.isChecked(),
                    r_usuario=self.pp.lblName_User.text(),
                    f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=EditContratoData()
                if  objData.editar(info=editContrato):
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Edicion Contratos AC")
                    m.setText("Contrato editado con exito")
                    m.exec()
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Edicion Contratos AC")
                    m=QMessageBox()
                    m.setText("Contrato no editado")
                    m.exec()
                
            elif res == QMessageBox.StandardButton.Cancel:
                m.close()
                
    def salir_fbc(self):
        self.fbc.close()
    
                 
#####################################TABLA DE INFORMACION CUOTAS MANTTO############################################          
    def mostrar_informacionCM(self):
        if self.ppcm.cmblocal.currentIndex()==0 :
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("informacion cartera")
            m.setText("Seleccione una Opcion")
            m.exec()
            self.ppcm.cmblocal.setFocus()
        else:    
            search=CarteraDataCM()
            data=search.buscar_info_ubicacion(self.ppcm.cmblocal.currentText(),self.ppcm.txtCliente.text())
            fila=0
            saldo=0
            if data==[]:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("informacion cartera")
                m.setText("No hay informacion")
                m.exec()
                self.ppcm.cmblocal.setFocus()
            else:
                self.ppcm.tblCarteraCM.setRowCount(len(data))
                for item in data:
                    saldo += float(item[4])
                    self.ppcm.txtSaldo.setText(f"{saldo:,.2f}")
                    
                for item in data:
                    self.ppcm.tblCarteraCM.setItem(fila,0,QTableWidgetItem(item[0]))
                    self.ppcm.tblCarteraCM.setItem(fila,1,QTableWidgetItem(item[1]))
                    self.ppcm.tblCarteraCM.setItem(fila,2,QTableWidgetItem(str(item[2])))
                    self.ppcm.tblCarteraCM.setItem(fila,3,QTableWidgetItem(str(item[3])))
                    self.ppcm.tblCarteraCM.setItem(fila,4,QTableWidgetItem(str(item[4])))
                    self.ppcm.tblCarteraCM.setItem(fila,5,QTableWidgetItem(item[5]))
                    self.ppcm.tblCarteraCM.setItem(fila,6,QTableWidgetItem(item[6]))
                    self.ppcm.tblCarteraCM.setItem(fila,7,QTableWidgetItem(item[9]))
                    self.ppcm.tblCarteraCM.setItem(fila,8,QTableWidgetItem(item[7]))
                    self.ppcm.tblCarteraCM.setItem(fila,9,QTableWidgetItem(item[8]))
                    fila+=1
                    
    def exportar_info_a_excelCM(self):
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("exportar informacion")
            m.setText("Seleccione una Opcion")
            m.exec()
        else:    
            if self.ppcm.tblCarteraCM.rowCount() > 0:
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self.pp, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                                
                if file_path:
                    try:                            
                        workbook = xlsxwriter.Workbook(file_path)
                        worksheet = workbook.add_worksheet()
                                        
                        headers = ["tipo_cuota", "num_fact", "importe_adeudo", "importe_pago", "importe_saldo", "fecha", "forma_pago", "num_cheque", "cta_banco","status"]
                        for col_num, header in enumerate(headers):
                            worksheet.write(0, col_num, header)           
                            for row_num in range(self.ppcm.tblCarteraCM.rowCount()):
                                for col_num in range(self.ppcm.tblCarteraCM.columnCount()):
                                    worksheet.write(row_num + 1, col_num, self.ppcm.tblCarteraCM.item(row_num, col_num).text())
                                        
                        workbook.close()               
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Information)
                        m.setWindowTitle("Exportar a Excel")
                        m.setText("Datos exportados exitosamente a Excel")
                        m.exec()
                    except Exception as e:
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Critical)
                        m.setWindowTitle("Error")
                        m.setText(f"Error al exportar a Excel: {e}")
                        m.exec()
            elif self.ppcm.tblCarteraCM.rowCount() < 0:
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Warning)
                m.setWindowTitle("Exportar a Excel")
                m.setText("No hay datos para exportar")
                m.exec()
                
##############################TABLA DE INFORMACION AREAS COMUNES############################################        
    def mostrar_informacionAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("informacion cartera")
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppac.cmbContrato.setFocus()
        else:    
            search=CarteraDataAC()
            data=search.buscar_info_area_x_contrato(self.ppac.cmbContrato.currentText())
            fila=0
            saldo=0
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("informacion cartera")
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("No hay informacion")
                m.exec()
                self.ppac.tblCarteraAC.clearContents()
                self.ppac.cmbContrato.setFocus()
            else:
                self.ppac.tblCarteraAC.setRowCount(len(data))
                for item in data:
                    saldo += float(item[5])
                    self.ppac.txtSaldo.setText(f"{saldo:,.2f}")
                    
                for item in data:
                     self.ppac.tblCarteraAC.setItem(fila,0,QTableWidgetItem(item[0]))
                     self.ppac.tblCarteraAC.setItem(fila,1,QTableWidgetItem(item[1]))
                     self.ppac.tblCarteraAC.setItem(fila,2,QTableWidgetItem(item[2]))
                     self.ppac.tblCarteraAC.setItem(fila,3,QTableWidgetItem(str(item[3])))
                     self.ppac.tblCarteraAC.setItem(fila,4,QTableWidgetItem(str(item[4])))
                     self.ppac.tblCarteraAC.setItem(fila,5,QTableWidgetItem(str(item[5])))
                     self.ppac.tblCarteraAC.setItem(fila,6,QTableWidgetItem(item[6]))
                     self.ppac.tblCarteraAC.setItem(fila,7,QTableWidgetItem(item[8]))
                     self.ppac.tblCarteraAC.setItem(fila,8,QTableWidgetItem(item[7]))
                     self.ppac.tblCarteraAC.setItem(fila,9,QTableWidgetItem(item[9]))   
                     fila+=1

    def exportar_info_a_excelAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("exportar informacion")
            m.setText("Seleccione una Opcion")
            m.exec()
        else:    
            if self.ppac.tblCarteraAC.rowCount() > 0:    
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self.pp, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                                
                if file_path:
                    try:                            
                        workbook = xlsxwriter.Workbook(file_path)
                        worksheet = workbook.add_worksheet()
                                        
                        headers = ["contrato", "tipo_cuota","num_fact", "importe_adeudo", "importe_pago", "importe_saldo", "fecha", "forma_pago", "cta_banco","status"]
                        for col_num, header in enumerate(headers):
                            worksheet.write(0, col_num, header)           
                            for row_num in range(self.ppac.tblCarteraAC.rowCount()):
                                for col_num in range(self.ppac.tblCarteraAC.columnCount()):
                                    worksheet.write(row_num + 1, col_num, self.ppac.tblCarteraAC.item(row_num, col_num).text())                
                        workbook.close()               
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Information)
                        m.setWindowTitle("Exportar a Excel")
                        m.setText("Datos exportados exitosamente a Excel")
                        m.exec()
                    except Exception as e:
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Critical)
                        m.setWindowTitle("Error")
                        m.setText(f"Error al exportar a Excel: {e}")
                        m.exec()
                else: pass        
            elif self.ppac.tblCarteraAC.rowCount() < 0:    
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Warning)
                m.setWindowTitle("Exportar a Excel")
                m.setText("No hay datos para exportar")
                m.exec()
                        
                
########################################CARGA MASIVA DE CUOTAS###########################################################
    def abrir_form_cmasiva(self):
        self.ffm=uic.loadUi("gui/formFactMasiva.ui")
        self.ffm.setWindowTitle("Carga Mensual Facturas Cuotas")
        self.ffm.show()
        self.ffm.cmbTcartera.setCurrentIndex(0)
        self.ffm.btnEjecutar.clicked.connect(self.seleccion_tipo_cartera)
        self.ffm.btnSalir.clicked.connect(self.salir_form_cmasiva)
    
    def seleccion_tipo_cartera(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga Mensual")
        if self.ffm.cmbTcartera.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ffm.cmbTcartera.setFocus()
        elif self.ffm.fechaPeriodo.date().toString("yyyy-MM") < current_datetime.strftime("%Y-%m"):
            m.setText("Periodo menor al actual")
            m.exec()
            self.ffm.fechaPeriodo.setFocus()
        else:
            if self.ffm.cmbTcartera.currentIndex()==1 :
                self.registro_masivo_cuotas_locales()
                m.close()     
            elif self.ffm.cmbTcartera.currentIndex()==2 :
                self.registro_masivo_cuotas_areas()
                m.close()    
            else:
                m.setText("Selecciona una Opcion")
                m.exec()
                self.ffm.cmbTcartera.setFocus()
               
    def registro_masivo_cuotas_locales(self):
        m=QMessageBox()  
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Carga Cuotas Locales.")
        m.setText("¿¿Se generaran las cuotas?? \ncontinuar....")
        m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res=m.exec()
            
        if res==QMessageBox.StandardButton.Ok:
            search=UbicacionesData()
            data=search.lista_ubicaciones()     
            p=self.ffm.fechaPeriodo.date().toString("MMyy")
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("Carga Mensual")  
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("sin informacion bd")
                m.exec()
            else:
                reg_Periodo=RegPeriodoFacturacion(
                    periodo=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                    tipoCartera=self.ffm.cmbTcartera.currentText(),
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=PeriodosCargaData()
                if objData._registrar_p(info=reg_Periodo):
                    for item in data:
                        reg_facturas=Reg_Factura(
                            num_factura=f"F-{p}",
                            cliente=item[7],
                            local_o_area=item[1],
                            fecha_factura=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            tipo_cuota="cuota ordinaria",
                            importe_factura=item[3],
                            tipo_factura="Ingreso",
                            tipo_cartera="locales comerciales",
                            status_pago=False,
                            usuario=self.pp.lblName_User.text(),
                            fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData=RegFacturaData()
                        objData._registrar(info=reg_facturas)
                        
                        reg_cartera=Reg_Cartera(
                            local_o_area=item[1],
                            clienteFact=item[7],
                            tipoCartera="locales comerciales",
                            tipoCuota="cuota ordinaria",
                            tipo_factura="Ingreso",
                            numFact=f"F-{p}",
                            importeAdeudo=item[3],
                            importePago=0,
                            fPago_Cobro=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            ctaBanco="",
                            formaPago="",
                            cheque="",
                            numContrato="",
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios="carga mensual " + self.ffm.fechaPeriodo.date().toString("yyyy-MM")         
                            )
                        objData=RegCarteraData()
                        objData._registrar(info=reg_cartera)
                         
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("carga mensual de cuotas exitosa") 
                    m.exec()
                           
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("Periodo ya registrado")
                    m.exec()    
                                        
        elif res==QMessageBox.StandardButton.Cancel:
            m.close()
                                   
    def registro_masivo_cuotas_areas(self):
        m=QMessageBox()  
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Carga Cuotas Areas C.")
        m.setText("¿¿Se generaran las facturas \npor cuotas areas comunes?? continuar....")
        m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res=m.exec()
            
        if res==QMessageBox.StandardButton.Ok:
            search=ContratosData()
            data=search.lista_contratos()
            p=self.ffm.fechaPeriodo.date().toString("MMyy")
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("Carga Mensual.")  
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("sin informacion bd")
                m.exec()
            else:
                reg_Periodo=RegPeriodoFacturacion(
                    periodo=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                    tipoCartera=self.ffm.cmbTcartera.currentText(),
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=PeriodosCargaData()
                if objData._registrar_p(info=reg_Periodo): 
                    for item in data:
                        reg_facturas=Reg_Factura(
                            num_factura=f"F-{p}",
                            cliente=item[2],
                            local_o_area=item[3],
                            fecha_factura=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            tipo_cuota="cuota ordinaria",
                            importe_factura=item[6],
                            tipo_factura="Ingreso",
                            tipo_cartera="areas comunes",
                            status_pago=False,
                            usuario=self.pp.lblName_User.text(),
                            fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData=RegFacturaData()
                        objData._registrar(info=reg_facturas)
                        
                        reg_cartera=Reg_Cartera(
                            local_o_area=item[3],
                            clienteFact=item[2],
                            tipoCartera="areas comunes",
                            tipoCuota="cuota ordinaria",
                            tipo_factura="Ingreso",
                            numFact=f"F-{p}",
                            importeAdeudo=item[6],
                            importePago=0,
                            fPago_Cobro=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            ctaBanco="",
                            formaPago="",
                            cheque="",
                            numContrato=item[1],  
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios="Facturacion masiva " + self.ffm.fechaPeriodo.date().toString("yyyy-MM")         
                            )
                        objData=RegCarteraData()
                        objData._registrar(info=reg_cartera)
                        
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("carga mensual de cuotas exitosa") 
                    m.exec()     
                          
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("Periodo ya registrado")
                    m.exec()

        elif res==QMessageBox.StandardButton.Cancel:
            m.close()
              
    def salir_form_cmasiva(self):
        self.ffm.close() 
        
        
###################################################MODULO GASTOS#####################################################################
    def abrir_form_gastos(self):
        self.fexp=uic.loadUi("gui/formRegGastos.ui")
        self.fexp.setWindowTitle("Registro Gastos Mensuales")
        self.fexp.show()
        self.set_cmb_proveedor()
        self.fexp.btnRegistrar.clicked.connect(self.registrar_gasto)
        self.fexp.btnSalir.clicked.connect(self.salir_form_gastos)
        
    def set_cmb_proveedor(self):
        search=ProveedoresData()
        data=search.lista_proveedores()
        for item in data:
            self.fexp.cmbProveedor.addItem(item[1])    

    def registrar_gasto(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro de Gasto")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.fexp.cmbProveedor.currentIndex() == 0:
            m.setText("Selecciona un proveedor")
            self.fexp.cmbProveedor.setFocus()
        elif self.fexp.txtImporte.text() == "":
            m.setText("Captura el importe del gasto")
            self.fexp.txtImporte.setFocus()
        elif not self.fexp.txtImporte.text().replace('.', '', 1).isnumeric():
            m.setText("Captura solo números en el importe")
            self.fexp.txtImporte.setText("")
            self.fexp.txtImporte.setFocus()
        elif self.fexp.txtDescripcion.toPlainText() == "":
            m.setText("Captura el concepto del gasto")
            self.fexp.txtDescripcion.setFocus()
        elif self.fexp.cmbFormaPago.currentIndex() == 0:
            m.setText("Selecciona una forma de pago")
            self.fexp.cmbFormaPago.setFocus()
        elif self.fexp.cmbTipoGasto.currentIndex() == 0:
            m.setText("Selecciona un tipo de gasto")
            self.fexp.cmbTipoGasto.setFocus()
        elif self.fexp.txtnFactura.text() == "":
            m.setText("Captura el número de factura")
            self.fexp.txtnFactura.setFocus()        
        else:
            regGasto = Reg_Gasto(
                num_fact=self.fexp.txtnFactura.text().upper(),
                n_proveedor=self.fexp.cmbProveedor.currentText(),
                t_gasto=self.fexp.cmbTipoGasto.currentText(),
                desc_gasto=self.fexp.txtDescripcion.toPlainText(),
                f_pago=self.fexp.cmbFormaPago.currentText(),
                n_cheque=self.fexp.txtn_cheque.text().upper(),
                i_pago=float(self.fexp.txtImporte.text()),
                iva_ret=float(self.fexp.txtIVA_ret.text()),
                isr_ret=float(self.fexp.txtISR_ret.text()),
                f_gasto=self.fexp.boxDate.date().toString("yyyy-MM-dd"),
                usuario=self.pp.lblName_User.text(),
                f_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData = RegGastoData()
            if objData._registrar(info=regGasto):
                m.setText("Gasto registrado con éxito")
                self.limpiar_campos_fexp()
            else:
                m.setText("Error al registrar el gasto")
                self.limpiar_campos_fexp()
        m.exec()

    def limpiar_campos_fexp(self):
        self.fexp.cmbProveedor.setCurrentIndex(0)
        self.fexp.txtnFactura.setText("")
        self.fexp.cmbTipoGasto.setCurrentIndex(0)
        self.fexp.txtDescripcion.setText("")
        self.fexp.cmbFormaPago.setCurrentIndex(0)
        self.fexp.txtn_cheque.setText("")
        self.fexp.txtImporte.setText("")
        self.fexp.txtIVA_ret.setText("")
        self.fexp.txtISR_ret.setText("")
    
    def salir_form_gastos(self):
        self.fexp.close()

    def abrir_form_alta_proveedor(self):
        self.fprov=uic.loadUi("gui/formRegProveedor.ui")
        self.fprov.setWindowTitle("Registro de Proveedor")
        self.fprov.show()
        self.fprov.btnRegistrar.clicked.connect(self.registrar_proveedor)
        self.fprov.btnSalir.clicked.connect(self.salir_form_proveedores)
        
    def registrar_proveedor(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Proveedor")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.fprov.txtRazon_social.text() == "":
            m.setText("Captura nombre del proveedor")
            self.fprov.txtRazon_social.setFocus()
        elif self.fprov.txtRFC.text() == "":
            m.setText("Captura RFC del proveedor")
            self.fprov.txtRFC.setFocus()
        elif self.fprov.txtTipoServicio.text() == "":
            m.setText("Captura  tipo de servicio")
            self.fprov.txtTipoServicio.setFocus()
        elif self.fprov.txtBanco.text()=="":
            m.setText("Captura banco")
            self.fprov.txtBanco.setFocus()            
        elif self.fprov.txtDireccion.text() == "":
            m.setText("Captura dirección del proveedor")
            self.fprov.txtDireccion.setFocus()
        elif self.fprov.txtTelefono.text() == "":
            m.setText("Captura teléfono del proveedor")
            self.fprov.txtTelefono.setFocus()
        elif not self.fprov.txtTelefono.text().isnumeric():
            m.setText("Captura solo números en el teléfono")
            self.fprov.txtTelefono.setText("")
            self.fprov.txtTelefono.setFocus()
        elif self.fprov.txtEmail.text() == "":
            m.setText("Captura email del proveedor")
            self.fprov.txtEmail.setFocus()
        else:
            regProveedor = RegProveedor(
                nombre=self.fprov.txtRazon_social.text().upper(),
                rfc=self.fprov.txtRFC.text().upper(),
                nComercial=self.fprov.txtNombre_comercial.text().upper(),
                curp=self.fprov.txtCURP.text().upper(),
                tipoServicio=self.fprov.txtTipoServicio.text(),
                cuentaBanco=self.fprov.txtBanco.text().upper(),
                direccion=self.fprov.txtDireccion.text(),
                telefono=self.fprov.txtTelefono.text(),
                email=self.fprov.txtEmail.text().lower(),
                usuario=self.pp.lblName_User.text(),
                fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            )
            objData = ProveedoresData()
            if objData.registrar_proveedor(regProveedor):
                m.setText("Proveedor registrado con éxito")
                self.limpiar_campos_fprov()
            else:
                m.setText("Proveedor ya registrado")
                self.limpiar_campos_fprov()
        m.exec()

    def limpiar_campos_fprov(self):
        self.fprov.txtRazon_social.setText("")
        self.fprov.txtRFC.setText("")
        self.fprov.txtNombre_comercial.setText("")
        self.fprov.txtCURP.setText("")
        self.fprov.txtDireccion.setText("")
        self.fprov.txtTelefono.setText("")
        self.fprov.txtEmail.setText("")
        self.fprov.txtTipoServicio.setText("")
        self.fprov.txtBanco.setText("")
    
    def salir_form_proveedores(self):
        self.fprov.close()       

    def abrir_form_alta_empleado(self):
        self.femp=uic.loadUi("gui/formEmpleados.ui")
        self.femp.setWindowTitle("Registro Empleados")
        self.femp.show()
        self.femp.btnGuardar.clicked.connect(self.registrar_empleado)
        self.femp.btnSalir.clicked.connect(self.salir_form_empleados)
        
    ##pendiente programar form empleados y sus metodos
    def registrar_empleado(self):   
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Empleado")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.femp.txtNombreCliente.text() == "":
            m.setText("Captura nombre del empleado")
            self.femp.txtNombreCliente.setFocus()
        elif self.femp.txtRFC.text() == "":
            m.setText("Captura RFC del empleado")
            self.femp.txtRFC.setFocus()
        elif self.femp.txtCURP.text() == "":
            m.setText("Captura CURP del empleado")
            self.femp.txtCURP.setFocus()
        elif self.femp.txtDireccion.text() == "":
            m.setText("Captura dirección del empleado")
            self.femp.txtDireccion.setFocus()
        elif self.femp.txtCel.text() == "":
            m.setText("Captura teléfono del empleado")
            self.femp.txtCel.setFocus()
        elif not self.femp.txtCel.text().isnumeric():
            m.setText("Captura solo números en el teléfono")
            self.femp.txtCel.setText("")
            self.femp.txtCel.setFocus()
        elif self.femp.txtEmail.text() == "":
            m.setText("Captura email del empleado")
            self.femp.txtEmail.setFocus()
        else:
            regEmpleado = RegEmpleado(
                nombre=self.femp.txtNombreCliente.text().upper(),
                rfc=self.femp.txtRFC.text().upper(),
                curp=self.femp.txtCURP.text().upper(),
                direccion=self.femp.txtDireccion.text(),
                telefono=self.femp.txtCel.text(),
                email=self.femp.txtEmail.text().lower(),
                usuario=self.pp.lblName_User.text(),
                fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            )
            objData = RegEmpleadoData()
            if objData.registrar(regEmpleado):
                m.setText("Empleado registrado con éxito")
                self.limpiar_campos_femp()
            else:
                m.setText("Empleado ya registrado")
                self.limpiar_campos_femp()
        m.exec()

    def limpiar_campos_femp(self):
        self.femp.txtNombreCliente.setText("")
        self.femp.txtRFC.setText("")
        self.femp.txtCURP.setText("")
        self.femp.txtDireccion.setText("")
        self.femp.txtCel.setText("")
        self.femp.txtEmail.setText("")
    
    def salir_form_empleados(self):
        self.femp.close()
    

    def reiniciar_sistema(self):
        self.pp.close()
        os.system("python main.py")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaPrincipal()
    sys.exit(app.exec())    
    
    


    





