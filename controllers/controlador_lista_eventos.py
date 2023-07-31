from models.Ubicacion import Ubicacion

from PIL import Image, ImageTk

class ControladorListaEventos:
    def __init__(self, app, array_eventos):
        self.app = app
        self.array_eventos = array_eventos
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/Ubicaciones.json")
        
        self.imagenes = []
        self.cargar_imagenes()

    def cargar_imagenes(self):
        for evento in self.array_eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"assets/images/{evento.imagen}").resize((150, 150))) #
            self.imagenes.append(imagen)

    def volver(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_eventos(self):
        return self.array_eventos
    
    def seleccionar_evento(self):
        indice = self.app.vista_eventos.obtener_evento_seleccionado()
        if indice is not None:
            evento = self.array_eventos[indice]
            indice_ubicacion = self.array_eventos[indice].id_ubicacion - 1
            ubicacion = self.ubicaciones[indice_ubicacion]
            self.app.vista_detalle.detalles.mostrar_evento(evento)
            self.app.vista_detalle.colocar_marcador(ubicacion.coordenadas[0], ubicacion.coordenadas[1], ubicacion.nombre)
            self.app.cambiar_frame(self.app.vista_detalle)