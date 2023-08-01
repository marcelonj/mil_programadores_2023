from views.vista_mapa import VistaMapa
from models.Evento import Evento
from models.Ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = VistaMapa(root, self.seleccionar_evento, seleccionar_ubicacion)
        self.array_eventos = Evento.cargar_eventos("app/data/Eventos.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/Ubicaciones.json")
        self.marcadores = []
        self.imagenes = []

        self.cargar_eventos()
        self.cargar_imagenes()
        self.cargar_marcadores()
        
    def cargar_locales(self):
        for evento in self.array_eventos:
            self.vista.agregar_local(evento)
        
    def cargar_imagenes(self):
        for evento in self.array_eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{Evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, evento in zip(self.ubicaciones, self.array_eventos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, Evento.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_evento(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.array_eventos.curselection()
        # Obtiene el evento seleccionado
        evento_seleccionado = self.Evento[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al evento seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == evento_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)