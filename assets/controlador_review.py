from models.Review import Review

class ControladorReview:
    def __init__(self, app, array_reviews):
        self.app = app
        self.review = array_reviews
        self.id = None
        
    def volver(self):
        self.app.cambiar_frame(self.app.vista_detalle)

    def set_id(self, id):
        self.id = id
        print(self.id)

    def retornar_id(self):
        return self.id
    
    def publicar_review(self, comentario, animo):
        estado_animo = {
            0: "Unlike",
            1: "Like"
        }
        nueva_review = Review(len(self.review ) + 1, self.id, 1, "Bueno", comentario, estado_animo[animo])
        self.review.append(nueva_review)
        Review.save_reviews("data/Reviews.json", self.review)