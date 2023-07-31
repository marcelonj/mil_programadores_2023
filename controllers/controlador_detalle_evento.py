class ControladorDetalleEvento:
    def __init__(self, app, evento=None):
        self.app = app
        self.evento = evento
        
    def volver(self):
        self.app.cambiar_frame(self.app.vista_eventos)

    def review(self):
        self.app.vista_review.control.set_id(self.evento.id)
        self.app.cambiar_frame(self.app.vista_review)