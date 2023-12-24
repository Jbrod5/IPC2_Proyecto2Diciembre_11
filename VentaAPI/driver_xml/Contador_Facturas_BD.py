from os import path
import xml.etree.ElementTree as ET

class Contador_Facturas_BD:
    
    def __init__(self):
        self.ruta = "./CONTADOR_FACTURAS.xml"
        
    def iniciarContador(self):
        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("CONTADOR_FACTURAS")
            tree = ET.ElementTree(root)
        
        contador_elemento = ET.SubElement(root, "CONTADOR", ID="Cont")
        ET.SubElement(contador_elemento, "NUMERO").text = "1"
        tree.write(self.ruta)
        
    def incrementarContador(self):
        try:
            tree = ET.parse(self.ruta)
            root = tree.getroot()
            
            contador_existente = root.find(f"./CONTADOR[@ID='Cont']")
            numero = int(contador_existente.find("NUMERO").text)
            numero += 1
            contador_existente.find("NUMERO").text = str(numero)
            tree.write(self.ruta)
        except FileNotFoundError:
            root = ET.Element("CONTADOR_FACTURAS")
            tree = ET.ElementTree(root)
            
    def obtenerNumeroActual(self):

        if path.exists(self.ruta):
            try:
                tree = ET.parse(self.ruta)
                root = tree.getroot()
                
                contador_existente = root.find(f"./CONTADOR[@ID='Cont']")
                numero = contador_existente.find("NUMERO").text 
                return numero
            except FileNotFoundError:
                root = ET.Element("CONTADOR_FACTURAS")
                tree = ET.ElementTree(root)  
        else:
            self.iniciarContador()
            return 1  