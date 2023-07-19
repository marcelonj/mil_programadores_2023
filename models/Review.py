import json

class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return {
            "id": self.id,
            "id_evento": self.id_evento,
            "id_usuario": self.id_usuario,
            "calificacion": self.calificacion,
            "comentario": self.comentario,
            "animo": self.animo
        }

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['id'], data['id_evento'], data['id_usuario'], data['calificacion'], data['comentario'], data['animo'])
