class Nodo:
    def __init__(self, value=None, izq=None, der=None):
        self.value=value
        self.izq=izq
        self.der=der

    def __str__(self):
        return self.value

class aBinarios:
    def __init__(self):
        self.raiz=None
    def agregar(self,elemnto):
        if self.raiz==None:
            self.raiz=elemnto
        else:
            aux=self.raiz
            padre=None
            while aux != None:
                padre=aux
                if int(elemnto.value) >= int(aux.value):
                    aux=aux.der
                else:
                    aux=aux.izq
            if int(elemnto.value) >= int(padre.value):
                padre.der=elemnto
            else:
                padre.izq = elemnto
    # se crea un metodo para mostrar el preorder

    def preorder(self,elemento):
        if elemento != None:
            print(elemento)
            self.preorder(elemento.izq)
            self.preorder(elemento.der)