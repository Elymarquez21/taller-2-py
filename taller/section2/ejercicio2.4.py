def convertir_calificacion():
    print("=== CONVERSOR DE CALIFICACIONES ===")
    print("Escala: A(90-100), B(80-89), C(70-79), D(60-69), F(0-59)")
    
    try:
        nota = float(input("\nIngrese la calificación numérica (0-100): "))
        
        if nota < 0 or nota > 100:
            print("❌ Error: La nota debe estar entre 0 y 100")
        elif nota >= 90:
            letra = 'A'
            print(f"\n{nota} puntos → Calificación: {letra} (Excelente)")
        elif nota >= 80:
            letra = 'B'
            print(f"\n{nota} puntos → Calificación: {letra} (Bien)")
        elif nota >= 70:
            letra = 'C'
            print(f"\n{nota} puntos → Calificación: {letra} (Suficiente)")
        elif nota >= 60:
            letra = 'D'
            print(f"\n{nota} puntos → Calificación: {letra} (Insuficiente)")
        else:
            letra = 'F'
            print(f"\n{nota} puntos → Calificación: {letra} (Reprobado)")
            
    except ValueError:
        print("❌ Error: Ingrese un número válido")

# Ejecutar
convertir_calificacion()