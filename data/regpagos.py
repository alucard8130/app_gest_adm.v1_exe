from model.operaciones import Reg_Cartera, Reg_Cobranza
import conexion_db as con


class RegCarteraData():
    def _registrar(self, info=Reg_Cartera):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO cartera values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nl_o_a,info._cliente,info._tCartera,info._tCuota,info._tFactura,info._nFact,info._iAdeudo,info._iPago,info._feP_C,info._cta,
                   info._foPago,info._cheque,info._nContrato,info._sPago,info._usuario,info._feReg,info._comm))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False
            
        
class RegCobranzaData():
    def _registrar(self, info=Reg_Cobranza):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO cobranza values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nFact,info._fePago,info._iPago,info._foPago,info._cta,info._cheque,info._tipoC,info._usuario,info._feReg,info._comm))     
        self.db.commit()        
        if self.cursor.rowcount==1:
            return True
        else:
            return False
        