
class ProductoGuia:
    
    def __init__(self, codigoProducto, cantidadAdquirida):
        self._codigoProducto = codigoProducto
        self._cantidadAdquirida = cantidadAdquirida
        
    def obtener_codigoProducto(self):
        return self._codigoProducto
    
    def obtener_cantidadAdquirida(self):
        return self._cantidadAdquirida
    
    def obtener_diccionario_producto_guia(self):
        return self.__dict__