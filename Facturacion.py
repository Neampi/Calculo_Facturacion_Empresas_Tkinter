
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


empresas={}
anual={}
sumgrupal=[]
class facturacion_window(QMainWindow):

    def __init__(self):
        super().__init__()
        factw=uic.loadUi("empresafacturacion.ui",self)

        self.btnRegistrar.clicked.connect(self.registro)
        self.btnCalcular.clicked.connect(self.calcular)
        

    def registro(self):
        nombre=self.name.text()
        numem=self.empleados.text()
        factu=self.facturacion.text()

        if nombre in empresas.keys():
            self.result.setText("ERROR EMPRESA EXISTENTE EN LOS DATOS")
        elif nombre=='' or numem=='' or factu=='':
            self.result.setText("INGRESE DATO")
        else:
            agregar(nombre,numem,factu)
            
            self.name.setText("")
            self.empleados.setText("")
            self.facturacion.setText("")

    def calcular(self):
        
        imp=''

        for n in empresas and anual:
           
            imp=imp+n+" = "+str(round(anual[n],2))+"\n"

        imp=imp+"\n\nLa suma de facturacion del grupo de empresas es: "+str(sum(sumgrupal))

        self.result.setText(imp)

def agregar(name,num,fa):
        empresas[name]=[num,fa]
        ratio=int(fa)/int(num)
        anual[name]=ratio
        sumgrupal.append(int(fa))

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=facturacion_window()
    window.show()
    sys.exit(app.exec_())
