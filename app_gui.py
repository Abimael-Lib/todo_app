import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Lista de Tareas")



entrada_tarea = tk.Entry(ventana)
entrada_tarea.pack()


lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()



try:
    with open("tareas.txt", "r") as archivo:
        for linea in archivo:
            lista_tareas.insert(tk.END, linea.strip())
    




def agregar_tarea():
    texto = entrada_tarea.get()
    if len(texto) > 0:
        lista_tareas.insert(tk.END, texto)
        with open("tareas.txt", "a") as archivo:
            archivo.write(texto + "\n")
        entrada_tarea.delete(0, tk.END)
    else:
        return messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")
    pass


boton_agregar = tk.Button(ventana, text = "Agregar tarea", command = agregar_tarea)
boton_agregar.pack()







ventana.mainloop()




