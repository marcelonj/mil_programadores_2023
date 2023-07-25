import json

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_json(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "direccion" : self.direccion,
            "coordenadas" : self.coordenadas 
        }
    
    def devolverDireccion(self):
        return self.direccion
    
    def devolverCoordenadas(self):
        return self.coordenadas

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_ubicaciones(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]