
tareas = []



try:
    with open("tareas.txt", 'r') as archivo:
        for linea in archivo:
            tareas.append(linea.strip())
except FileNotFoundError:
    pass

def mostrar_menu():
    print("=== Lista de tareas ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")


def main():
    flag = True
    while flag:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            if len(tareas) == 0:
                print("No hay tareas para mostrar.")
            else:
                print("Las tareas guardadas son: ")
                contador = 1
                for i in tareas:
                    print(contador, ".", i)
                    contador += 1
        # Agregar tareas
        elif opcion == "2":
            nueva_tarea = input("Escribe la tarea: ")
            
            if len(nueva_tarea) > 0:
                tareas.append(nueva_tarea)
                with open("tareas.txt", "a") as archivo:
                    archivo.write(nueva_tarea + "\n")
                print("Tarea agregada correctamente")
            else:
                print("No se puede agregar una tarea vacía.")
        # Salir
        elif opcion == "3":
            print("¡Hasta luego!")
            flag = False        
        else:
            print("Opcion aun no implementada.")







if __name__ == "__main__":
    main()







