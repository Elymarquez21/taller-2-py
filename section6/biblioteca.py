# Sistema de Gestion de Biblioteca
# Estructura: lista de diccionarios con id, titulo, autor, año y disponibilidad

catalogo = []
contador_id = 1


def agregar_libro():
    # Registra un nuevo libro validando que el año sea numerico y mayor a 1900
    global contador_id
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    if not titulo or not autor:
        print("Error: titulo y autor son obligatorios.")
        return
    while True:
        año = input("Año (mayor a 1900): ").strip()
        if año.isdigit() and int(año) > 1900:
            break
        print("Error: año invalido.")
    catalogo.append({"id": contador_id, "titulo": titulo, "autor": autor, "año": int(año), "disponible": True})
    print(f"Libro agregado con ID {contador_id}.")
    contador_id += 1


def mostrar_libros():
    # Muestra todos los libros en formato: "ID: 1 - 'Titulo' (Autor, Año) [Estado]"
    if not catalogo:
        print("No hay libros registrados.")
        return
    for libro in catalogo:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['año']}) [{estado}]")


def buscar_libro():
    # Busca libros por titulo o autor mostrando coincidencias parciales
    termino = input("Buscar por titulo o autor: ").strip().lower()
    resultados = [l for l in catalogo if termino in l["titulo"].lower() or termino in l["autor"].lower()]
    if not resultados:
        print("No se encontraron resultados.")
    else:
        for l in resultados:
            estado = "Disponible" if l["disponible"] else "Prestado"
            print(f"ID: {l['id']} - '{l['titulo']}' ({l['autor']}, {l['año']}) [{estado}]")


def prestar_libro(id_libro):
    # Cambia disponibilidad a False si el libro existe y esta disponible
    for libro in catalogo:
        if libro["id"] == id_libro:
            if libro["disponible"]:
                libro["disponible"] = False
                print(f"Libro '{libro['titulo']}' prestado.")
            else:
                print("El libro ya esta prestado.")
            return
    print("ID no encontrado.")


def devolver_libro(id_libro):
    # Cambia disponibilidad a True cuando el libro es devuelto
    for libro in catalogo:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                libro["disponible"] = True
                print(f"Libro '{libro['titulo']}' devuelto.")
            else:
                print("El libro ya esta disponible.")
            return
    print("ID no encontrado.")


def eliminar_libro(id_libro):
    # Elimina un libro solo si no esta prestado actualmente
    for libro in catalogo:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                print("No se puede eliminar un libro prestado.")
                return
            catalogo.remove(libro)
            print(f"Libro '{libro['titulo']}' eliminado.")
            return
    print("ID no encontrado.")


def libros_por_autor(autor):
    # Lista todos los libros de un autor especifico (busqueda parcial)
    resultado = [l for l in catalogo if autor.lower() in l["autor"].lower()]
    if not resultado:
        print(f"No hay libros del autor '{autor}'.")
    else:
        for l in resultado:
            estado = "Disponible" if l["disponible"] else "Prestado"
            print(f"ID: {l['id']} - '{l['titulo']}' ({l['año']}) [{estado}]")


def estadisticas():
    # Muestra cantidad total de libros, disponibles y prestados
    total = len(catalogo)
    disponibles = sum(1 for l in catalogo if l["disponible"])
    print(f"Total: {total} | Disponibles: {disponibles} | Prestados: {total - disponibles}")


def exportar_a_txt():
    # Guarda todos los libros en un archivo de texto llamado "biblioteca.txt"
    if not catalogo:
        print("No hay libros para exportar.")
        return
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        for l in catalogo:
            estado = "Disponible" if l["disponible"] else "Prestado"
            f.write(f"ID: {l['id']} - '{l['titulo']}' ({l['autor']}, {l['año']}) [{estado}]\n")
    print("Catalogo exportado a 'biblioteca.txt'.")


def pedir_id(mensaje):
    # Valida que el ID ingresado sea un numero entero positivo
    val = input(mensaje).strip()
    return int(val) if val.isdigit() and int(val) > 0 else None


def menu_principal():
    # Menu interactivo con while que se repite hasta que el usuario elija salir
    print("=== SISTEMA DE BIBLIOTECA ===")
    while True:
        print("\n1. Agregar libro\n2. Mostrar libros\n3. Buscar libro")
        print("4. Prestar libro\n5. Devolver libro\n6. Eliminar libro")
        print("7. Libros por autor\n8. Estadisticas\n9. Exportar a TXT\n0. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":   agregar_libro()
        elif opcion == "2": mostrar_libros()
        elif opcion == "3": buscar_libro()
        elif opcion == "4":
            mostrar_libros()
            id_ = pedir_id("ID a prestar: ")
            if id_: prestar_libro(id_)
        elif opcion == "5":
            mostrar_libros()
            id_ = pedir_id("ID a devolver: ")
            if id_: devolver_libro(id_)
        elif opcion == "6":
            mostrar_libros()
            id_ = pedir_id("ID a eliminar: ")
            if id_: eliminar_libro(id_)
        elif opcion == "7":
            autor = input("Nombre del autor: ").strip()
            if autor: libros_por_autor(autor)
        elif opcion == "8": estadisticas()
        elif opcion == "9": exportar_a_txt()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    # Libros de ejemplo precargados para pruebas
    catalogo = [
        {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel Garcia Marquez", "año": 1967, "disponible": True},
        {"id": 2, "titulo": "1984", "autor": "George Orwell", "año": 1949, "disponible": True},
        {"id": 3, "titulo": "El amor en los tiempos del colera", "autor": "Gabriel Garcia Marquez", "año": 1985, "disponible": False},
    ]
    contador_id = 4
    menu_principal()