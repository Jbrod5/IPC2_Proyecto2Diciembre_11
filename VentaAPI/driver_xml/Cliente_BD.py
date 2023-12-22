
import xml.etree.ElementTree as ET
from modelos.Cliente import Cliente
#from lista.Lista import Lista
import os.path as path


class Cliente_BD:
    
    def __init__(self):
        self.ruta = "./CLIENTE_BD.xml"
        if not path.exists(self.ruta):
            try:
                root = ET.Element("CLIENTE_BD")
                tree = ET.ElementTree(root)
                tree.write(self.ruta)
                print(f"El archivo se ha creado correctamente.")
            except IOError:
                print(f"No se pudo crear el archivo.")
        else:
            print(f"El archivo {self.ruta} ya existe.")
    
    # Recibe de Parametro un Cliente Nuevo para su verificación si no existe lo crea y retorna True, caso contrario retorna False
    def verificarClienteNuevo(self, clienteAIngresar: Cliente):

        if path.exists(self.ruta):
                            
            cliente_existente = self.obtenerClienteEspecifico(clienteAIngresar.obtener_nit())
            
            if cliente_existente is not None:
                print("Ya hay un Usuario Ingresado con ese NIT")
                return False
            else:
                self.ingresarClienteNuevo(clienteAIngresar)
                return True
        else:
            self.ingresarClienteNuevo(clienteAIngresar)
            return True
          
    # (DE USO EXCLUSIVO DE ESTA CLASE) Se invoca este metodo en caso el Cliente no este Registrado en el XML
    def ingresarClienteNuevo(self, clienteAIngresar: Cliente):

        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("CLIENTE_BD")
            tree = ET.ElementTree(root)


        # Verificar que los atributos del cliente sean string
        if isinstance (clienteAIngresar.obtener_nit(), int):
            clienteAIngresar.establecer_nit( str(clienteAIngresar.obtener_nit()) )

          
        cliente_Elemento = ET.SubElement(root, "CLIENTE", ID=clienteAIngresar.obtener_nit())
        ET.SubElement(cliente_Elemento, "NOMBRE").text = clienteAIngresar.obtener_nombre()
        ET.SubElement(cliente_Elemento, "NIT").text = clienteAIngresar.obtener_nit()
        ET.SubElement(cliente_Elemento, "DIRECCION").text = clienteAIngresar.obtener_direccion()
        tree.write(self.ruta)
            
    # Obtiene todos los Clientes del Archivo XML, en caso el archivo no exista retorna None
    def obtenerTodosLosClientes(self):

        if path.exists(self.ruta):
            try:
                xml_file = open(self.ruta)
                
                if xml_file.readable():
                    listaClientes = []
                    xml_data = ET.fromstring(xml_file.read())
                    listaArchivo = xml_data.findall('CLIENTE')
                    
                    for cliente in listaArchivo:
                        nombre = cliente.find('NOMBRE').text
                        nit = cliente.find('NIT').text
                        direccion = cliente.find('DIRECCION').text
                        
                        cliente = Cliente(nombre, nit, direccion)
                        listaClientes.append(cliente)
                        
                    return listaClientes
            
            except FileNotFoundError as err:
                print("Error: ", err)   
            except Exception as err:
                print("Error: ", err)
                   
            finally:
                xml_file.close()
        return None
    
    # Obtiene un cliente en especifico localizado por medio del NIT, en caso no haya concidencia o este vacia retorna None
    def obtenerClienteEspecifico(self, nitCliente: int):
        listaClientes = self.obtenerTodosLosClientes()
        
        if listaClientes is not None:
            for i in range(len(listaClientes)):
                #clienteRecibido = listaClientes.obtenerContenido(i + 1).obtenerElementoNodo()
                clienteRecibido = listaClientes[i]
                if nitCliente == clienteRecibido.obtener_nit():
                    return clienteRecibido
        return None
      
    # Elimina un Usuario en base a su NIT y retorna True, caso contrario retorna False     
    def eliminarCliente(self, nitCliente: int):
        
        if path.exists(self.ruta):
            try:
                tree = ET.parse(self.ruta)
                root = tree.getroot()
                
                for cliente in root.findall('CLIENTE'):
                    id = cliente.get('ID')
                    
                    if int(id) == nitCliente:
                        root.remove(cliente)
                tree.write(self.ruta)
                return True
            except FileNotFoundError:
                root = ET.Element("CLIENTE_BD")
                tree = ET.ElementTree(root)
        return False

    # Actualizar a un Cliente en base a su NIT, el valor Nuevo y la etiqueta a modificar
    # Si todo se realiza bien retorna True, caso Contrario retorna False
    def actualizarCliente(self, nitCliente: int, etiqueta, dato):
        
        if path.exists(self.ruta):
            try:
                tree = ET.parse(self.ruta)
                root = tree.getroot()
                
                clienteEspecifico = self.obtenerClienteEspecifico(nitCliente)
                cliente_existente = root.find(f"./CLIENTE[@ID='{clienteEspecifico.obtener_nit()}'][NIT='{nitCliente}']")
                cliente_existente.find(etiqueta).text = dato       
                tree.write(self.ruta)
                return True
            except FileNotFoundError:
                root = ET.Element("CLIENTE_BD")
                tree = ET.ElementTree(root)
        return False
        