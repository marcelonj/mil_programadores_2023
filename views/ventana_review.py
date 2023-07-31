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

        self.seccion_comentario()
        self.boton_publicar()
        self.boton_volver()  

        self.mensaje = tk.Label(self, text="") 
        self.mensaje.grid(row=4, column=0, columnspan=2)     

    def cargar_review(self, review, evento):
            nombre_evento = f"{evento.nombre}"
            self.nombre["text"] = nombre_evento
            comentario_evento = f"{review.comentario}"
            self.comentario["text"] = comentario_evento
            animo_evento = f"Animo: {review.animo}"
            self.animo["text"] = animo_evento
            
         
    def boton_volver(self):
        self.boton_volver = tk.Button(self, text= 'volver', command=self.volver)
        self.boton_volver.grid(row=3, column=1)

    def boton_publicar(self):       
        self.boton_publicar = tk.Button(self, text= 'publicar', command=self.publicar_review)
        self.boton_publicar.grid(row=3, column=0)

    def seccion_comentario(self):
        self.label_comentario = tk.Label(self, text="Deja tu comentario")
        self.label_comentario.grid(row=0, column=0)
        self.comentario = tk.Text(self, width=30, height=10)
        self.comentario.insert(tk.END, "Deje su comentario...")
        self.comentario.grid(row=1, column=0, columnspan=2)
        self.animo = tk.IntVar(value=1)
        self.me_gusta = tk.Radiobutton(self, text="Me gustó", variable=self.animo, value=1)
        self.me_gusta.grid(row=2, column=0)
        self.no_me_gusta = tk.Radiobutton(self, text="No me gustó", variable=self.animo, value=0)
        self.no_me_gusta.grid(row=2, column=1)

    def publicar_review(self):
        animo = self.animo.get()
        comentario = self.comentario.get("1.0", tk.END)
        self.control.publicar_review(comentario, animo)
        self.mensaje.config(text="se publicó tu review")

    def volver(self):
        self.animo = tk.IntVar(value=1)
        self.comentario.insert(tk.END, "Deje su comentario...")
        self.control.volver()        