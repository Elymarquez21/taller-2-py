def registrar_usuario():
    print("=== REGISTRO DE USUARIO ===")
    
    # Solicitar nombre
    nombre = input("Ingrese su nombre: ")
    
    # Solicitar y validar edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                break
            else:
                print("Error: La edad debe ser un número positivo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
    
    # Solicitar ciudad
    ciudad = input("Ingrese su ciudad de residencia: ")
    
    # Mostrar mensaje personalizado
    print(f"Hola {nombre}; tienes {edad} años y vives en {ciudad}.")

# Ejecutar el programa
if __name__ == "__main__":
    registrar_usuario()