def gestor_inventario():
    inventario = [
        {"nombre": "Laptop", "precio": 1200.00, "stock": 15},
        {"nombre": "Mouse", "precio": 25.50, "stock": 50},
        {"nombre": "Teclado", "precio": 45.00, "stock": 30},
        {"nombre": "Monitor", "precio": 350.00, "stock": 10},
        {"nombre": "Audífonos", "precio": 80.00, "stock": 25}
    ]
    
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Ver inventario completo")
        print("2. Buscar producto")
        print("3. Actualizar precio de producto")
        print("4. Actualizar stock de producto")
        print("5. Agregar nuevo producto")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == '1':
            print("\nINVENTARIO COMPLETO:")
            print("-" * 50)
            print(f"{'NOMBRE':<15} {'PRECIO':<12} {'STOCK':<10}")
            print("-" * 50)
            for producto in inventario:
                print(f"{producto['nombre']:<15} ${producto['precio']:<11.2f} {producto['stock']:<10}")
            print("-" * 50)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ").strip().capitalize()
            
            encontrado = False
            for producto in inventario:
                if producto['nombre'].lower() == nombre.lower():
                    print(f"Producto encontrado:")
                    print(f"  • Nombre: {producto['nombre']}")
                    print(f"  • Precio: ${producto['precio']:.2f}")
                    print(f"  • Stock: {producto['stock']} unidades")
                    encontrado = True
                    break
            
            if not encontrado:
                print(f"Producto '{nombre}' no encontrado")
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
            
            for producto in inventario:
                if producto['nombre'].lower() == nombre.lower():
                    print(f"Producto encontrado: {producto['nombre']}")
                    print(f"Precio actual: ${producto['precio']:.2f}")
                    
                    try:
                        nuevo_precio = float(input("Ingrese el nuevo precio: $"))
                        if nuevo_precio > 0:
                            producto['precio'] = nuevo_precio
                            print(f"Precio actualizado a ${nuevo_precio:.2f}")
                        else:
                            print("El precio debe ser positivo")
                    except ValueError:
                        print("Ingrese un número válido")
                    break
            else:
                print(f"Producto '{nombre}' no encontrado")
        
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
            
            for producto in inventario:
                if producto['nombre'].lower() == nombre.lower():
                    print(f"Producto encontrado: {producto['nombre']}")
                    print(f"Stock actual: {producto['stock']} unidades")
                    
                    try:
                        nuevo_stock = int(input("Ingrese el nuevo stock: "))
                        if nuevo_stock >= 0:
                            producto['stock'] = nuevo_stock
                            print(f"Stock actualizado a {nuevo_stock} unidades")
                        else:
                            print("El stock no puede ser negativo")
                    except ValueError:
                        print("Ingrese un número entero válido")
                    break
            else:
                print(f"Producto '{nombre}' no encontrado")
        
        elif opcion == '5':
            nombre = input("Ingrese el nombre del nuevo producto: ").strip().capitalize()
            
            for producto in inventario:
                if producto['nombre'].lower() == nombre.lower():
                    print(f"El producto '{nombre}' ya existe en el inventario")
                    break
            else:
                try:
                    precio = float(input("Ingrese el precio: $"))
                    stock = int(input("Ingrese el stock inicial: "))
                    
                    if precio > 0 and stock >= 0:
                        inventario.append({
                            "nombre": nombre,
                            "precio": precio,
                            "stock": stock
                        })
                        print(f"Producto '{nombre}' agregado al inventario")
                    else:
                        print("Precio debe ser positivo y stock no negativo")
                except ValueError:
                    print("Ingrese valores numéricos válidos")
        
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

gestor_inventario()