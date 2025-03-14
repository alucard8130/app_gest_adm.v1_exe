import conexion_db as con


class ContratosData():
    def lista_contratos(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM contratos order by num_contrato")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
        

                