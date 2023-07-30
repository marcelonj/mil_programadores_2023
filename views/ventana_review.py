import tkinter as tk


class DejarReview(tk.Frame): 
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.control = control
        self.detalles = FrameFormulario(self, control=self.control)
        self.detalles.place(x=0, y=0, width=250, height=600)
             
class FrameFormulario(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.master = master
        self.control = control        

        self.comentario = tk.Label(self, text="comentario")
        self.comentario.pack(pady=20, padx=1)
        self.animo = tk.Label(self, text="animo")
        self.animo.pack(pady=20, padx=1)
        self.boton_publicar()
        self.boton_volver()        

    def cargar_review(self, review, evento):
            nombre_evento = f"{evento.nombre}"
            self.nombre["text"] = nombre_evento
            comentario_evento = f"{review.comentario}"
            self.comentario["text"] = comentario_evento
            animo_evento = f"Animo: {review.animo}"
            self.animo["text"] = animo_evento
            
         
    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.control.volver)
        self.boton_volver.pack(padx=10, pady=10)

    def boton_publicar(self):
        self.boton_publicar = tk.Button(self, text= 'publicar', command=self.control.volver)
        self.boton_publicar.pack(padx=10, pady=10)