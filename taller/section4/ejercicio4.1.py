def sistema_lista_compras():
    lista_compras = []
    
    while True:
        print("\n=== SISTEMA DE LISTA DE COMPRAS ===")
        print("1. Agregar producto")
        print("2. Eliminar producto específico")
        print("3. Mostrar todos los productos")
        print("4. Vaciar lista")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == '1':
            producto = input("Ingrese el nombre del producto: ").strip().capitalize()
            if producto:
                lista_compras.append(producto)
                print(f"'{producto}' agregado a la lista")
            else:
                print("El nombre del producto no puede estar vacío")
        
        elif opcion == '2':
            if not lista_compras:
                print("La lista está vacía")
                continue
                
            print("\nProductos actuales:")
            for i, prod in enumerate(lista_compras, 1):
                print(f"  {i}. {prod}")
            
            try:
                indice = int(input("\nIngrese el número del producto a eliminar: ")) - 1
                if 0 <= indice < len(lista_compras):
                    producto_eliminado = lista_compras.pop(indice)
                    print(f"'{producto_eliminado}' eliminado de la lista")
                else:
                    print("Número de producto no válido")
            except ValueError:
                print("Ingrese un número válido")
        
        elif opcion == '3':
            print("\nLISTA DE COMPRAS ACTUAL:")
            if lista_compras:
                for i, prod in enumerate(lista_compras, 1):
                    print(f"  {i}. {prod}")
                print(f"Total de productos: {len(lista_compras)}")
            else:
                print("  La lista está vacía")
        
        elif opcion == '4':
            confirmar = input("¿Está seguro de vaciar la lista? (s/n): ").lower()
            if confirmar in ['s', 'si']:
                lista_compras.clear()
                print("Lista vaciada completamente")
        
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

sistema_lista_compras()