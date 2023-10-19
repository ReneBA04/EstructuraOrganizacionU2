class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    
    def esHijoIzquierdo(self):
        return self.padre and self.padre.Hijoizquierdo==self

    def esHijoDerecho(self):
        return self.padre and self.padre.HijoDerecho==self
    
    def esRaiz(self):
        return not self.padre
    
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    
    def tieneAlgunHijo(self):
        return self.esHijoDerecho or self.esHijoIzquierdo
    
    def tieneAmbosHijos(self):
        return self.esHijoDerecho and self.esHijoIzquierdo
    
    def reemplezarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre=self

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano=self.tamano+1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
