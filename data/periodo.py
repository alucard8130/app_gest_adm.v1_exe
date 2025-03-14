
import conexion_db as con
from model.regperiodofacturacion import RegPeriodoFacturacion


class PeriodosCargaData():
    def _registrar_p(self,info=RegPeriodoFacturacion):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""SELECT COUNT(*) FROM reg_carga_cuotas WHERE tipo_cartera = '{}' AND periodo = '{}'""".format(info._tipoCartera,info._periodo,))
        if self.cursor.fetchone()[0] > 0:
            return False
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO reg_carga_cuotas values(null,'{}','{}','{}','{}')""".format(info._tipoCartera,info._periodo,info._usuario,info._fechaReg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
        

        
        

                