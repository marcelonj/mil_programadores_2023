import tkinter as tk
from views.ventana_principal import VentanaPrincipal
from views.lista_eventos import ListaEventos
from assets.controlador_vista_principal import ControladorVistaPrincipal
from assets.controlador_lista_eventos import ControladorListaEventos
from models.Evento import Evento

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tour Musical')
        self.geometry('800x600')
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        array_eventos = Evento.cargar_eventos("data/Eventos.json")

        controlador_inicio = ControladorVistaPrincipal(self)
        controlador_lista_eventos = ControladorListaEventos(self, array_eventos)

        self.vista_inicio = VentanaPrincipal(self, controlador_inicio)
        self.vista_eventos = ListaEventos(self, controlador_lista_eventos)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()