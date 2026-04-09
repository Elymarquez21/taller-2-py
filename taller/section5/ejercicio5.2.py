def calcular_promedio(numeros):
    if not numeros:
        return 0
    
    suma = 0
    for num in numeros:
        suma += num
    
    promedio = suma / len(numeros)
    return promedio

def probar_promedio():
    print("=== CALCULADORA DE PROMEDIOS ===")
    print("Ingrese números separados por comas")
    print("Ejemplo: 5,8,12,7,3")
    
    entrada = input("\nIngrese los números: ").strip()
    
    numeros = []
    for item in entrada.split(','):
        try:
            num = float(item.strip())
            numeros.append(num)
        except ValueError:
            print(f"'{item.strip()}' no es válido y será ignorado")
    
    if not numeros:
        print("No se ingresaron números válidos")
        return
    
    resultado = calcular_promedio(numeros)
    
    print(f"\nNúmeros ingresados: {numeros}")
    print(f"Cantidad de números: {len(numeros)}")
    print(f"Promedio: {resultado:.2f}")

probar_promedio()