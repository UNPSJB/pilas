import sys

from PyQt4 import QtGui

import pilas
from pilas.console import console_widget


class Window(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setMinimumWidth(500)
        vbox = QtGui.QVBoxLayout(self)
        #self.ui.verticalLayout.removeWidget(self.ui.graphicsView)
        pilas.iniciar()
        ventana_pilas = pilas.mundo.motor
        ventana_pilas.setMinimumHeight(500)
        vbox.addWidget(ventana_pilas)
        # Agrega la Consola
        locals = {'pilas': pilas}
        self.consoleWidget = console_widget.ConsoleWidget(locals)
        vbox.addWidget(self.consoleWidget)

        #Crear actor
        self.mono = pilas.actores.Mono()
        pilas.eventos.click_de_mouse.conectar(self.sonreir)

        #self.ui.ventana = pilas.obtener_widget()
        # Agrega un nuevo widget al layout existente.
        #label = QtGui.QLabel(self.ui.centralwidget)
        #self.ui.layout.addWidget(label)
        #label.setText("Hola")

    def sonreir(self, evento):
        self.mono.sonreir()


def main():
    app = QtGui.QApplication(sys.argv)
    ventana = Window()
    ventana.show()
    app.exec_()

if __name__ == '__main__':
    main()
