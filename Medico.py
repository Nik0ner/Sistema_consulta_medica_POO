


class Medico: 

    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes_asig = []


    def atender_paciente(self, Paciente):
        self.pacientes_asig.append(Paciente)

    
