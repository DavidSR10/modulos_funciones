'''
Actividad 1 - 25 puntos
Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

def sumar_numeros_cantidad(cantidad):
    suma_parcial = 0
    intentos = 0

    while intentos < cantidad:
        entrada = input(lambda: f"Ingrese el número {intentos + 1} (o 'mostrar suma' para ver la suma, 'q' para salir): ")

        if entrada.lower() == 'mostrar suma':
            print(f"La suma parcial hasta ahora es: {suma_parcial}")
        elif entrada.lower() == 'q':
            print(f"La suma de los números ingresados es: {suma_parcial}")
            break
        else:
            try:
                numero = float(entrada)
                suma_parcial += numero
                intentos += 1
            except ValueError:
                print("Por favor, ingrese un número válido.")

    else:
        print(f"Se han ingresado {cantidad} números. La suma final es: {suma_parcial}")

# Solicitar al usuario la cantidad de números que quiere sumar
cantidad_a_sumar = int(input("Ingrese la cantidad de números que desea sumar: "))
sumar_numeros_cantidad(cantidad_a_sumar)






