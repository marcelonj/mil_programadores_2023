import json

class RutaVisita:
    def __init__(self, id, nombre, destinos = []):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "destinos" : self.destinos 
        }

    def agregarEvento(self, evento):
        self.destinos.append(evento)

    def retornarEventos(self):
        if len(self.destinos) > 0:
            return self.destinos
        else:
            raise ValueError("La ruta no contiene detinos")
    
    @classmethod
    def from_json(cls, json_str):
        data = json.load(json_str)
        return cls(data["id"], data["nombre"], data["destinos"])