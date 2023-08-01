import tkinter as tk
import customtkinter as ctk

class VentanaPrincipal(ctk.CTkFrame):
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.control = control
        self.mi_widget = self.tres_botones()
        
    def tres_botones(self):
        self.boton_eventos = ctk.CTkButton(self, text= 'Mostrar todos los eventos', command=self.control.mostrar_eventos)
        self.boton_eventos.pack(pady=50, padx=330)
        self.boton_reviews = ctk.CTkButton(self, text= 'Reviews', command=self.control.mostrar_reviews)
        self.boton_reviews.pack(pady=50, padx=330)
        self.boton_asistidos = ctk.CTkButton(self, text= 'Eventos asistidos')
        self.boton_asistidos.pack(pady=50, padx=330)