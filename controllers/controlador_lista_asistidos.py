from models.Asistidos import Asistido


class ControladorListaAsistidos:
    def __init__(self, app, array_asistidos, array_eventos):
        self.app = app
        self.array_asistidos = array_asistidos
        self.array_eventos = array_eventos

    def volver(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_asistidos(self):
        return self.array_asistidos
    
    def obtener_eventos(self):
        return self.array_eventos
    
    def obtener_asistidos(self):
        return self.array_asistidos
    
    def seleccionar_asistido(self):
        indice = self.app.vista_reviews.obtener_asistido_seleccionado()
        if indice is not None:
            asistido = self.array_asistidos[indice]
            self.app.vista_asistidos.detalles.mostrar_asistido(asistido)
            self.app.cambiar_frame(self.app.vista_asistido)