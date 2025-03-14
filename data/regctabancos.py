import conexion_db as con
from model.ctasbancos import Cuentas


class RegCtasBancoData():
    def registrar(self, info=Cuentas):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query =self.cursor.execute( "SELECT * FROM ctas_banco WHERE UPPER(num_cta) = '{}'".format(info._cta))
        result = query.fetchone()
        if result is None:    
            self.db = con.Conexion().conectarBd()
            self.cursor= self.db.cursor()
            query= self.cursor.execute("""INSERT INTO ctas_banco values(null,'{}','{}','{}','{}','{}','{}')
            """.format(info._name,info._cta,info._tipo,info._moneda,info._user,info._fReg))
            self.db.commit()
            self.cursor.close()
            self.db.close()
            return True
        else:
            return False
            

            
        
                