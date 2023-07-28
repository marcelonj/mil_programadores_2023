import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView

class VistaMapa(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.frame_mapa = tk.Frame(self.master, width=600, height=600)
        self.frame_mapa.pack(side='right')

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

    def agregar_evento(self, evento):
        nombre = evento.nombre
        self.lista_eventos.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen)