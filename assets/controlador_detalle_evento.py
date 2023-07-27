from models.Ubicacion import Ubicacion

class ControladorDetalleEvento:
    def __init__(self, app, evento=None):
        self.app = app
        self.evento = evento
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/Ubicaciones.json")

    def retornar_evento(self):
        print(self.evento.nombre)

    def obtener_evento(self):
        return self.evento

    def volver(self):
        self.app.cambiar_frame(self.app.vista_eventos)