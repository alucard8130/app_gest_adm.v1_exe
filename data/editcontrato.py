import conexion_db as con
from model.editcontrato import EditContrato



class EditContratoData():
    def editar(self, info:EditContrato):
        self.bd = con.Conexion().conectarBd()
        self.cursor = self.bd.cursor()
        query=(
        """UPDATE contratos SET cliente = '{}', area_comun = '{}', fecha_inicio = '{}', fecha_fin = '{}', cuota_mensual = '{}', deposito_garantia = '{}',
            status_activo = '{}', status_vencido = '{}', usuario = '{}', fecha_reg = '{}' WHERE num_contrato = '{}'"""
            .format(info._clienteFact, info._area, info._fechaInicio, info._fechaFin, info._cuota, info._deposito, info._statusContrato, info._statusVigencia, info._usuarioReg, info._fechaReg, info._numContrato)
        )
        self.cursor.execute(query)
        self.bd.commit()
        self.cursor.close()
        self.bd.close()
        return True
    
            
        
   