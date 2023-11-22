'''
Actividad 2
En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

import datetime

def obtener_fecha_ingresada():
    try:
        dia = int(input("Ingrese el día (1-31): "))
        mes = int(input("Ingrese el mes (1-12): "))
        return datetime.datetime(datetime.datetime.now().year, mes, dia)
    except ValueError:
        print("Ingrese una fecha válida.")
        return obtener_fecha_ingresada()

def calcular_descuento(unidades, precio, fecha):
    return unidades * precio * 0.05 if fecha.day < 15 else 0

def calcular_total_factura():
    try:
        unidades = float(input("Ingrese la cantidad de unidades: "))
        precio = float(input("Ingrese el precio por unidad: "))

        fecha_actual = datetime.datetime.now()
        fecha_ingresada = obtener_fecha_ingresada()

        descuento = calcular_descuento(unidades, precio, fecha_ingresada)
        subtotal = unidades * precio - descuento

        print(f"Subtotal: {subtotal:.2f}")
        print(f"Descuento aplicado: {descuento:.2f}")
        print(f"Total de la factura: {subtotal:.2f}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

calcular_total_factura()



