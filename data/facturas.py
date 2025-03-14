import conexion_db as con


class FacturasData():       
    def lista_facturas(self,ubicacion,cliente):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute(
            """SELECT * FROM cartera  WHERE area_o_local='{}' AND cliente_facturacion='{}' """.format(ubicacion,cliente))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                