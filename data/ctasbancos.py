
import conexion_db as con


        
class CuentasData():
    def lista_ctas(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM ctas_banco order by num_cta")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                