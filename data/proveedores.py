import conexion_db as con
from model.regProveedor import RegProveedor


class ProveedoresData():       
    def lista_proveedores(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM proveedores order by nombre_razon")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    

    def registrar_proveedor(self,info=RegProveedor):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM proveedores WHERE rfc = '{}' OR nombre_razon = '{}'".format(info._rfc, info._nombre))
        if self.cursor.fetchone()[0] > 0:
            return False
        self.cursor.execute("INSERT INTO proveedores VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
        .format(info._nombre, info._rfc, info._nComercial, info._curp, info._tipoServicio, info._cuentaBanco, info._direccion, info._telefono, info._email, info._usuario, info._fechaReg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False