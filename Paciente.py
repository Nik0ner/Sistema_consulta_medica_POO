


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.prioridad = False
        self.rango = ""

    def es_prioritario(self):
        if self.edad >= 65:
            self.prioridad = True
            self.rango = "Adulto mayor"
            
        elif self.edad <= 1:
            self.prioridad = True
            self.rango = "Lactante de meses"

        else:
            self.prioridad = False
            self.rango = "Adulto"
     
        return self.prioridad

