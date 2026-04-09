def calculadora():
    print("=== CALCULADORA SIMPLE ===")
    print("Operaciones disponibles:")
    print("+ : Suma")
    print("- : Resta")
    print("* : Multiplicación")
    print("/ : División")
    print("==========================")
    
    try:
        # Solicitar los números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        # Solicitar la operación
        operacion = input("Ingrese la operación (+, -, *, /): ")
        
        # Realizar la operación correspondiente
        if operacion == "+":
            resultado = num1 + num2
            print(f"\n{num1} + {num2} = {resultado}")
            
        elif operacion == "-":
            resultado = num1 - num2
            print(f"\n{num1} - {num2} = {resultado}")
            
        elif operacion == "*":
            resultado = num1 * num2
            print(f"\n{num1} * {num2} = {resultado}")
            
        elif operacion == "/":
            # Validar división por cero
            if num2 == 0:
                print("\n❌ Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"\n{num1} / {num2} = {resultado}")
                
        else:
            print(f"\n❌ Error: La operación '{operacion}' no es válida.")
            
    except ValueError:
        print("\n❌ Error: Por favor ingrese números válidos.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
    
    # Preguntar si quiere hacer otro cálculo
    while True:
        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar == 's':
            print("\n" + "="*30)
            calculadora()
        elif continuar == 'n':
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Por favor ingrese 's' para sí o 'n' para no.")