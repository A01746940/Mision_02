# Autor: Sharone Márquez, A01746940
# Calcular cuantas galletas se quieren elaborar

vg= int(input("¿Cuántas galletas quiere elaborar?: "))
TazasA= 1.5
TazasM= 1
TazasH= 2.75

ta= (vg*TazasA)/48
tm= (vg*TazasM)/48
th= (vg*TazasH)/48

print("Tazas de azúcar: " , ta)
print("Tazas de mantequilla: %.1f" % (tm))
print("Tazas de harina: %.1f" % (th))

