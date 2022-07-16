
from ast import Is
import os
import re
from ventana_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Analizador Sintactico SQL")
        self.ingreso_texto
        self.botton_ingresar.clicked.connect(self.analizar)
        self.palabras = []
        self.pila = []
        self.ids = []
        self.history=[]
        self.results=[]
        self.resultsContent=[]
        self.resultsForeign = []
        self.resultsOrigin = []
        self.resultsFrom = []
        self.tabla_predictiva = [["", "CREAR", "TABLA", "AGREGAR", "FORANEA", "(", ")", ";", ".", ",", "EN", "TABLA", "DE", "TABLA", "CON", "a..z", "$"],
                                 ["I", ["QC", "PUC", "RR"], "", "", "", "",
                                     "", "", "", "", "", "", "", "", "", "", ""],
                                 ["RR", "RAUX", "", "RAUX", "", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["RAUX", ["R", "PUC", "RR"], "", ["R", "PUC", "RR"],
                                     "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["QC", ["CR", "T", "PA", "ID", "PC", "C"], "", "",
                                     "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["QF", "", "", ["A", "FO", "PA", "ID", "PC", "F"],
                                     "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["R", "QC", "", "QF", "", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["ID", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", ["L", "RES"], ""],
                                 ["RES", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", ["L", "RES"], ""],
                                 ["IDR", "", "", "", "", ["PA", "ID", "PC", "IDRAUX"],
                                  "", "", "", "", "", "", "", "", "", "", ""],
                                 ["IDRAUX", "", "", "", "", "e", "", "e", "e", [
                                     "CO", "IDR"], "", "", "", "", "", "", ""],
                                 ["C", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", ["CON", "IDR"], "", ""],
                                 ["F", "", "", "", "", "", "", "", "", "", "", "", ["DT", "PA",
                                                                                    "ID", "PC", "E"], ["DT", "PA", "ID", "PC", "E"], "", "", ""],
                                 ["E", "", "", "", "", "", "", "", "", "", ["ET", "PA", "ID", "PC"], [
                                     "ET", "PA", "ID", "PC"], "", "", "", "", ""],
                                 ["CR", "CREAR", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["T", "", "TABLA", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["A", "", "", "AGREGAR", "", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["FO", "", "", "", "FORANEA", "", "", "",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["PA", "", "", "", "", "(", "", "", "", "",
                                  "", "", "", "", "", "", ""],
                                 ["PC", "", "", "", "", "", ")", "", "",
                                  "", "", "", "", "", "", "", ""],
                                 ["PUC", "", "", "", "", "", "", ";",
                                  "", "", "", "", "", "", "", "", ""],
                                 ["P", "", "", "", "", "", "", "", ".",
                                     "", "", "", "", "", "", "", ""],
                                 ["CO", "", "", "", "", "", "", "", "",
                                  ",", "", "", "", "", "", "", ""],
                                 ["ET", "", "", "", "", "", "", "", "", "", [
                                     "EN", "TABLA"], ["EN", "TABLA"], "", "", "", "", ""],
                                 ["DT", "", "", "", "", "", "", "", "", "", "", "",
                                  ["DE", "TABLA"], ["DE", "TABLA"], "", "", ""],
                                 ["CON", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "CON", "", ""],
                                 ["L", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "a..z", ""],
                                 ]

    def analizar(self):
        print("Analizando...")
        print(self.ingreso_texto.toPlainText())
        self.palabras = self.ingreso_texto.toPlainText().split(" ")
        self.palabras2 = self.ingreso_texto.toPlainText().split(";")
        print(self.palabras)
        self.Predict()

    def eval_id(self, id):
        patron = re.compile('[a-z]+')
        if patron.match(id) != None:
            self.ids.append(id)
            return True
        else:
            return False

    def Predict(self):
        self.pila.append("I")
        while len(self.palabras) != 0 and len(self.pila) != 0:
            print("ENTRADA: ", self.palabras[0])
            print("PILA: ", self.pila)
            if self.pila[0] == "IDRAUX":
                if(self.palabras[0] == ","):
                    self.pila.pop(0)
                    self.pila.insert(0, "IDR")
                    self.pila.insert(0, "CO")
                else:
                    self.pila.pop(0)
            if self.palabras[0] == ".":
                self.pila.clear()
                self.pila.append(".")
    
            if self.pila[0] == self.palabras[0] or self.pila[0] == "ID" or self.pila[0] == "IDRAUX":
                if self.pila[0] == "ID":
                    if self.eval_id(self.palabras[0]) == False:
                        print("Error: ID no valido")
                        break
                
                self.pila.pop(0)
                self.palabras.pop(0)
            else:
                posx = 0
                posy = 0
                while self.palabras[0] != self.tabla_predictiva[0][posy] and posy < len(self.tabla_predictiva[0])-1:
                    posy += 1
                print("Selecciono Y : ", self.tabla_predictiva[0][posy])
                while self.pila[0] != self.tabla_predictiva[posx][0] and posx < 26:
                    print("X : ", self.tabla_predictiva[posx][0])
                    posx += 1
                print("Selecciono X : ", self.tabla_predictiva[posx][0])
                print("CRUZO : ", self.tabla_predictiva[posx][posy])
                if self.tabla_predictiva[posx][posy] == "":
                    print("Error")
                    break
                else:
                    self.pila.pop(0)
                    if type(self.tabla_predictiva[posx][posy]) == list:
                        aux = self.tabla_predictiva[posx][posy].copy()
                        aux = aux[::-1]
                        for i in aux:
                            self.pila.insert(0, i)
                            self.history.insert(0, i)
                    else:
                        self.pila.insert(0, self.tabla_predictiva[posx][posy])
                        self.history.insert(0, self.tabla_predictiva[posx][posy])
        if len(self.pila) == 0 and len(self.palabras) == 0:
            print("PILA: ", self.pila)
            self.aviso.setText("La sentencia es valida.")
            self.evaluateIds()
            self.ids.clear()
            self.history.clear()
            self.results.clear()
            self.resultsContent.clear()
            self.resultsForeign.clear()
            self.resultsFrom.clear()
            self.resultsOrigin.clear()

        else:
            print("PILA: ", self.pila)
            self.pila.clear()
            self.aviso.setText("La sentencia no es valida.")
    def evaluateIds(self):
        IsRepeated=True
        for i in range(len(self.palabras2)):
            for j in range(len(self.palabras2)):
                if(i!=j):
                    if(self.palabras2[i]==self.palabras2[j]):
                        print("hay sentencias repetidas.")
                        IsRepeated=False
                        break
                    if(len(self.palabras2) == j+1):
                        if(self.palabras2[i]==self.palabras2[j][:len(self.palabras2[j])-1]):
                            print("hay sentencias repetidas.")
                            IsRepeated=False
                            break
        if(IsRepeated==True):
            patron = re.compile('CREAR TABLA \( [a-z]+ \)')
            for i in range(len(self.palabras2)):
                result = re.findall(patron,self.palabras2[i])
                #print(result)
                if(len(result)>0):
                    patron2 = re.compile('[a-z]+')
                    for j in range(len(result)):
                        result2 = re.findall(patron2,result[j])
                        for x in range(len(result2)):
                            self.results.append(result2[x])
            #print(self.results)
            patron = re.compile('AGREGAR FORANEA \( [a-z]+ \)')
            for i in range(len(self.palabras2)):
                result = re.findall(patron,self.palabras2[i])
                #print(result)
                if(len(result)>0):
                    patron2 = re.compile('[a-z]+')
                    for j in range(len(result)):
                        result2 = re.findall(patron2,result[j])
                        for x in range(len(result2)):
                            self.resultsForeign.append(result2[x])
            #print(self.resultsForeign)
            patron = re.compile('DE TABLA \( [a-z]+ \)')
            for i in range(len(self.palabras2)):
                result = re.findall(patron,self.palabras2[i])
                #print(result)
                if(len(result)>0):
                    patron2 = re.compile('[a-z]+')
                    for j in range(len(result)):
                        result2 = re.findall(patron2,result[j])
                        for x in range(len(result2)):
                            self.resultsOrigin.append(result2[x])
            #print(self.resultsOrigin)
            patron = re.compile('EN TABLA \( [a-z]+ \)')
            for i in range(len(self.palabras2)):
                result = re.findall(patron,self.palabras2[i])
                #print(result)
                if(len(result)>0):
                    patron2 = re.compile('[a-z]+')
                    for j in range(len(result)):
                        result2 = re.findall(patron2,result[j])
                        for x in range(len(result2)):
                            self.resultsFrom.append(result2[x])
            IsRepeated=True
            for i in range(len(self.results)):
                for j in range(len(self.results)):
                    if(i!=j):
                        if(self.results[i]==self.results[j]):
                            print("tablas repetidas.")
                            IsRepeated=False
                            break
            if(IsRepeated==True):
                self.generateRelation()

    def generateRelation(self):
        tablas=self.results
        foraneas=self.resultsForeign
        de=self.resultsOrigin
        hacia=self.resultsFrom
        de_hacia=[]
        deF=[]
        haciaF=[]
        if((len(tablas)>=2) and (len(tablas)<=10)):
            for i in range(len(foraneas)):
                for x in range(len(tablas)):
                    for y in range(len(de)):
                        if(de[y]==tablas[x]):
                            for j in range(len(hacia)):
                                #print(de[j]+" "+hacia[j])
                                deF.append(de[j])
                                haciaF.append(hacia[j])
            correct = len(deF)
            deFF=[]
            haciaFF=[]
            for i in range(int(correct)):
                deFF.append(deF[i])
                haciaFF.append(haciaF[i])
            #print(deFF)
            #print(haciaFF)
            self.printDiagram(deFF,haciaFF)
        else:
            print("numero de tablas incorrecto")
                                
                               
    def printDiagram(self,de,hacia):

        path="./code.py"
        code=[]
        for i in range(len(self.results)):
            if(i<len(de)):
                #print(len(self.results))
                #print(len(de))
                #print(i)
                code.append(f"""class {self.results[i]}(object):
                                    def __init__(self):
                                        self.{de[i]}={de[i]}(self,)
                                        return\n""")
            else:
                code.append(f"""class {self.results[i]}(object):
                                    def __init__(self):
                                        return\n""")
        if os.path.exists("./code.py"):
            os.remove('./code.py')
        file = open("./code.py", "w")
        #print(code[i])
        for i in range(len(code)):
            file.write(code[i])
        file.close()
        os.system(f"pyreverse -o png ./code.py -d ./")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
