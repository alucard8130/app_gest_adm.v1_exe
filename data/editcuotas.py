import conexion_db as con
from model.editcuotas import EditCuotasLocales


class UpdateCuotasData():
    def editar(self, info:EditCuotasLocales):
        self.bd = con.Conexion().conectarBd()
        self.cursor = self.bd.cursor()
        query=(
        """UPDATE ubicaciones SET cuota_mensual = '{}', usuario = '{}', fecha_reg = '{}' WHERE num_local = '{}'"""
            .format(info._cuota, info._usuario, info._fecha_reg, info._num_local))
        self.cursor.execute(query)
        self.bd.commit()
        self.cursor.close()
        self.bd.close()
        return True
    
            
        
   