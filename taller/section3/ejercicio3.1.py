def generar_pares():
    print("=== GENERADOR DE NÚMEROS PARES ===")
    
    try:
        n = int(input("Ingrese un número entero positivo N: "))
        
        if n <= 0:
            print("❌ Error: Debe ingresar un número positivo")
            return
        
        print(f"\nNúmeros pares del 1 al {n}:")
        contador = 0
        
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
                contador += 1
        
        if contador == 0:
            print("No hay números pares en este rango")
        else:
            print(f"\n\nTotal de números pares encontrados: {contador}")
            
    except ValueError:
        print("❌ Error: Ingrese un número válido")

# Ejecutar
generar_pares()