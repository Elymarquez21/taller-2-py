def clasificar_edad():
    print("=== CLASIFICADOR DE EDADES ===")
    
    try:
        edad = int(input("Ingrese su edad: "))
        
        if edad < 0:
            print("❌ Edad no válida")
        elif edad <= 12:
            print(f"\n{edad} años → NIÑO (0-12 años)")
        elif edad <= 17:
            print(f"\n{edad} años → ADOLESCENTE (13-17 años)")
        elif edad <= 64:
            print(f"\n{edad} años → ADULTO (18-64 años)")
        else:
            print(f"\n{edad} años → ADULTO MAYOR (65 años o más)")
            
    except ValueError:
        print("❌ Error: Ingrese un número válido")

# Ejecutar
clasificar_edad()