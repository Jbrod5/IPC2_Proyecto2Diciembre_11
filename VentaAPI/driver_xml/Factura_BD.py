import xml.etree.ElementTree as ET
import os.path as path
from VentaAPI.driver_xml.Contador_Facturas_BD import Contador_Facturas_BD
from VentaAPI.modelos import Factura, ProductoGuia

class Factura_BD:
    
    def __init__(self):
        self.ruta = "./FACTURA_BD.xml"
        
    # Este método ingresa una nueva factura al XML
    def ingresarFactura(self, facturaAIngresar: Factura):
        
        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("FACTURA_BD")
            tree = ET.ElementTree(root)
        
        contador = Contador_Facturas_BD()
        facturaAIngresar.establecer_noFactura(str(contador.obtenerNumeroActual()))
        contador.incrementarContador()
        
        factura_elemento = ET.SubElement(root, "FACTURA", ID=facturaAIngresar.obtener_noFactura())
        ET.SubElement(factura_elemento, "NO_FACTURA").text = facturaAIngresar.obtener_noFactura()
        ET.SubElement(factura_elemento, "NIT").text = facturaAIngresar.obtener_nit()
        ET.SubElement(factura_elemento, "FECHA_EMISION").text = facturaAIngresar.obtener_FechaDeEmision()
        listaDeCompras = facturaAIngresar.obtener_ListaProductosComprados()
        
        for productoGuia in listaDeCompras:
            productos_comprados = ET.SubElement(factura_elemento, "PRODUCTO", ID=facturaAIngresar.obtener_noFactura())
            ET.SubElement(productos_comprados, "CODIGO_PRODUCTO").text = productoGuia.obtener_codigoProducto()
            ET.SubElement(productos_comprados, "CANTIDAD_ADQUIRIDA").text = productoGuia.obtener_cantidadAdquirida()      
        tree.write(self.ruta)
        
    # Obtenemos todas las facturas disponibles en el archivo
    def obtenerTodasLasFacturas(self):
        listaFacturas = []
        
        if path.exists(self.ruta):
            try:
                tree = ET.parse(self.ruta)
                root = tree.getroot()
                
                for factura in root.findall('FACTURA'):
                    noFactura = factura.find('NO_FACTURA').text
                    nit = factura.find('NIT').text
                    fechaDeEmision = factura.find('FECHA_EMISION').text
                    
                    productos = factura.findall(f"./PRODUCTO[@ID='{factura.find('NO_FACTURA').text}']")
                    facturaEntrante = Factura(nit, fechaDeEmision)
                    facturaEntrante.establecer_noFactura(noFactura)
                    
                    for producto in productos:
                        codigoProducto = producto.find('CODIGO_PRODUCTO').text
                        cantidadAdquirida = producto.find('CANTIDAD_ADQUIRIDA').text
                        facturaEntrante.agregarProducto(ProductoGuia(codigoProducto, cantidadAdquirida))
                    listaFacturas.append(facturaEntrante)         
            except Exception | FileNotFoundError as err:
                print("Error: ", err)            
        return listaFacturas
    
    # Obtenemos una lista con todas las facturas de un cliente en especifico
    def obtenerFacturasDeUnClienteEspecifico(self, nitCliente: int):
        listaFacturas = self.obtenerTodasLasFacturas()
        listaFacturasCliente = []
        
        for factura in listaFacturas:
            
            if nitCliente == int(factura.obtener_nit()):
                listaFacturasCliente.append(factura)                 
        return listaFacturasCliente       

    # Elimina una factura en base a su No de Factura
    def eliminarFactura(self, noFactura: int):
        
        if path.exists(self.ruta):
            try:
                tree = ET.parse(self.ruta)
                root = tree.getroot()
                
                for factura in root.findall('FACTURA'):
                    id = factura.get('ID')
                    
                    if int(id) == noFactura:
                        root.remove(factura)
                tree.write(self.ruta)
                return True
            except Exception | FileNotFoundError as err:
                print("Error: ", err)                
        return False
