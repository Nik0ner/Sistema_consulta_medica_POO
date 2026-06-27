
from Medico import Medico
from Paciente import Paciente

class Sistema:

    def __init__(self):

        self.medicos = [
            Medico("Lucas", "Médico general"),
            Medico("Javier", "Médico general")
        ]
        self.pacientes = []

    def registrar_paciente(self, nombre, edad):
        
        paciente = Paciente(nombre, edad)
        self.pacientes.append(paciente)

    def mostrar_pacientes(self):

        if len(self.pacientes) == 0:
            print("No hay pacientes registrados en este momento.")
        else:
            for i, Paciente in enumerate(self.pacientes):
                print(f"ID Paciente: {i} | Nombre: {Paciente.nombre} | Edad: {Paciente.edad} años")
        pass

    def mostrar_medicos(self):

        if len(self.medicos) == 0:
            print("No hay pacientes registrados en este momento.")
        else:
            for i, Medico in enumerate(self.medicos):
                print(f"ID Medico: {i} | {Medico.nombre} | {Medico.especialidad}")

    def asignar_paciente_a_medico(self, medico_elegido, paciente_elegido):

        medico_elegido.pacientes_asig.append(paciente_elegido)
        print(f"¡Listo! {paciente_elegido.nombre} asignado con {medico_elegido.nombre}")

    def gestionar_asignacion(self):
        print("--- Asignación de Hora ---")
        
        # --- VALIDACIÓN DEL MÉDICO ---
        self.mostrar_medicos()
        try:
            indice_med = int(input("Seleccione el número del médico: "))
            if indice_med < 0 or indice_med >= len(self.medicos):
                print("¡Error! Ese número de médico no existe en el sistema.")
                return
            
            medico_seleccionado = self.medicos[indice_med]
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")
            return

        # --- VALIDACIÓN DEL PACIENTE ---
        print("\n" + "-"*30)
        self.mostrar_pacientes()
        
        if len(self.pacientes) == 0:
            return
            
        try:
            indice_pac = int(input("Seleccione el número del paciente: "))
            if indice_pac < 0 or indice_pac >= len(self.pacientes):
                print("¡Error! Ese número de paciente no está en la fila.")
                return
                
            paciente_seleccionado = self.pacientes[indice_pac]
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")
            return

        self.asignar_paciente_a_medico(medico_seleccionado, paciente_seleccionado)