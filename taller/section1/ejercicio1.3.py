def validar_correo():
    print("=== VALIDADOR DE CORREO ELECTRÓNICO ===")
    print("Formato básico requerido: nombre@dominio.extension")
    print("==========================================")
    
    # Solicitar correo al usuario
    correo = input("Ingrese su correo electrónico: ").strip()
    
    # Variable para rastrear errores
    errores = []
    
    # Verificar que no esté vacío
    if not correo:
        errores.append("❌ El correo no puede estar vacío")
    
    # Verificar que contenga @
    if '@' not in correo:
        errores.append("❌ El correo debe contener el símbolo '@'")
    else:
        # Verificar que tenga solo un @
        if correo.count('@') > 1:
            errores.append("❌ El correo no puede tener más de un '@'")
        
        # Verificar posiciones del @
        pos_arroba = correo.find('@')
        
        # Verificar que haya texto antes del @
        if pos_arroba == 0:
            errores.append("❌ Debe haber un nombre antes del '@'")
        
        # Verificar que haya texto después del @
        if pos_arroba == len(correo) - 1:
            errores.append("❌ Debe haber un dominio después del '@'")
            
        # Verificar que contenga . después del @
        if pos_arroba != -1:
            dominio = correo[pos_arroba + 1:]
            if '.' not in dominio:
                errores.append("❌ El dominio debe contener un punto (.)")
            else:
                # Verificar posición del último punto
                ultimo_punto = correo.rfind('.')
                
                # Verificar que el punto no esté inmediatamente después del @
                if ultimo_punto == pos_arroba + 1:
                    errores.append("❌ Debe haber un nombre de dominio antes del punto")
                
                # Verificar que haya al menos 2 caracteres después del último punto
                if ultimo_punto >= len(correo) - 2:
                    errores.append("❌ La extensión debe tener al menos 2 caracteres")
                
                # Verificar que no haya puntos consecutivos
                if '..' in correo:
                    errores.append("❌ No puede haber puntos consecutivos")
    
    # Verificar caracteres especiales no permitidos (opcional)
    caracteres_invalidos = " <>()[]\\,;:\" "
    for char in caracteres_invalidos:
        if char in correo:
            errores.append(f"❌ El carácter '{char}' no es válido en un correo")
            break
    
    # Mostrar resultado
    print("\n" + "="*40)
    if not errores:
        print("✅ ¡Correo electrónico válido!")
        print(f"   {correo}")
        print("\n   El correo tiene el formato básico correcto:")
        print("   - Contiene @")
        print("   - Contiene . después del @")
        print("   - Tiene nombre antes del @")
        print("   - Tiene dominio después del @")
        print("   - Tiene extensión válida")
    else:
        print("❌ Correo electrónico INVÁLIDO")
        print("   Se encontraron los siguientes errores:")
        for i, error in enumerate(errores, 1):
            print(f"   {i}. {error}")
    
    print("="*40)

# Función con validación más simple
def validar_correo_simple():
    print("=== VALIDADOR DE CORREO (VERSIÓN SIMPLE) ===")
    
    correo = input("Ingrese su correo electrónico: ").strip()
    
    # Validaciones básicas
    tiene_arroba = '@' in correo
    tiene_punto = '.' in correo
    arroba_en_posicion_valida = correo.find('@') > 0 and correo.find('@') < len(correo) - 1
    punto_despues_arroba = correo.find('@') < correo.rfind('.') if tiene_arroba else False
    
    print("\n" + "="*40)
    
    if (tiene_arroba and tiene_punto and 
        arroba_en_posicion_valida and punto_despues_arroba):
        print("✅ ¡Formato de correo válido!")
        print(f"   {correo}")
    else:
        print("❌ Formato de correo inválido")
        
        # Mostrar errores específicos
        if not tiene_arroba:
            print("   - Falta el símbolo @")
        elif correo.find('@') == 0:
            print("   - No hay nombre antes del @")
        elif correo.find('@') == len(correo) - 1:
            print("   - No hay dominio después del @")
            
        if not tiene_punto:
            print("   - Falta el punto (.)")
        elif tiene_arroba and correo.find('@') > correo.rfind('.'):
            print("   - El punto debe estar después del @")
    
    print("="*40)

# Función principal con menú
def main():
    while True:
        print("\n=== MENÚ VALIDADOR DE CORREOS ===")
        print("1. Validación detallada")
        print("2. Validación simple")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            validar_correo()
        elif opcion == "2":
            validar_correo_simple()
        elif opcion == "3":
            print("¡Gracias por usar el validador!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar programa
if __name__ == "__main__":
    main()