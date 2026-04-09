def simulador_descuentos():
    print("=== SIMULADOR DE DESCUENTOS ===")
    print("Categorías de descuento:")
    print("A → 20% de descuento")
    print("B → 15% de descuento") 
    print("C → 10% de descuento")
    print("-" * 30)
    
    try:
        monto = float(input("Ingrese el monto de compra: $"))
        
        if monto <= 0:
            print("❌ El monto debe ser mayor a cero")
            return
        
        categoria = input("Ingrese su categoría (A, B o C): ").upper()
        
        # Aplicar descuento según categoría
        if categoria == 'A':
            descuento = monto * 0.20
        elif categoria == 'B':
            descuento = monto * 0.15
        elif categoria == 'C':
            descuento = monto * 0.10
        else:
            descuento = 0
            print(f"\n⚠️ Categoría '{categoria}' no válida. No se aplica descuento.")
        
        monto_final = monto - descuento
        
        print("\n=== RESUMEN DE COMPRA ===")
        print(f"Monto original: ${monto:.2f}")
        if descuento > 0:
            print(f"Descuento ({categoria}): ${descuento:.2f}")
        print(f"Total a pagar: ${monto_final:.2f}")
        print(f"¡Ahorraste: ${descuento:.2f}!")
        
    except ValueError:
        print("❌ Error: Ingrese un monto válido")

# Ejecutar
simulador_descuentos()