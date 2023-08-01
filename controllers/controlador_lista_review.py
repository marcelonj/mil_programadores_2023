from models.Review import Review


class ControladorListaReviews:
    def __init__(self, app, array_reviews, array_eventos):
        self.app = app
        self.array_reviews = array_reviews
        self.array_eventos = array_eventos

    def volver(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_reviews(self):
        return self.array_reviews
    
    def obtener_eventos(self):
        return self.array_eventos
    
    def seleccionar_review(self):
        indice = self.app.vista_reviews.obtener_review_seleccionado()
        if indice is not None:
            review = self.array_reviews[indice]
            self.app.vista_review.detalles.mostrar_review(review)
            self.app.cambiar_frame(self.app.vista_review)
