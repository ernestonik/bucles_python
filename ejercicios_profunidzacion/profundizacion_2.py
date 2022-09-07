# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from http.client import MULTIPLE_CHOICES


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
numero1 = int(input('Ingrese el primer número\n'))
numero2 = int(input('Ingrese el segundo número\n'))
print(''' Ingresa la operacion:
(+)  Suma 
(-)  Resta 
(*)  Multiplicación 
(/)  División 
(**) Exponente/Potencia 
(x)  Detener''')
operacion = str(input ())

while operacion =="+":
    suma = numero1 + numero2
    print ("El resultado de su suma es; ", suma)
    if operacion == "-":
        resta = numero1 - numero2
        print ("El resultado de su resta es; ", resta)
    if operacion == "*":
         Multiplicacion = numero1 * numero2
         print ("El resultado de su multiplicacion es; ", Multiplicacion)
    if operacion == "/":
         division = numero1 / numero2
         print ("El resultado de su division es; ", division)
    if operacion == "**":
         expo = numero1 ** numero2
         print ("El resultado de su operaicon es; ", expo)           
    if operacion == "x":
        print("FIN")
        break