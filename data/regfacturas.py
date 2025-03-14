from model.operaciones import Reg_Cartera, Reg_Factura
import conexion_db as con
from model.regperiodofacturacion import RegPeriodoFacturacion


class RegCarteraData():
    def _registrar(self, info=Reg_Cartera):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO cartera values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nl_o_a,info._cliente,info._tCartera,info._tCuota,info._tFactura,info._nFact,info._iAdeudo,info._iPago,info._iSaldo,info._feP_C,info._cta,
                   info._foPago,info._cheque,info._nContrato,info._sPago,info._usuario,info._feReg,info._comm))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
            
        
class RegFacturaData():
    def _registrar(self, info=Reg_Factura):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO facturas values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._num_factura,info._cliente,info._nl_o_a,info._fecha_factura,info._tipo_cuota,info._importe_factura,info._tipo_factura,info._tipo_cartera,
                   info._status_pago,info._usuario,info._fecha_reg))
        self.db.commit()        
        if self.cursor.rowcount==1:
            return True
        else:
            return False
        
class RegPeriodoFactData():
    def _registrar_p(self,info=RegPeriodoFacturacion):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO reg_carga_cuotas values(null,'{}','{}','{}','{}')
        """.format(info._tipoCartera,info._periodo,info._usuario,info._fechaReg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False