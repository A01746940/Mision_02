# Autor: Sharone Márquez, A01746940
# Calcula la velocidad de un viaje

V= int(input("Teclea la velocidad del auto en km/h: "))
t1= 6
t2= 3.5
dist= 485

distancia1= V*t1
distancia2= V*t2
tiempo= dist/V

print("Distancia recorrida en 6 hrs: ", distancia1)
print("Distancia recorrida en 3.5 hrs: ", distancia2)
print("Tiempo para recorrer 485 km: %.1f" % (tiempo))
