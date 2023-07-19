class Usuario:
    def __init__(self, nombre, apellido, historial=None):
        self.nombre = nombre
        self.apellido= apellido
        if historial is None :
          self.items=[]
        else:
          self.historial= historial
