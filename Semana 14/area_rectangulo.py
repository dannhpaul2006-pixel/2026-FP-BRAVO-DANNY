def calcular_area (base, altura):
    area = base * altura
    return area
b= float(input("Ingrese la base del rectangulo:"))
h= float(input("Ingrese la altura del rectangulo:"))
resultado = calcular_area (b, h)
print(f"El area del rectangulo es: {resultado}")

