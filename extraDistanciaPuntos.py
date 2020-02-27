# Autor: Sharone Márquez, A01746940
# Calcular la distancia entre dos puntos

x1= int(input("Teclea la cordenada x1: "))
y1= int(input("Teclea la cordenada y1: "))
x2= int(input("Teclea la cordenada x2: "))
y2= int(input("Teclea la cordenada y2: "))

dist= (x2-x1)**2 + (y2-y1)**2
r=dist**.5

print("La distancia entre los dos puntos es: %.3f" % (r))
        