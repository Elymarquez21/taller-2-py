def calculadora_mejorada():
    while True:
        print("\n=== CALCULADORA MEJORADA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("\nSeleccione una operación (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion not in ['1', '2', '3', '4']:
            print("❌ Opción no válida")
            continue
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = num1 + num2
                operacion = "+"
            elif opcion == '2':
                resultado = num1 - num2
                operacion = "-"
            elif opcion == '3':
                resultado = num1 * num2
                operacion = "*"
            else:  # opcion == '4'
                if num2 == 0:
                    print("❌ Error: No se puede dividir por cero")
                    continue
                resultado = num1 / num2
                operacion = "/"
            
            print(f"\n{num1} {operacion} {num2} = {resultado}")
            
        except ValueError:
            print("❌ Error: Ingrese números válidos")

# Ejecutar
calculadora_mejorada()