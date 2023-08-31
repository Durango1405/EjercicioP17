import math  # Importamos el módulo math para tener acceso a funciones matemáticas
# Leer el radio del círculo 
radio = float(input("Ingrese el radio del círculo: "))
# Calcular el área del círculo 
area = math.pi * radio ** 2 #con la función math, podemos operar con pi
# Calcular la longitud de la circunferencia 
longitud_circunferencia = 2 * math.pi * radio
# Mostrar los resultados
print(f"El área del círculo con radio {radio} es: {area}")
print(f"La longitud de la circunferencia con radio {radio} es: {longitud_circunferencia}")
