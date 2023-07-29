import tkinter as tk


class DetalleReview(tk.Frame): 
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.control = control
        self.detalles = FrameDetalle(self, control=self.control)
        self.detalles.place(x=0, y=0, width=250, height=600)
             
class FrameDetalle(tk.Frame):
    def __init__(self, master = None, control = None):
        super().__init__(master)
        self.master = master
        self.control = control        

        self.id = tk.Label(self, text="")
        self.id.pack(pady=20, padx=1)
        self.comentario = tk.Label(self, text="")
        self.comentario.pack(pady=20, padx=1)
        self.animo = tk.Label(self, text="")
        self.animo.pack(pady=20, padx=1)
        
        self.boton_volver()        

    def mostrar_review(self, review, evento):
            nombre_evento = f"{evento.nombre}"
            self.nombre["text"] = nombre_evento
            comentario_evento = f"{review.comentario}"
            self.comentario["text"] = comentario_evento
            animo_evento = f"Animo: {review.animo}"
            self.animo["text"] = animo_evento
            
         
    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.control.volver)
        self.boton_volver.pack(padx=10, pady=10)