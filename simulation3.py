'''
Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

def mostrar_numeros(numero_inicial, numero_final, filtrar_pares=True):
    try:
        # Asegurarse de que el número inicial sea menor o igual al número final
        if numero_inicial > numero_final:
            numero_inicial, numero_final = numero_final, numero_inicial
            print("Los números se intercambiaron para que el número inicial sea menor que el número final.")

        # Generar la lista de números pares o impares según la preferencia del usuario
        numeros_filtrados = [num for num in range(numero_inicial, numero_final + 1) if (num % 2 == 0) == filtrar_pares]

        # Mostrar la lista de números
        tipo_numero = "pares" if filtrar_pares else "impares"
        print(f"Números {tipo_numero} entre {numero_inicial} y {numero_final}: {numeros_filtrados}")

    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

# Solicitar al usuario que ingrese los números iniciales y finales, y su preferencia (pares o impares)
try:
    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))
    filtrar_pares = input("¿Quiere ver los números pares? (Sí/No): ").lower() == 'si'
    mostrar_numeros(inicio, fin, filtrar_pares)
except ValueError:
    print("Por favor, ingrese números enteros válidos.")

