def analizador_estadistico():
    print("=== ANALIZADOR ESTADÍSTICO ===")
    print("Ingrese una lista de números separados por comas")
    print("Ejemplo: 5,8,12,3.5,7,1")
    
    entrada = input("\nIngrese los números: ").strip()
    
    numeros = []
    for item in entrada.split(','):
        try:
            num = float(item.strip())
            numeros.append(num)
        except ValueError:
            print(f"'{item.strip()}' no es un número válido y será ignorado")
    
    if not numeros:
        print("No se ingresaron números válidos")
        return
    
    print(f"\nANALIZANDO {len(numeros)} NÚMEROS:")
    print(f"   {numeros}")
    print("\n" + "=" * 40)
    
    suma = 0
    maximo = numeros[0]
    minimo = numeros[0]
    
    for num in numeros:
        suma += num
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    
    promedio = suma / len(numeros)
    
    print("RESULTADOS:")
    print(f"   • Suma total:     {suma:.2f}")
    print(f"   • Promedio:       {promedio:.2f}")
    print(f"   • Valor máximo:   {maximo:.2f}")
    print(f"   • Valor mínimo:   {minimo:.2f}")
    
    print("\nDETALLE ADICIONAL:")
    print(f"   • Cantidad de números: {len(numeros)}")
    
    numeros_ordenados = sorted(numeros)
    print(f"   • Números ordenados: {numeros_ordenados}")
    
    rango = maximo - minimo
    print(f"   • Rango: {rango:.2f}")

analizador_estadistico()