def tablas_multiplicar():
    print("=== GENERADOR DE TABLAS DE MULTIPLICAR ===")
    
    while True:
        print("\n" + "-" * 40)
        try:
            numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
            
            print(f"\n📊 TABLA DEL {numero}:")
            print("-" * 20)
            
            # Generar tabla del 1 al 10
            for i in range(1, 11):
                resultado = numero * i
                print(f"  {numero} x {i:2d} = {resultado:3d}")
            
            # Preguntar si desea continuar
            while True:
                continuar = input("\n¿Desea generar otra tabla? (s/n): ").lower()
                if continuar in ['s', 'n', 'si', 'no']:
                    break
                print("❌ Por favor, ingrese 's' para sí o 'n' para no")
            
            if continuar in ['n', 'no']:
                print("\n👋 ¡Hasta luego!")
                break
                
        except ValueError:
            print("❌ Error: Ingrese un número válido")

# Ejecutar
tablas_multiplicar()