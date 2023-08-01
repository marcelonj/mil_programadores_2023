import tkinter as tk
from tkinter import ttk

""" Vista que permite realizar la busqueda de asistidos por un usuario"""

class ListaAsistidos(tk.Frame):
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.master = master
        self.control = control
        self.eventos = self.control.obtener_eventos()
        self.reviews = self.control.obtener_reviews()
        self.reviews = self.control.obtener_asistidos()
        self.filtro_asistido()
        

    def filtro_asistido(self):
        usuario = self.id_usuario()
        self.mensaje_evento = tk.Label(self, text="Usuario: ")
        self.mensaje_evento.grid(row=0, column=0)
        self.seleccionado = tk.StringVar()
        self.seleccion = ttk.Combobox(self, state="readonly", values=ListaAsistidos, textvariable=self.seleccionado)
        self.seleccion.grid(row=0, column=1)
        self.buscar = tk.Button(self, text="buscar", command=self.mostrar_seleccionados)
        self.buscar.grid(row=0, column=2)
        self.boton_volver = tk.Button(self, text="volver", command=self.control.volver)
        self.boton_volver.grid(row=0, column=3)
    
    def nombre_asistidos(self):
        array_nombre_eventos_asistidos = []
        for evento in self.eventos:
            array_nombre_eventos_asistidos.append(evento.nombre)
        return array_nombre_eventos_asistidos
    
    def mostrar_seleccionados(self):
        id = None
        mensaje = ""
        for asistido in self.asistidos:
            if asistido.usuario_id == self.seleccionado.get():
                print(f"{evento.nombre} \n-----------------------\n")
        