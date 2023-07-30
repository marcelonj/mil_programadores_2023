class ControladorReview:
    def __init__(self, app, review=None):
        self.app = app
        self.review = review
        self.id = None
        
    def volver(self):
        self.app.cambiar_frame(self.app.vista_detalle)

    def set_id(self, id):
        self.id = id
        print(self.id)

    def retornar_id(self):
        return self.id