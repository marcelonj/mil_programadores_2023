import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tour Musical')
        self.geometry('800x600')
        self.frame_principal = MiFrame(self)
        self.frame_principal.pack(fill="both", pady=170)

class MiFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.mi_widget = self.tres_botones()
        
    def tres_botones(self):
        self.boton_eventos = tk.Button(self, text= 'Mostrar todos los eventos')
        self.boton_eventos.pack(pady=20)
        self.boton_buscar = tk.Button(self, text= 'Filtrar eventos')
        self.boton_buscar.pack(pady=20)
        self.boton_asistidos = tk.Button(self, text= 'Eventos asistidos')
        self.boton_asistidos.pack(pady=20)