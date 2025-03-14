
import conexion_db as con


class CarteraDataCM():
    def buscar_info_ubicacion(self,ubicacion,cliente):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cuota,num_fact,imp_adeudo,imp_pago,saldo_adeudo,f_cobro_o_pago,forma_pago,cta_banco,status_pago,num_cheque FROM cartera
        WHERE area_o_local='{}' AND cliente_facturacion='{}'
        """.format(ubicacion,cliente)
        )
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
        


class CarteraDataAC():
    def buscar_info_area_x_contrato(self,contrato):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT num_contrato,tipo_cuota,num_fact,imp_adeudo,imp_pago,saldo_adeudo,f_cobro_o_pago,forma_pago,cta_banco,status_pago FROM cartera
        WHERE num_contrato='{}'""".format(contrato)
        )
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                
                