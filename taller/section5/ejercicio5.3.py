def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora_funciones():
    while True:
        print("\n=== CALCULADORA CON FUNCIONES ===")
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
            print("Opción no válida")
            continue
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"{num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = restar(num1, num2)
                print(f"{num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                print(f"{num1} * {num2} = {resultado}")
            elif opcion == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
                
        except ValueError:
            print("Error: Ingrese números válidos")

calculadora_funciones()