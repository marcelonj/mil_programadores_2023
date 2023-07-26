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

    @classmethod
    def load_reviews(cls, file_path):
        reviews = []
        with open(file_path, 'r') as file:
            data = json.load(file)
            for review_data in data:
                review = cls(**review_data)
                reviews.append(review)
        return reviews

    @classmethod
    def save_reviews(cls, file_path, reviews):
        data = [review.to_json() for review in reviews]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def find_by_event_id(reviews, event_id):
        return [review for review in reviews if review.id_evento == event_id]

    @staticmethod
    def find_by_user_id(reviews, user_id):
        return [review for review in reviews if review.id_usuario == user_id]
