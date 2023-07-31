import tkinter as tk

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.control = control
        self.mi_widget = self.tres_botones()
        
    def tres_botones(self):
        self.boton_eventos = tk.Button(self, text= 'Mostrar todos los eventos', command=self.control.mostrar_eventos)
        self.boton_eventos.pack(pady=50, padx=330)
        self.boton_reviews = tk.Button(self, text= 'Reviews', command=self.control.mostrar_reviews)
        self.boton_reviews.pack(pady=50, padx=330)
        self.boton_asistidos = tk.Button(self, text= 'Eventos asistidos')
        self.boton_asistidos.pack(pady=50, padx=330)