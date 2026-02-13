# Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista: 
    print ("El numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range (2, 8):
    print (i)

mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in mi_lista_2:
    if i !="lunes":
       print (f"Feliz {i}!")

# While loop
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break

else:
    print("i es ahora mayor o igual a 5")

#Practica 2
#Dada la lista mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]
#Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluya
# Pista: usa los dos tipos loops while y for en el mismo programa para logarlo
# Resultado:
# Martes
# Miercoles 
# Jueves
# Viernes
# Martes
# Miercoles 
# Jueves
# Viernes
# Martes
# Miercoles 
# Jueves
# Viernes
j = 0
while j <4:
    j += 1
    if j == 4:
        continue