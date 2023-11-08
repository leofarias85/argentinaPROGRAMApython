
sueldos_por_mes = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

def calcular_sueldo_promedio(sueldos):
    return sum(sueldos) / len(sueldos)

def cambiar_sueldo_mes(sueldos, mes, nuevo_sueldo):
    sueldos[mes - 1] = nuevo_sueldo

while True:
    sueldo_promedio = calcular_sueldo_promedio(sueldos_por_mes)
    print(f"El sueldo promedio de Juan es de ${sueldo_promedio:.2f}")

    respuesta = input("¿Desea cambiar el sueldo de algún mes? (si/no): ").lower()
    
    if respuesta == "si":
        mes = int(input("Ingrese el número del mes que desea cambiar (1-12): "))
        nuevo_sueldo = int(input(f"Ingrese el nuevo sueldo para el mes {mes}: "))
        cambiar_sueldo_mes(sueldos_por_mes, mes, nuevo_sueldo)
    elif respuesta == "no":
        print("Entonces el código ha terminado.")
        break
    else:
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
