#clase 
class RegCliente():
    def __init__(self, nombre, rfc, tContribuyente, curp, num_area_o_local, tCliente, giro, direccion, numcel, email, fechareg, status_cliente, usuario):
        self._nombre = nombre
        self._rfc = rfc
        self._tipoC = tContribuyente
        self._curp = curp
        self._num_a_o_l= num_area_o_local
        self._tipoCl = tCliente
        self._giro  = giro
        self._direccion = direccion
        self._numcel = numcel
        self._email = email
        self._fReg = fechareg
        self._status= status_cliente
        self._usuario = usuario
        
        
    