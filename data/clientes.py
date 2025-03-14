import conexion_db as con


class ClientesData():
    #lista de clientes        
    def lista_clientes(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM clientes order by nombre_o_razon_social")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    
class BuscarCliente():
    def buscar_cliente(self, local):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM ubicaciones WHERE num_local = '{}'".format(local))
        serch_info=query.fetchall()
        self.db.close()
        return (serch_info)              
    
     