import json

class Asistidos:
    def __init__(self, id, id_evento, id_usuario):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        
    def to_json(self):
        return {
            "id": self.id,
            "id_evento": self.id_evento,
            "id_usuario": self.id_usuario,
            }

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    @classmethod
    def load_asistidos(cls, file_path):
        asistidos = []
        with open(file_path, 'r') as file:
            data = json.load(file)
            for asistidos_data in data:
                asistido = cls(**asistidos_data)
                asistidos.append(asistido)
        return asistidos

    @classmethod
    def save_asistidos(cls, file_path, asistidos):
        data = [asistido.to_json() for asistido in asistidos]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def find_by_user_id(asistidos, user_id):
        return [asistido for asistido in asistidos if asistido.id_usuario == user_id]

   