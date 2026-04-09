def buscar_nombre():
    print("=== BÚSQUEDA EN LISTA DE NOMBRES ===")
    
    # Lista predefinida de nombres
    nombres = ["Ana", "Carlos", "María", "Juan", "Laura", 
               "Pedro", "Sofía", "Diego", "Valentina", "Luis"]
    
    print("\nLista de nombres disponibles:")
    for i, nombre in enumerate(nombres, 1):
        print(f"  {i}. {nombre}")
    
    nombre_buscar = input("\nIngrese el nombre que desea buscar: ").strip().capitalize()
    
    encontrado = False
    posicion = -1
    
    # Búsqueda lineal
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscar:
            encontrado = True
            posicion = i + 1  # +1 para posición más amigable (1-based)
            break
    
    print("\n" + "=" * 40)
    if encontrado:
        print(f"✅ ¡Nombre encontrado!")
        print(f"• '{nombre_buscar}' está en la posición {posicion}")
    else:
        print(f"❌ El nombre '{nombre_buscar}' no se encuentra en la lista")
    print("=" * 40)

# Ejecutar
buscar_nombre()