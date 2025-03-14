
import conexion_db as con
from model.regempleado import RegEmpleado


class RegEmpleadoData():
    def registrar(self, info=RegEmpleado):
        self.db = con.Conexion().conectarBd()
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM empleados WHERE rfc = '{}'".format(info._rfc))
        if self.cursor.fetchone()[0] > 0:
            return False
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO empleados values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nombre, info._apellido_paterno, info._apellido_materno, info._rfc, info._curp, info._nns, info._f_nacimiento, info._puesto, info._departamento, 
                   info._sueldo, info._direccion, info._telefono, info._email, info._f_ingreso, info._f_baja, info._fechareg, info._status, info._usuario, info._f_reg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
            
        
        
                