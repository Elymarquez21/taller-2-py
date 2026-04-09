def saludar(nombre, hora):
    if 5 <= hora <= 12:
        return f"Buenos días {nombre}"
    elif 13 <= hora <= 19:
        return f"Buenas tardes {nombre}"
    else:
        return f"Buenas noches {nombre}"

def probar_saludos():
    print("=== GENERADOR DE SALUDOS ===")
    
    nombre = input("Ingrese su nombre: ").strip().capitalize()
    
    try:
        hora = int(input("Ingrese la hora (0-23): "))
        
        if 0 <= hora <= 23:
            saludo = saludar(nombre, hora)
            print(f"\n{saludo}")
        else:
            print("La hora debe estar entre 0 y 23")
            
    except ValueError:
        print("Ingrese un número válido")

probar_saludos()