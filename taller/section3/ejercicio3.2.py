def acumulador_numerico():
    print("=== ACUMULADOR NUMÉRICO ===")
    print("Ingrese números para sumar (0 para terminar)")
    print("-" * 40)
    
    suma_total = 0
    contador = 0
    
    while True:
        try:
            numero = float(input(f"Ingrese el número {contador + 1}: "))
            
            if numero == 0:
                break
            
            suma_total += numero
            contador += 1
            print(f"  → Suma parcial: {suma_total}")
            
        except ValueError:
            print("❌ Error: Ingrese un número válido")
    
    print("\n" + "=" * 40)
    print(f"RESUMEN FINAL:")
    print(f"• Números ingresados: {contador}")
    print(f"• Suma total: {suma_total}")
    print("=" * 40)

# Ejecutar
acumulador_numerico()