

class Reg_Cartera():
    def __init__(self,local_o_area="",clienteFact="",tipoCartera="",tipoCuota="",tipo_factura="",numFact="",importeAdeudo="",importePago="",fPago_Cobro="",
                 ctaBanco="",formaPago="",cheque="",numContrato="",statusPago="",usuario="",fechaReg="",comentarios=""):
        self._nl_o_a = local_o_area
        self._cliente=clienteFact
        self._tCartera=tipoCartera
        self._tCuota = tipoCuota
        self._tFactura = tipo_factura
        self._nFact = numFact
        self._iAdeudo= importeAdeudo
        self._iPago = importePago
        self._feP_C = fPago_Cobro
        self._cta = ctaBanco
        self._foPago  = formaPago
        self._cheque  = cheque
        self._nContrato=numContrato
        self._sPago=statusPago
        self._usuario = usuario
        self._feReg = fechaReg
        self._comm = comentarios
     
   
class Reg_Cobranza():
    def __init__(self,num_fact="",fecha_pago="",importe_pago="",forma_pago="",cta_banco="",num_cheque="",tipoCuota="",usuario="",fechaReg="",comentarios=""):
        self._nFact = num_fact
        self._fePago = fecha_pago
        self._iPago = importe_pago
        self._foPago  = forma_pago
        self._cta = cta_banco
        self._cheque  = num_cheque
        self._tipoC=tipoCuota
        self._usuario = usuario
        self._feReg = fechaReg
        self._comm = comentarios
       
   
class Reg_Factura():
    def __init__(self,num_factura="",cliente="",local_o_area="",fecha_factura="",tipo_cuota="",importe_factura="",tipo_factura="",tipo_cartera="",status_pago="",usuario="",fecha_reg=""):
        self._num_factura=num_factura
        self._cliente=cliente
        self._nl_o_a = local_o_area
        self._fecha_factura=fecha_factura
        self._tipo_cuota=tipo_cuota
        self._importe_factura=importe_factura
        self._tipo_factura=tipo_factura
        self._tipo_cartera=tipo_cartera
        self._status_pago=status_pago
        self._usuario=usuario
        self._fecha_reg=fecha_reg        

class Reg_Gasto():
    def __init__(self,num_fact="",n_proveedor="",t_gasto="",desc_gasto="",f_pago="",n_cheque="",i_pago="",iva_ret="",isr_ret="",f_gasto="",usuario="",f_reg=""):
        self._nFact=num_fact
        self._n_prov=n_proveedor
        self._tipoG=t_gasto
        self._descG=desc_gasto
        self._foPago=f_pago
        self._cheque=n_cheque
        self._iPago=i_pago
        self._ivaRet=iva_ret
        self._isrRet=isr_ret
        self._feGasto=f_gasto
        self._usuario=usuario
        self._feReg=f_reg
   