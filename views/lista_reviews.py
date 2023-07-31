import tkinter as tk
from tkinter import ttk

class ListaReviews(tk.Frame):
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.master = master
        self.control = control
        self.eventos = self.control.obtener_eventos()
        self.reviews = self.control.obtener_reviews()
        self.filtro_evento()
        self.comentarios()

    def filtro_evento(self):
        eventos = self.nombre_eventos()
        self.mensaje_evento = tk.Label(self, text="Evento: ")
        self.mensaje_evento.grid(row=0, column=0)
        self.seleccionado = tk.StringVar()
        self.seleccion = ttk.Combobox(self, state="readonly", values=eventos, textvariable=self.seleccionado)
        self.seleccion.grid(row=0, column=1)
        self.buscar = tk.Button(self, text="buscar", command=self.mostrar_seleccionados)
        self.buscar.grid(row=0, column=2)
        self.boton_volver = tk.Button(self, text="volver", command=self.control.volver)
        self.boton_volver.grid(row=0, column=3)
    
    def comentarios(self):
        self.comentario = tk.Label(self, text="")
        self.comentario.grid(row=1, column=0, columnspan=3)

    def nombre_eventos(self):
        array_nombre_eventos = []
        for evento in self.eventos:
            array_nombre_eventos.append(evento.nombre)
        return array_nombre_eventos
    
    def mostrar_seleccionados(self):
        id = None
        mensaje = ""
        for evento in self.eventos:
            if evento.nombre == self.seleccionado.get():
                id = evento.id
        for review in self.reviews:
            if review.id_evento == id:
                mensaje = mensaje + review.comentario + "\n-----------------------\n"
        self.comentario["text"] = mensaje