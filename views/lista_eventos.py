import tkinter as tk

class ListaEventos(tk.Frame):
    def __init__(self, master=None, control=None):
        super().__init__(master)
        self.control = control
        self.volver = self.boton_volver()
        self.lista = self.mostrar_lista()

    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.control.volver)
        self.boton_volver.pack(padx=10, pady=10)

    def mostrar_lista(self):
        self.titulo = tk.Label(self, text="Lista de Eventos")
        self.titulo.pack(pady=20)
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(pady=10)
        self.actualizar_eventos()

    def seleccionar_evento(self, event):
        self.control.seleccionar_evento()
    
    def actualizar_eventos(self):
        eventos = self.control.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            detalles = f"{evento.nombre} | {evento.artista} | {evento.genero}"
            self.listbox.insert(tk.END, detalles)

    def obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None