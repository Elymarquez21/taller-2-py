def eliminar_duplicados():
    print("=== ELIMINADOR DE DUPLICADOS ===")
    print("Ingrese 10 números (pueden repetirse)")
    print("-" * 40)
    
    numeros = []
    
    # Ingresar 10 números
    for i in range(10):
        while True:
            try:
                num = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("❌ Error: Ingrese un número válido")
    
    print(f"\n📋 Lista original: {numeros}")
    
    # Eliminar duplicados usando lista auxiliar
    numeros_sin_duplicados = []
    
    for num in numeros:
        # Verificar si el número ya está en la lista auxiliar
        existe = False
        for elemento in numeros_sin_duplicados:
            if elemento == num:
                existe = True
                break
        
        if not existe:
            numeros_sin_duplicados.append(num)
    
    print(f"📋 Lista sin duplicados: {numeros_sin_duplicados}")
    
    # Mostrar estadísticas
    print("\n📊 ESTADÍSTICAS:")
    print(f"• Total original: {len(numeros)} números")
    print(f"• Números únicos: {len(numeros_sin_duplicados)} números")
    print(f"• Duplicados eliminados: {len(numeros) - len(numeros_sin_duplicados)} números")
    
    # Mostrar frecuencias
    print("\n📈 FRECUENCIAS:")
    for num in numeros_sin_duplicados:
        frecuencia = 0
        for elemento in numeros:
            if elemento == num:
                frecuencia += 1
        if frecuencia > 1:
            print(f"  • {num} aparece {frecuencia} veces")

# Ejecutar
eliminar_duplicados()