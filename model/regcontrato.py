
class RegContrato():
    def __init__(self, n_contrato, c_facturacion, n_area, f_inicio, f_fin, m_cuota, m_dg, t_contrato, s_contrato, s_vigencia, r_usuario, f_registro):
        self._numContrato=n_contrato
        self._clienteFact=c_facturacion
        self._area=n_area
        self._fechaInicio=f_inicio
        self._fechaFin=f_fin
        self._cuota=m_cuota
        self._dg=m_dg
        self._tipoContrato=t_contrato
        self._statusContrato=s_contrato
        self._statusVigencia=s_vigencia
        self._usuarioReg=r_usuario
        self._fechaReg=f_registro

           