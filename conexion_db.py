import datetime
import sqlite3

current_datetime = datetime.datetime.now()        

class Conexion():
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("gac.db")
            self.create_tables()
        except sqlite3.Error as e:
            print(e)

    def create_tables(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT ,
                usuario TEXT,
                clave TEXT ,
                status BOOLEAN,
                fecha_reg TEXT,
                usuario_reg TEXT);
            """
            self.conexion.execute(query)
            self.conexion.commit()
        
            self.crear_super_user()
            self.create_table_cartera()
            self.create_table_clientes()
            self.create_table_ac()
            self.create_table_lc()
            self.create_table_facturas()
            self.create_table_contratos()
            self.create_table_cobranza()
            self.create_table_ctas_bancarias()
            self.create_table_reg_carga_cuotas()
            self.create_table_gastos()
            self.create_table_proveedores() 
            self.create_table_empleados()
            #self.create_table_otros_ingresos()
            
            
            
        except sqlite3.Error as e:
            print(e)
            

    def crear_super_user(self):
            try:
                query = "SELECT * FROM usuarios WHERE usuario = 'administrador'"
                cursor = self.conexion.cursor()
                cursor.execute(query)
                result = cursor.fetchone()
                if result is None:
                    query = """
                    INSERT INTO usuarios (nombre, usuario, clave, status, fecha_reg) 
                    VALUES (?, ?, ?, ?, ?)
                    """
                    cursor.execute(query, ('Super User', 'administrador', 'adMin_81@', "True", current_datetime))
                    self.conexion.commit()
                else:
                    pass
            except sqlite3.Error as e:
                print(e)
                              

    def create_table_cartera(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS cartera(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area_o_local TEXT , 
            cliente_facturacion TEXT,
            tipo_cartera TEXT ,
            tipo_cuota TEXT ,
            tipo_factura TEXT ,
            num_fact TEXT,
            imp_adeudo FLOAT,
            imp_pago FLOAT,
            saldo_adeudo as (imp_adeudo - imp_pago) VIRTUAL,
            f_cobro_o_pago TEXT ,
            cta_banco TEXT,
            forma_pago TEXT ,
            num_cheque TEXT,
            num_contrato TEXT,
            status_pago TEXT,
            usuario_reg TEXT ,
            fecha_reg TEXT,
            comentarios TEXT);
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
    

    def create_table_clientes(self):
        #status = activo, inactivo
        try:
            query = """
            CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_o_razon_social TEXT,
            rfc TEXT,
            tipo_contribuyente TEXT,
            curp TEXT,
            area_o_local TEXT,
            tipo_cliente TEXT,
            giro TEXT,
            direccion TEXT ,
            telefono TEXT ,
            email TEXT ,
            fecha_reg TEXT ,
            status TEXT ,
            usuario TEXT); """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
     

    def create_table_ac(self):
        #tipo area =#estacionamiento, baño, area, isla, modulo, stand,cajon,otros
        #status_ocupacion = ocupado, disponible
        try:
            query = """
            CREATE TABLE IF NOT EXISTS areas_comunes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_area TEXT,
            cliente_fact TEXT,
            cuota_mensual FLOAT,
            deposito_garantia FLOAT,
            tipo_area TEXT, 
            cantidad TEXT,
            superficie FLOAT,
            giro TEXT,
            num_contrato TEXT,
            status_disponible TEXT, 
            fecha_reg TEXT,
            usuario TEXT);"""
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e) 
    

    def create_table_lc(self):
        #num_local = no aceptar repetidos
        #status_ocupacion = false,true
        try:
            query = """
            CREATE TABLE IF NOT EXISTS ubicaciones(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_local TEXT  ,    
            superficie FLOAT ,
            cuota_mensual FLOAT  ,
            deposito_garantia  FLOAT,
            propietario TEXT ,
            rfc_propietario TEXT ,
            cliente_fact TEXT,
            giro TEXT,
            status_disponible TEXT ,
            usuario TEXT ,
            fecha_reg TEXT );
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)  
     
    def create_table_facturas(self):
        #tipo_cuota = cuota area comun, cuota mantto, cuota extraordinaria mantto, cuota deposito garantia,cuota recuperacion servicio,otra
        #tipo_factura = ingreso, egreso(nota credito)
        #tipo_cartera = locales comerciales, areas comunes, recuperacion, extraordinarias,otras
        #status_pagada = false,true
        #num_fact = no aceptar repetidos
        try:
            query = """
            CREATE TABLE IF NOT EXISTS facturas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_fact TEXT ,
            cliente TEXT ,
            area_o_local TEXT ,
            fecha_fact TEXT ,
            dias_vencimiento AS (julianday(fecha_reg) - julianday(fecha_fact)) VIRTUAL,
            tipo_cuota TEXT , 
            imp_factura FLOAT ,
            tipo_factura TEXT , 
            tipo_cartera TEXT ,
            status_pagada TEXT ,  
            usuario TEXT ,
            fecha_reg TEXT );
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
    
    def create_table_cobranza(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS cobranza(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_fact TEXT,
            fecha_pago TEXT ,
            imp_pago FLOAT ,
            forma_pago TEXT ,
            cta_banco TEXT,
            num_cheque TEXT,
            tipo_cuota TEXT ,
            usuario TEXT ,
            fecha_reg TEXT ,
            comentarios TEXT);
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
            
    def create_table_contratos(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS contratos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_contrato TEXT,
            cliente TEXT ,
            area_comun TEXT ,
            fecha_inicio TEXT ,
            fecha_fin TEXT ,
            cuota_mensual FLOAT ,
            deposito_garantia FLOAT,
            tipo_contrato TEXT ,
            status_activo TEXT , 
            status_vencido TEXT ,
            usuario TEXT ,
            fecha_reg TEXT );
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
 
    def create_table_ctas_bancarias(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS ctas_banco(
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            nombre_banco TEXT  ,    
            num_cta TEXT ,
            tipo_cta TEXT ,
            tipo_moneda TEXT,
            usuario TEXT ,
            fecha_reg TEXT );
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)  
        
    def create_table_reg_carga_cuotas(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS reg_carga_cuotas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_cartera TEXT,
            periodo TEXT ,
            usuario TEXT ,
            fecha_reg TEXT );
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)    
    
    def create_table_gastos(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS gastos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_factura TEXT,
            proveedor_name TEXT,
            tipo_gasto TEXT,
            descripcion_gasto TEXT,
            forma_pago TEXT,
            num_cheque TEXT,
            importe_pago FLOAT,
            subtotal as (importe_pago / 1.16) VIRTUAL,
            iva as (subtotal * 0.16) VIRTUAL,
            iva_ret FLOAT,
            isr_ret FLOAT,
            fecha_gasto TEXT,
            usuario TEXT,
            fecha_reg TEXT);
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)    
    
    def create_table_proveedores(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS proveedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_razon TEXT,
            rfc TEXT,
            nombre_comercial TEXT,
            curp TEXT,
            tipo_servicio TEXT,
            cuenta_banco TEXT,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            usuario TEXT,
            fecha_reg TEXT);
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
    
    def create_table_empleados(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS empleados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido_paterno TEXT,
            apellido_materno TEXT,
            rfc TEXT,
            curp TEXT,
            NSS TEXT,
            fecha_nacimiento TEXT,
            puesto TEXT,
            departamento TEXT,
            sueldo_diario FLOAT,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_ingreso TEXT,
            fecha_baja TEXT,
            antiguedad as (julianday('now') - julianday(fecha_ingreso)) VIRTUAL,
            status_activo BOOLEAN,
            usuario TEXT,
            fecha_reg TEXT);
            """
            self.conexion.execute(query)
        except sqlite3.Error as e:
            print(e)
                     
    #funcion que crea una conexion a la base de datos        
    def conectarBd(self):
       return self.conexion                    
            
conexion=Conexion()  
conexion.conexion.close()