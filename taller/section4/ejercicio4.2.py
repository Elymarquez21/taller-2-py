def directorio_contactos():
    contactos = {}
    
    while True:
        print("\n=== DIRECTORIO DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ").strip().capitalize()
            if not nombre:
                print("El nombre no puede estar vacío")
                continue
                
            if nombre in contactos:
                print(f"El contacto '{nombre}' ya existe")
                sobreescribir = input("¿Desea actualizar su número? (s/n): ").lower()
                if sobreescribir not in ['s', 'si']:
                    continue
            
            telefono = input("Ingrese el número telefónico: ").strip()
            if telefono:
                contactos[nombre] = telefono
                print(f"Contacto '{nombre}' guardado")
            else:
                print("El teléfono no puede estar vacío")
        
        elif opcion == '2':
            if not contactos:
                print("El directorio está vacío")
                continue
                
            nombre = input("Ingrese el nombre a buscar: ").strip().capitalize()
            
            if nombre in contactos:
                print(f"Contacto encontrado:")
                print(f"   Nombre: {nombre}")
                print(f"   Teléfono: {contactos[nombre]}")
            else:
                print(f"No se encontró el contacto '{nombre}'")
                
                coincidencias = [n for n in contactos if nombre.lower() in n.lower()]
                if coincidencias:
                    print("Contactos similares:")
                    for n in coincidencias:
                        print(f"  • {n}: {contactos[n]}")
        
        elif opcion == '3':
            if not contactos:
                print("El directorio está vacío")
                continue
                
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().capitalize()
            
            if nombre in contactos:
                confirmar = input(f"¿Eliminar a '{nombre}'? (s/n): ").lower()
                if confirmar in ['s', 'si']:
                    del contactos[nombre]
                    print(f"Contacto '{nombre}' eliminado")
            else:
                print(f"No se encontró el contacto '{nombre}'")
        
        elif opcion == '4':
            print("\nDIRECTORIO DE CONTACTOS:")
            if contactos:
                for nombre, telefono in sorted(contactos.items()):
                    print(f"  • {nombre}: {telefono}")
                print(f"Total de contactos: {len(contactos)}")
            else:
                print("  El directorio está vacío")
        
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

directorio_contactos()