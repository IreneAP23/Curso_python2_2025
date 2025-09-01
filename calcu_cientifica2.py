#Diseño de calculadora cientifica con TK inter.
#Curso python 2
#Irene Aguilar Peña


import tkinter as tk
import math

base_exp= None
modo_exp= False
estado= {"base_exp":None, "modo_exp":False}

def click_boton(caracter):
    current_text = display.get()
    if caracter == "=":
        try:
            if estado["modo_exp"]:
                exponente=float(current_text)
                result=math.pow(estado["base_exp"],exponente)
                estado["modo_exp"]=False
                estado["base_exp"]=None
            else:
                result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "ERROR")
    elif caracter == "C":
        display.delete(0, tk.END)
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
        estado["base_exp"] = float(display.get())
        estado["modo_exp"]=True
        display.delete(0, tk.END)
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

# Interfaz
root = tk.Tk()
root.title("Calculadora científica")
root.geometry("400x400")

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

display = tk.Entry(root, font=("Arial", 20, "bold"), bd=6, justify="right", bg="lightsteelblue")
display.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW, padx=5, pady=5)

botones = [
    ("log", log), ("In", ln), ("√", raiz), ("exp", exp),
    ("sen", sen), ("cos", cos), ("tan", tan), ("%", lambda: click_boton("%")),
    ("7", lambda: click_boton("7")), ("8", lambda: click_boton("8")), ("9", lambda: click_boton("9")), ("/", lambda: click_boton("/")),
    ("4", lambda: click_boton("4")), ("5", lambda: click_boton("5")), ("6", lambda: click_boton("6")), ("*", lambda: click_boton("*")),
    ("1", lambda: click_boton("1")), ("2", lambda: click_boton("2")), ("3", lambda: click_boton("3")), ("-", lambda: click_boton("-")),
    ("0", lambda: click_boton("0")), (".", lambda: click_boton(".")), ("=", lambda: click_boton("=")), ("+", lambda: click_boton("+")),
    ("(", lambda: click_boton("(")), (")", lambda: click_boton(")")), ("C", lambda: click_boton("C"))
]

row_num = 1
col_num = 0
for texto, comando in botones:
    button = tk.Button(root, text=texto, font=("Arial", 17), command=comando, bg="lightgray")
    button.grid(row=row_num, column=col_num, sticky=tk.NSEW, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()