import tkinter as tk
from views.vista_mapa import VistaMapa


class DetalleEvento(tk.Frame): 
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.control = control
        self.detalles = FrameDetalle(self, control=self.control)
        self.detalles.place(x=0, y=0, width=250, height=600)
        self.mapa = VistaMapa(self)
        self.mapa.pack(side="right")

      

    def colocar_marcador(self, latitud, longitud, texto):
        self.mapa.mapa.set_position(latitud, longitud)
        self.mapa.agregar_marcador_mapa(latitud, longitud, texto)

class FrameDetalle(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.master = master
        self.control = control        

        self.nombre = tk.Label(self, text="")
        self.nombre.pack(pady=20, padx=1)
        self.artista = tk.Label(self, text="")
        self.artista.pack(pady=20, padx=1)
        self.genero = tk.Label(self, text="")
        self.genero.pack(pady=20, padx=1)
        self.hora_inicio = tk.Label(self, text="")
        self.hora_inicio.pack(pady=20, padx=1)
        self.hora_fin = tk.Label(self, text="")
        self.hora_fin.pack(pady=20, padx=1)
        self.descripcion = tk.Label(self, text="")
        self.descripcion.pack(pady=20, padx=1)
        
    

        self.boton_volver()
        self.boton_dejar_review()        

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
            #descripcion_evento = f"Descripcion: {evento.descripcion}"
            #self.descripcion["text"] = descripcion_evento
            self.control.evento = evento
         
    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.control.volver)
        self.boton_volver.pack(padx=10, pady=10)

    def boton_dejar_review(self):
         self.boton_dejar_review = tk.Button(self, text= 'dejar review', command=self.control.review)
         self.boton_dejar_review.pack(padx=10, pady=10)