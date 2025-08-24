import tkinter as tk
import math

def click_boton(caracter):
    current_text= display.get()

    if caracter == "=":
        try:
            result= eval(current_text)
            display.delete(0,tk.END)
            display.insert(tk.END, str(result))
        
        except Exception:
            display.delete(0,tk.END)
            display.insert(tk.END, "ERROR")

    elif caracter == "C":
        display.delete(0,tk.END)
    else:
        display.insert(tk.END, caracter)

# Funciones científicas
def sen():
    try:
        valor = float(display.get())
        resultado = math.sin(math.radians(valor))
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cos():
    try:
        valor = float(display.get())
        resultado = math.cos(math.radians(valor))
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def tan():
    try:
        valor = float(display.get())
        resultado = math.tan(math.radians(valor))
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def log():
    try:
        numero = float(display.get())
        resultado = math.log10(numero)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def exp():
    try:
        numero = float(display.get())
        resultado = math.exp(numero)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def ln():
    try:
        numero = float(display.get())
        resultado = math.log(numero)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def raiz():
    try:
        numero = float(display.get())
        resultado = math.sqrt(numero)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root=tk.Tk()
root.title("Calculadora científica")
root.geometry("350x400")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

display= tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
display.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW, padx=5,pady=5)

botones= ["log", "In","raiz","exp",
          "sen","cos","tan","%",
          "7","8","9", "/",
          "4","5","6","*",
          "1","2","3","-",
          "0",".","=","+",
          "(", ")","C"]

row_num=1
col_num=0

for boton_texto in botones:
    if boton_texto== "=":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: click_boton(b))
    if boton_texto== "(":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: click_boton(b))
    if boton_texto== ")":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: click_boton(b))
    if boton_texto=="sen":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto:sen)
    if boton_texto=="cos":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: cos)
    if boton_texto=="tan":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: tan)
    if boton_texto=="log":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: log)
    if boton_texto=="In":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: ln)
    if boton_texto=="exp":
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: exp)
    elif boton_texto=="C":
        button=tk.Button(root, text=boton_texto, font=("Arial",16) , command=lambda b=boton_texto: click_boton(b))
    else:
        button=tk.Button(root, text=boton_texto, font=("Arial",16), command=lambda b=boton_texto: click_boton(b))
    button.grid(row=row_num,column=col_num,sticky=tk.NSEW, padx=5,pady=5)
    col_num+=1
    if col_num >3:
        col_num=0
        row_num+=1


root.mainloop()

