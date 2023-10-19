class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil=valor
        self.hijoIzquierdo=izquierdo
        self.hijoDerecho=derecho
        self.padre=padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    