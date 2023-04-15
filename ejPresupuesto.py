import math
# Calcular el promedio de gasto de ciertos meses

presupuesto_enero = 2000
presupuesto_febrero = 1590
presupuesto_marzo = 2890

promedio_presupuesto_trimestral = (presupuesto_enero + presupuesto_febrero + presupuesto_marzo / 3)

print(f"El promedio del presupuesto trimestral es: {math.trunc(promedio_presupuesto_trimestral)}")
