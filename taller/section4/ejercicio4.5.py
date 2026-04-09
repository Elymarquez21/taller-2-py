def comparador_listas():
    print("=== COMPARADOR AVANZADO DE LISTAS ===")
    
    def ingresar_lista(nombre_lista):
        print(f"\nIngrese elementos para la {nombre_lista} separados por comas")
        print("Ejemplo: manzana,pera,uva,manzana,banana")
        entrada = input(f"{nombre_lista}: ").strip()
        
        lista = []
        for item in entrada.split(','):
            elemento = item.strip()
            if elemento:
                lista.append(elemento)
        
        return lista
    
    lista1 = ingresar_lista("LISTA 1")
    lista2 = ingresar_lista("LISTA 2")
    
    if not lista1 and not lista2:
        print("\nAmbas listas están vacías")
        return
    
    print("\n" + "=" * 50)
    print("LISTAS INGRESADAS:")
    print(f"   Lista 1: {lista1}")
    print(f"   Lista 2: {lista2}")
    
    comunes = []
    for elem in lista1:
        if elem in lista2 and elem not in comunes:
            comunes.append(elem)
    
    unicos_lista1 = []
    for elem in lista1:
        if elem not in lista2 and elem not in unicos_lista1:
            unicos_lista1.append(elem)
    
    unicos_lista2 = []
    for elem in lista2:
        if elem not in lista1 and elem not in unicos_lista2:
            unicos_lista2.append(elem)
    
    print("\n" + "=" * 50)
    print("RESULTADOS DE LA COMPARACIÓN:")
    
    print(f"\nELEMENTOS COMUNES:")
    if comunes:
        for i, elem in enumerate(comunes, 1):
            print(f"   {i}. {elem}")
    else:
        print("   No hay elementos comunes")
    
    print(f"\nELEMENTOS ÚNICOS DE LISTA 1:")
    if unicos_lista1:
        for i, elem in enumerate(unicos_lista1, 1):
            print(f"   {i}. {elem}")
    else:
        print("   No hay elementos exclusivos en lista 1")
    
    print(f"\nELEMENTOS ÚNICOS DE LISTA 2:")
    if unicos_lista2:
        for i, elem in enumerate(unicos_lista2, 1):
            print(f"   {i}. {elem}")
    else:
        print("   No hay elementos exclusivos en lista 2")
    
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS:")
    print(f"   • Lista 1: {len(lista1)} elementos ({len(unicos_lista1)} exclusivos)")
    print(f"   • Lista 2: {len(lista2)} elementos ({len(unicos_lista2)} exclusivos)")
    print(f"   • Elementos comunes: {len(comunes)}")
    
    total_unicos = []
    for elem in lista1 + lista2:
        if elem not in total_unicos:
            total_unicos.append(elem)
    
    print(f"   • Total elementos únicos: {len(total_unicos)}")

comparador_listas()