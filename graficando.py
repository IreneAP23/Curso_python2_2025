#graficos 
import matplotlib.pyplot as plt
import numpy as np

# x=np.linspace(0,10,100)
# #print(x)
# y=np.sin(x)
# #print(y)

# plt.figure(figsize=(8,4))
# plt.plot(x,y, label="Función seno", color="blue", linestyle="--")
# plt.title("Gráfico de la función seno")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.grid(True)
# plt.legend()
# plt.show()

# x=np.arange(0,5,0.1)
# y1=x
# y2=x**2
# y3=x**3

# plt.figure(figsize=(10,6))
# plt.plot(x,y1, label="y = x", color="red")
# plt.plot(x,y2, label="y = x**2", color="blue", linestyle=":")
# plt.plot(x,y3, label="y = x**3", color="green", linewidth=2)
# plt.title("Gráficos de lineas")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.grid(True)
# plt.legend()
# plt.show()

# np.random.seed(46)
# num_points= 50

# x_scatter= np.random.rand(num_points*10)
# y_scatter= 2 * x_scatter + np.random.rand(num_points)*5 + 3

# plt.figure(figsize=(7,5))
# plt.scatter(x_scatter,y_scatter, alpha=0.7, s=50, edgecolors="black")
# plt.title("Gráfico de dispersión")
# plt.xlabel("Variable independiente")
# plt.ylabel("Variable dependiente")
# plt.grid(True)
# plt.show()

# data_hist=np.random.rand(1000) *15 + 100
# plt.figure(figsize=(7,5))
# plt.hist(data_hist, bins=30, color="skyblue", edgecolor="black", alpha=0.8)
# plt.title("Histograma de datos normales")
# plt.xlabel("Valores")
# plt.ylabel("Frecuencia")
# plt.grid(axis="y", alpha=0.75)
# plt.show()

#grafico de barras

categorias=["A","B","C","D","E"]
valores=[23,45,56,12,39]

plt.figure(figsize=(7,5))
plt.bar(categorias,valores,color="royalblue",edgecolor="k")
plt.title("Gráfico de barras de categorías")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.ylim(0,60)
plt.show()

