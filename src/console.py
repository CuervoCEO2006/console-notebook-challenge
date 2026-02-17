# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
import datetime



class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)




