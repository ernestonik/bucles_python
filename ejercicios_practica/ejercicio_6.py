# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
numeros = range(inicio, fin + 1)
cantidad_numeros_positivos = 0  # Inicializo el contador en 0

for i in range(inicio, fin):
    print (inicio)
    inicio += 1
    if i == fin - 1:
        print (fin)
   
cantidad_numeros_positivos = 0
cantidad_numeros_negativos = 0
numeros_posi =[]
numeros_nega =[]

for numero in numeros:
    if numero >= 0:
        numeros_posi.append(numero)
    elif numero < 0:
        numeros_nega.append(numero)

print ("Positivos", numeros_posi, "en total son", len(numeros_posi))
print ("Negativos", numeros_nega, "en total son", len(numeros_nega))

# for ... in range(....)

# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
