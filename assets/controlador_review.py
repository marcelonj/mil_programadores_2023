class ControladorReview:
    def __init__(self, app, review=None):
        self.app = app
        self.review = review
        
    def volver(self):
        self.app.cambiar_frame(self.app.vista_reviews)