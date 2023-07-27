from views.detalle_evento import FrameDetalle

class ControladorListaEventos:
    def __init__(self, app, array_eventos):
        self.app = app
        self.array_eventos = array_eventos

    def volver(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_eventos(self):
        return self.array_eventos
    
    def seleccionar_evento(self):
        indice = self.app.vista_eventos.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.array_eventos[indice]
            self.app.vista_detalle.detalles.mostrar_evento(evento)
            self.app.cambiar_frame(self.app.vista_detalle)