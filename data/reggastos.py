import conexion_db as con
from model.operaciones import Reg_Gasto


class RegGastoData():
    def _registrar(self, info=Reg_Gasto):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO gastos values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nFact,info._n_prov,info._tipoG,info._descG,info._foPago,info._cheque,info._iPago,info._ivaRet,info._isrRet,info._feGasto,info._usuario,info._feReg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False

        