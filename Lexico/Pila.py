class Pila:
    def __init__(self):
        self.items=[]
    def apilar(self, x):
        self.items.append(x)
    def es_vacia(self):
        return self.items == []
    def showPila(self):
        return self.items
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def length(self):
        return len(self.items)
    def getTop(self):
        self.dato = self.items.pop()
        self.items.append(self.dato)
        return self.dato