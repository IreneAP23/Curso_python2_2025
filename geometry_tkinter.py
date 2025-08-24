
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title("Utilizando el pack Geometry")
sytle=ttk.Style()
sytle.theme_use("clam")
sytle.configure("TFrame", background="green")

root.configure(bg="lightgreen")
root.geometry("400x300")

background_frame= ttk.Frame(root, style="TFrame")
background_frame.pack(fill="both", expand=True)

btn1=tk.Button(background_frame, text="botton 1 (superior)")
btn1.pack(pady=10)

btn2=tk.Button(background_frame, text="botton 2 (Izquierda)")
btn2.pack(side=tk.LEFT, padx=10, pady=10)

btn3=tk.Button(background_frame, text="botton 3 (Derecha)")
btn3.pack(side=tk.RIGHT, padx=10, pady=10)


label_fill= tk.Label(background_frame, text="Esta etiqueta esta llenando un espacio", bg="lightgray")
label_fill.pack(side=tk.TOP, expand=True, padx=10, pady=10)

btn4=tk.Button(background_frame, text="botton 4 (abajo)")
btn4.pack(side=tk.BOTTOM, padx=10, pady=10)


root.mainloop()