# La Lista
# Es una colección ordenada y modificable. Permite miembros duplicados
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(type(thislist))
print(thislist[0])
print(thislist[-1])

# Rango de índices
print("=== Rango de índices ===")
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
print(thislist2[:4])
print(thislist2[2:])
print(thislist2[-4:-1])

# Para determinar si un elemento existe dentro de la lista
if "apple" in thislist2:
    print("Yes, 'apple' is in the fruits list")

# Cambiar el elemento de una LISTA
thislist2[1] = "blackcurrant"
print(thislist2)

# Cambiar un Rango de valores
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)

#Insertar Elementos
thislist2.insert(2, "Papaya")
print(thislist2)

# Agregar elementos al final de la lista
thislist2.append("Palta")
print(thislist2)

# Ampliar la lista
print("=== Ampliar la Lista ====")
thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
print(thislist3)

# Eliminar elementos especificado, Si hay más de un elemento con el valor especificado, el remove() método elimina la primera aparición
thislist3.remove("banana")
print(thislist3)

# El pop()método elimina el índice especificado.
# Si no especifica el índice, el pop()método elimina el último elemento.
thislist3.pop(1)
print(thislist3)

# La del palabra clave también elimina el índice especificado:
#La del palabra clave también puede eliminar la lista por completo.
del thislist3[0]
print(thislist3)

# El clear() método vacía la lista.
thislist3.clear()
print(thislist3)

# Recorrer una lista con el BUCLE FOR
# ITERACIONES
print("=== Bucle FOR ===")
frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
for fruta in frutas:
  print(fruta)

print("=====")
for indice in range(len(frutas)):
   print(frutas[indice])

print("==== bucle WHILE =======")
i = 0
while i < len(frutas):
   print(frutas[i])
   i = i + 1

# Comprensión de listas
# CONDICIONALES
# A partir de una lista de frutas, desea una nueva lista, que contenga solo las frutas con la letra "a" en el nombre.
newlist = [x.upper() for x in frutas if "a" in x]
print(newlist)

# Ordenar Listas
frutas.sort() # ordenar alfanuméricamente
print(frutas)

numeros = [100, 50, 65, 82, 23]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

#Invertir el de la lista
frutas.reverse()
print(frutas)

#Copiar una lista
print("=== Copiar una lista ===")
copia = frutas.copy()
print(copia)