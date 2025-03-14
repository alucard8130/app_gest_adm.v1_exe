import conexion_db as con
from model.reglocal import RegLocal


class RegLocalData():
    def registrar(self, info=RegLocal):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query =self.cursor.execute( "SELECT * FROM ubicaciones WHERE UPPER(num_local) = '{}'".format(info._numLocal))
        result = query.fetchone()
        if result is None:    
            self.db = con.Conexion().conectarBd()
            self.cursor= self.db.cursor()
            query= self.cursor.execute("""INSERT INTO ubicaciones values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(info._numLocal, info._sup, info._cuota, info._dg, info._nomPropietario, info._rfcPropietario, info._cliente, info._giro, info._status, info._usuario, info._fReg))
            self.db.commit()
            self.cursor.close()
            self.db.close()
            return True
   
        else:
            return False
            

            
        
                