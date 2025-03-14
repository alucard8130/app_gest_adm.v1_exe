from model.regcliente import RegCliente
import conexion_db as con


class RegClienteData():
    def registrar(self, info=RegCliente):
        self.db = con.Conexion().conectarBd()
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM clientes WHERE rfc = '{}' OR nombre_o_razon_social = '{}'".format(info._rfc, info._nombre))
        if self.cursor.fetchone()[0] > 0:
            return False
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO clientes values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nombre, info._rfc, info._tipoC, info._curp, info._num_a_o_l, info._tipoCl, info._giro, info._direccion, info._numcel, info._email, info._fReg, info._status, info._usuario))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
            
        
        
                