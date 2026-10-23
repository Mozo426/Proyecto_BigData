import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

dias = ["Domingo", "Sabado", "Jueves", "Viernes"]
promedios = [21.41, 20.44, 17.76, 17.15]

plt.figure(figsize=(8, 5))
plt.bar(dias, promedios)
plt.title("promedio de la cuenta por dia")
plt.xlabel("Dia de la semana")
plt.ylabel("Promedio de la cuenta")
plt.tight_layout()

plt.savefig("/home/matheus/Proyecto_BigData/grafica_cuentas.png")

print("Grafica guardada correctamente.")
