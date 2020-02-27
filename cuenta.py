# Autor: Sharone Márquez, A01746940
# Calcular el costo total de una de una comida en un restaurante

T= int(input("Teclea el costo de su comida: "))

I= T*.16
P= T*.13

TP= T+I+P

print("Propina: ","$"," %.2f" % (P))
print("IVA: ","$"," %.2f" % (I))
print("Total a pagar: ","$"," %.2f" % (TP))
