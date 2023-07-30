from models.Review import Review


class ControladorListaReviews:
    def __init__(self, app, array_reviews):
        self.app = app
        self.array_reviews = array_reviews
        self.reviews = Review.load_reviews("data/Reviews.json")

    def volver(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_reviews(self):
        return self.array_reviews
    
    def seleccionar_review(self):
        indice = self.app.vista_reviews.obtener_review_seleccionado()
        if indice is not None:
            review = self.array_reviews[indice]
            self.app.vista_review.detalles.mostrar_review(review)
            self.app.cambiar_frame(self.app.vista_review)
