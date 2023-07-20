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
            "destinos" : self.direccion,
            "coordenadas" : self.coordenadas 
        }

    @classmethod
    def from_json(cls, json_str):
        data = json.load(json_str)
        return cls(data["id"], data["nombre"], data["direccion"], data["coordenadas"])