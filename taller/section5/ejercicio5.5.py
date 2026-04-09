def factorial(n):
    if n < 0:
        return "Error: No existe factorial de números negativos"
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

def probar_factorial():
    print("=== CALCULADORA FACTORIAL ===")
    print("El factorial de n (n!) es: n * (n-1) * (n-2) * ... * 1")
    
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        resultado = factorial(numero)
        
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"{numero}! = {resultado}")
            
    except ValueError:
        print("Ingrese un número válido")
    except RecursionError:
        print("Número demasiado grande para calcular recursivamente")

probar_factorial()