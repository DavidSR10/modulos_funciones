#vamps a utilixar el contenido del modulo ejemplo2

import ejemplo2
from ejemplo3 import Pais


#uso de variables
ejemplo2.alumnos.update({"Luis":"dam"})
print(ejemplo2.alumnos)

#uso de funciones
ejemplo2.calcular_cubo()

#uso de clase
producto1=ejemplo2.Producto("camisa",50)

france=Pais("Francia","Paris")
