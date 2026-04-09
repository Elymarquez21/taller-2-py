def convertidor_unidades():
    while True:
        print("\n=== CONVERTIDOR DE UNIDADES ===")
        print("1. Celsius a Fahrenheit")
        print("2. Kilómetros a Millas")
        print("3. Kilogramos a Libras")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '4':
            print("¡Hasta luego!")
            break
        
        if opcion not in ['1', '2', '3']:
            print("❌ Opción no válida. Intente nuevamente.")
            continue
        
        try:
            valor = float(input("Ingrese el valor a convertir: "))
            
            if opcion == '1':
                resultado = (valor * 9/5) + 32
                print(f"\n{valor:.2f}°C = {resultado:.2f}°F")
            elif opcion == '2':
                resultado = valor * 0.621371
                print(f"\n{valor:.2f} km = {resultado:.2f} millas")
            elif opcion == '3':
                resultado = valor * 2.20462
                print(f"\n{valor:.2f} kg = {resultado:.2f} libras")
                
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido")

# Ejecutar
convertidor_unidades()