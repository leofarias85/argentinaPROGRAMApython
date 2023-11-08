
sueldos = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

promedioSueldo = sum(sueldos) / len(sueldos)

categoria = "Sueldo bajo" if promedioSueldo < 300 else "Sueldo normal" if promedioSueldo <= 900 else "Sueldo mejor de lo normal"

print(f"El sueldo promedio de Juan es de ${promedioSueldo}")
print(f"Categoría de sueldo de Juan: {categoria}")
