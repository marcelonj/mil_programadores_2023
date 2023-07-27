import tkinter as tk

class DetalleEvento(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.control = control
        self.detalles = FrameDetalle(self, control=self.control)
        self.detalles.config(width=400, height=600, bg="blue")
        self.detalles.pack(side="left", fill="both")

class FrameDetalle(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.master = master
        self.control = control        

        self.nombre = tk.Label(self, text="")
        self.nombre.pack(pady=20, padx=20)
        self.artista = tk.Label(self, text="")
        self.artista.pack(pady=20, padx=20)
        self.genero = tk.Label(self, text="")
        self.genero.pack(pady=20, padx=20)
        self.hora_inicio = tk.Label(self, text="")
        self.hora_inicio.pack(pady=20, padx=20)
        self.hora_fin = tk.Label(self, text="")
        self.hora_fin.pack(pady=20, padx=20)
        self.descripcion = tk.Label(self, text="")
        self.descripcion.pack(pady=20, padx=20)

        self.boton_volver()        

    def mostrar_evento(self, evento):
            nombre_evento = f"{evento.nombre}"
            self.nombre["text"] = nombre_evento
            artista_evento = f"Artista: {evento.artista}"
            self.artista["text"] = artista_evento
            genero_evento = f"Genero: {evento.genero}"
            self.genero["text"] = genero_evento
            hora_inicio_evento = f"Hora de inicio: {evento.hora_inicio}"
            self.hora_inicio["text"] = hora_inicio_evento
            hora_fin_evento = f"Hora de finalizacion: {evento.hora_fin}"
            self.hora_fin["text"] = hora_fin_evento
            descripcion_evento = f"Descripcion: {evento.descripcion}"
            self.descripcion["text"] = descripcion_evento

    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.control.volver)
        self.boton_volver.pack(padx=10, pady=10)