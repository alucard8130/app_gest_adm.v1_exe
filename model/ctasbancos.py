#clase empresa
class Cuentas():
    def __init__(self, nombre_banco="", num_cta="", tipo_cta="",tipo_moneda="",usuario="",fechareg=""):
        self._name = nombre_banco
        self._cta = num_cta
        self._tipo = tipo_cta
        self._moneda = tipo_moneda
        self._user = usuario
        self._fReg = fechareg
    