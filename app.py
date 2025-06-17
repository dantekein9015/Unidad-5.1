# TP 5 - Listas - UTN A Distancia
# Alumno: [Tu Nombre]

# 1. Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("Múltiplos de 4:", multiplos_de_4)

# 2. Mostrar el penúltimo de una lista de 5 elementos que me gusten
cosas_que_me_gustan = ["pizza", "música", "series", "helado", "gatos"]
print("Penúltimo elemento:", cosas_que_me_gustan[-2])

# 3. Crear lista vacía, agregar 3 palabras con append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Lista con palabras:", lista_vacia)

# 4. Reemplazar segundo y último valor en lista de animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista de animales modificada:", animales)

# 5. Explicar programa (acá iría tu explicación en un comentario o word según pida el profe)

# 6. Lista con números del 10 al 30 (saltos de 5) y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("Dos primeros:", numeros[0], numeros[1])

# 7. Reemplazar los valores centrales de la lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mustang", "camaro"]
print("Autos modificados:", autos)

# 8. Crear lista con los dobles de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

# 9. Manipulación de lista anidada de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras modificada:", compras)

# 10. Crear lista anidada con tipos mixtos
lista_anidada = [
    15,                   # posición 0
    True,                # posición 1
    [25.5, 57.9, 30.6],  # posición 2 (sublista)
    False                # posición 3
]
print("Lista anidada:", lista_anidada)
