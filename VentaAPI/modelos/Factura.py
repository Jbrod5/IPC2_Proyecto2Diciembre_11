
class Factura:
    
    def __init__(self, nit, fechaEmision):
        self._noFactura = 0
        self._nit = nit
        self._listaDeProductosComprados = []
        self._fechaDeEmision = fechaEmision
        
    def establecer_noFactura(self, noFactura):
        self._noFactura = noFactura
    def establecer_fecha_emision(self, fecha):
        self._fechaDeEmision = fecha
        
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
    
    def obtener_diccionario(self):
        
        dict_productos = {}
        contador = 0
        while contador < len(self._listaDeProductosComprados):
            tupla = self._listaDeProductosComprados[contador]
            dict_productos[tupla.obtener_codigoProducto()] = tupla.obtener_cantidadAdquirida()
            contador += 1

        dict = {
            "Numero": self._noFactura,
            "Nit": self._nit,
            "Fecha_emision": self._fechaDeEmision,
            "Productos" : dict_productos 
            }
        return dict