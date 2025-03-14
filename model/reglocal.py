#clase 
class RegLocal():
    def __init__(self, num_local="", superficie="", cuota="", dg="", nom_propietario="", rfc_propietario="", cliente="", giro="", status="", usuario="", fechareg=""):
        self._numLocal = num_local
        self._sup = superficie  
        self._cuota = cuota
        self._dg = dg
        self._nomPropietario  = nom_propietario
        self._rfcPropietario= rfc_propietario
        self._cliente = cliente
        self._giro = giro
        self._status = status
        self._usuario = usuario
        self._fReg = fechareg
       
    