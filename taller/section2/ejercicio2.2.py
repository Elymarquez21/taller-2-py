def menu_basico():
    while True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '1':
            print("\n👋 ¡Hola! ¿Cómo estás?")
        elif opcion == '2':
            print("\n👋 ¡Hasta luego! Que tengas un buen día")
        elif opcion == '3':
            print("\nSaliendo del programa...")
            break
        else:
            print("\n❌ Opción no válida. Intente nuevamente.")

# Ejecutar
menu_basico()