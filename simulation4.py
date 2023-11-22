'''
Actividad 4
Crea un módulo con las siguientes clases
Mesa
Silla
Lampara
las tres clases tiene como atributo color y precio.
En otro módulo importa únicamente la clase Silla y crea dos sillas. Una de color azul y otra roja con precios de 9.95

algoritmo funciona:5 puntos
algoritmo utiliza características de POO : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica enumeradores o similar para Color : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos
'''

from enum import Enum

class Color(Enum):
    AZUL = "azul"
    ROJO = "rojo"
    VERDE = "verde"
    AMARILLO = "amarillo"
    # Agrega más colores según sea necesario

class Mueble:
    def __init__(self, tipo, color, precio):
        self.tipo = tipo
        if not isinstance(color, Color):
            raise ValueError(f"Error: Color no válido para {tipo}.")
        self.color = color
        try:
            self.precio = float(precio)
        except ValueError:
            raise ValueError(f"Error: El precio debe ser un número válido para {tipo}.")

class Mesa(Mueble):
    pass

class Silla(Mueble):
    pass

class Lampara(Mueble):
    pass

def crear_muebles_automaticos():
    muebles = []

    # Crear automáticamente una silla azul y otra roja con precio de 9.95
    silla_azul = Silla(tipo="silla", color=Color.AZUL, precio=9.95)
    silla_roja = Silla(tipo="silla", color=Color.ROJO, precio=9.95)

    muebles.extend([silla_azul, silla_roja])

    print("Muebles creados automáticamente:")
    for mueble in muebles:
        print(f"{mueble.tipo.capitalize()} - Color: {mueble.color.value}, Precio: {mueble.precio}")

    return muebles

# Llamar a la función que crea y muestra información de los muebles automáticamente
muebles_automaticos = crear_muebles_automaticos()

