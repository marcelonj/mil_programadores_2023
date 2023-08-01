from models.Review import Review
from models.Asistidos import Asistido

class ControladorReview:
    def __init__(self, app, array_reviews, array_asistidos):
        self.app = app
        self.review = array_reviews
        self.id = None
        self.asistidos = array_asistidos
        
    def volver(self):
        self.app.cambiar_frame(self.app.vista_detalle)

    def set_id(self, id):
        self.id = id
        print(self.id)

    def retornar_id(self):
        return self.id
    
    def publicar_review(self, comentario, animo):
        """ 
        Guarda el comentario y el animo en el fichero json correspondiente.
        """
        estado_animo = {
            0: "Unlike",
            1: "Like"
        }
        nueva_review = Review(len(self.review ) + 1, self.id, 1, "Bueno", comentario, estado_animo[animo])
        self.review.append(nueva_review)
        Review.save_reviews("data/Reviews.json", self.review)
       
        nuevo_asistido = Asistido(len(self.asistido) + 1, self.id_evento, self.id_usuario) 
        self.asistidos.append(nuevo_asistido)
        Asistido.save_asistidos("data/Asistidos.json", self.asistidos)
        


