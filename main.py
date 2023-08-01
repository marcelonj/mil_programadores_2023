import tkinter as tk
import customtkinter
from views.lista_reviews import ListaReviews
from views.ventana_principal import VentanaPrincipal
from views.lista_eventos import ListaEventos
from views.detalle_evento import DetalleEvento
from views.ventana_review import DejarReview
from controllers.controlador_vista_principal import ControladorVistaPrincipal
from controllers.controlador_lista_eventos import ControladorListaEventos
from controllers.controlador_detalle_evento import ControladorDetalleEvento
from controllers.controlador_lista_review import ControladorListaReviews
from controllers.controlador_review import ControladorReview
from models.Evento import Evento
from models.Review import Review 

class Aplicacion(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Tour Musical')
        self.geometry('800x600')
        self.resizable(width=0, height=0)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        array_eventos = Evento.cargar_eventos("data/Eventos.json")
        array_reviews = Review.load_reviews("data/Reviews.json")

        controlador_inicio = ControladorVistaPrincipal(self)
        controlador_lista_eventos = ControladorListaEventos(self, array_eventos)
        controlador_detalle_evento = ControladorDetalleEvento(self)
        controlador_review = ControladorReview(self, array_reviews)
        controlador_lista_reviews = ControladorListaReviews(self, array_reviews, array_eventos) 

        self.vista_inicio = VentanaPrincipal(self, controlador_inicio)
        self.vista_eventos = ListaEventos(self, controlador_lista_eventos)
        self.vista_detalle = DetalleEvento(self, controlador_detalle_evento)
        self.vista_review = DejarReview(self, controlador_review)
        self.vista_lista_reviews = ListaReviews(self, controlador_lista_reviews) 

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_detalle)
        self.ajustar_frame(self.vista_review)
        self.ajustar_frame(self.vista_lista_reviews)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()