import tkinter as tk

root= tk.Tk()
root.title("ejemplos de frames")
root.geometry("400x250")

#crear un frame superior

frame_superior= tk.Frame(root, borderwidth=2, relief="groove", bg="lightblue")
frame_superior.pack(pady=10,padx=10, fill="x")

label_titulo= tk.Label(frame_superior,text="Controles superiores", font=("Arial",16),bg="lightblue")
label_titulo.pack(pady=5)

boton_a=tk.Button(frame_superior, text="botton A")
boton_a.pack(side="left", padx=10, pady=5)

boton_b=tk.Button(frame_superior, text="botton B")
boton_b.pack(side="right", padx=10, pady=5)

#frame abajo
frame_inferior= tk.Frame(root, borderwidth=2, relief="groove", bg="lightgreen")
frame_inferior.pack(pady=20,padx=20, fill="x")

label_info= tk.Label(frame_inferior,text="Controles inferiores", font=("Arial",16),bg="lightgreen")
label_info.pack(pady=5)

boton_c=tk.Button(frame_inferior, text="botton C")
boton_c.pack(side="left", padx=10, pady=5)

boton_d=tk.Button(frame_inferior, text="botton D")
boton_d.pack(side="right", padx=10, pady=5)




root.mainloop()

