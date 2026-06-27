
import os 

from Sistema import Sistema


sistema = Sistema()

ejecutando = True


while ejecutando:

    print("=== SISTEMA MÉDICO VIRTUAL (MODO POO) ===")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar pacientes en memoria")
    print("3. Asignar hora")
    print("4. Guardar y Salir")
    print("=========================================")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":

        os.system("cls")
        print("--- REGISTRO DE PACIENTE ---")

        nombre = str(input("Ingrese su nombre: "))
        try:
            edad = int(input("Ingrese su edad: "))
        except ValueError:
            edad = 0
            print("¡Edad inválida! Se registrará como 0.")

        sistema.registrar_paciente(nombre, edad)

        input("\nPresiona Enter para volver al menú...")
        os.system("cls")
        
    elif opcion == "2":

        os.system("cls")
        print("--- PACIENTES REGISTRADOS ---")

        sistema.mostrar_pacientes()    

        input("\nPresiona Enter para volver al menú...")
        os.system("cls")

    elif opcion == "3":

        os.system("cls")

        sistema.gestionar_asignacion()

        input("\nPresiona Enter para volver al menú...")
        os.system("cls")

        
    elif opcion == "4":

        os.system("cls")
        print("Guardando datos en el archivo...")
    
        print("¡Datos guardados con éxito en POO! ¡Adiós!")
        ejecutando = False

    else:
        print("Opción no válida. Intente de nuevo.")