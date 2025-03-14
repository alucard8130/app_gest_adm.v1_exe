import conexion_db as con
from model.regareac import RegAC


class RegACData():
    def registrar(self, info=RegAC):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query =self.cursor.execute( "SELECT * FROM areas_comunes WHERE UPPER(num_area) = '{}'".format(info._nArea))
        result = query.fetchone()
        if result is None:    
            self.db = con.Conexion().conectarBd()
            self.cursor= self.db.cursor()
            query= self.cursor.execute("""INSERT INTO areas_comunes values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(info._nArea,info._cFacturacion,info._iCuota,info._iDg,info._tArea,info._iCantidad,info._superficie,info._giro,info._nContrato,info._status,info._fReg,info._usuario))
            self.db.commit()
            self.cursor.close()
            self.db.close()
            return True   
        else:
            return False

    
                