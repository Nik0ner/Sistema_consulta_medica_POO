
import os 

from Sistema import Sistema


sistema = Sistema()

ejecutando = True


while ejecutando:

    sistema.menu_visual()
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":

        os.system("cls")
        print("--- REGISTRO DE PACIENTE ---")

        sistema.registrar_paciente()

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