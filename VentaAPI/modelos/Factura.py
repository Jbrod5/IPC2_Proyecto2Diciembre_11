
class Factura:
    
    def __init__(self, nit, fechaEmision):
        self._noFactura = 0
        self._nit = nit
        self._listaDeProductosComprados = []
        self._fechaDeEmision = fechaEmision
        
    def establecer_noFactura(self, noFactura):
        self._noFactura = noFactura
        
    def obtener_noFactura(self):
        return self._noFactura
    
    def obtener_nit(self):
        return self._nit
    
    def agregarProducto(self, productoComprado):
        self._listaDeProductosComprados.append(productoComprado)
        
    def obtener_ListaProductosComprados(self):
        return self._listaDeProductosComprados
    
    def obtener_FechaDeEmision(self):
        return self._fechaDeEmision
    