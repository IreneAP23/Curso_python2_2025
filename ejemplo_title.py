
import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo("saludos desde tkinter")

def mostrar_saludo():
    nombre= entry_nombre.get()
    if nombre:
        messagebox.showinfo("saludo personalizado", f"Hola, {nombre}")
    else:
        messagebox.showwarning("Advertencia", "por favor introduce tu nombre")


root= tk.Tk()
root.title("Entrada de texo y saludo")
root.geometry("400x150")

label_pregunta=tk.Label(root, text="Introduce tu nombre : ", font=("Arial",12))
label_pregunta.pack(pady=10)

entry_nombre= tk.Entry(root, width=30, font=("Arial",12))
entry_nombre.pack(pady=5)

boton_saludar=tk.Button(root, text="saludar", command=mostrar_saludo, font=("Arial,12"))
boton_saludar.pack(pady=10)

#crear una etiqueta
#label = tk.Label(root, text="Bienvenido a mi app", font=("Arial",14),fg="blue")
#label.pack(pady=20)

#Crear un boton
#button=tk.Button(root, text="Haz click aca", command=saludar, font=("Arial",12),bg="green",fg="white")
#button.pack()



root.mainloop()