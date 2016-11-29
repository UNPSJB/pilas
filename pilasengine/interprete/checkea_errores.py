from PyQt4.QtCore import QObject, QThread

from multiprocessing import Process

def llamar_a_pylint(nombre_archivo):
    proc = Process(checker)
    return {}

class CheckeadorDeErrores(QThread):
    """
    Checkeador de código, recibe una señal con el nombre de archivo a checkear
    y una vez realizado el checkeo emite otra señal con el resultado del checkeo.
    Esta úlitma lleva como argumento el diccionario compuesto por 
        {
            numero_de_linea: "mensae"
        }
    Este objeto chckea un archivo a la vez
    """
    def __init__(self, parent=None):
        QThread.__init__(parent)
        self.proc = None

    def checkear(self, nombre_archivo):
        pass
    
    def run(self):
        self.proc = Popen()
