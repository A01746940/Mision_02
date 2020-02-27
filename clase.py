# Autor: Sharone Márquez, A01746940
# Calcular el procentaje entre hombre y mujeres de una clase

M= int(input("Teclea el número de mujeres inscritas: "))
H= int(input("Teclea el número de hombre inscritos: "))

NT= M+H
PM= M/NT*100
PH= H/NT*100

print("Total de inscritos: " , NT)
print("Porcentaje de mujeres: %.1f" % (PM),"%")
print("Porcentaje de hombres: %.1f" % (PH),"%")
