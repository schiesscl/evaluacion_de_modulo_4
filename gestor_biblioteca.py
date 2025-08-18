from biblioteca import Biblioteca       # Importa la clase Biblioteca (gestión de libros y archivo)
from libro import Libro                 # Importa la clase Libro (base)
from libro_digital import LibroDigital  # Importa la clase LibroDigital (hereda de Libro)

# Función que muestra el menú principal
def mostrar_menu():
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Ver todos los libros")
    print("4. Buscar libro")
    print("5. Marcar libro como prestado")
    print("6. Devolver libro")
    print("7. Salir")

# Función que muestra el submenú al elegir agregar libro
def sub_menu_agregar():
    print("\n---  Agregar Libro ---")
    print("1. Libro físico")
    print("2. Libro digital")
    print("3. Volver al menú principal")
    
def main():
    biblioteca = Biblioteca()  # Se crea una instancia de la clase Biblioteca
    
    while True:  # Bucle infinito para mantener el menú activo
        mostrar_menu()  # Muestra el menú principal
        opcion = input("Seleccione una opción: ").strip()  # Lee la opción del usuario

        # --- Opción 1: Agregar libro ---
        if opcion == "1":
            sub_menu_agregar()  # Muestra el submenú de agregar libro
            tipo_opcion = input("Seleccione el tipo de libro a agregar: ").strip()
            
            if tipo_opcion == "1":  # Agregar libro físico
                try:
                    # Solicita datos del libro físico
                    titulo = input("Título: ").strip()
                    autor = input("Autor: ").strip()
                    anyo_publicacion = int(input("Año de publicación: ").strip())
                    # Crea un objeto Libro
                    libro = Libro(titulo, autor, anyo_publicacion)
                    biblioteca.agregar_libro(libro)  # Lo agrega a la biblioteca
                except ValueError as e:  # Captura errores de conversión o validación
                    print(f"Error al agregar libro: {e}")

            elif tipo_opcion == "2":  # Agregar libro digital
                try:
                    # Solicita datos del libro digital
                    titulo = input("Título: ").strip()
                    autor = input("Autor: ").strip()
                    anyo_publicacion = int(input("Año de publicación: ").strip())
                    # Muestra los formatos válidos definidos en LibroDigital
                    print(f"Formatos válidos: {', '.join(LibroDigital.FORMATOS_VALIDOS)}")
                    formato = input("Formato: ").strip().lower()
                    # Crea un objeto LibroDigital
                    libro = LibroDigital(titulo, autor, anyo_publicacion, formato)
                    biblioteca.agregar_libro(libro)  # Lo agrega a la biblioteca
                except ValueError as e:  # Captura errores de validación (ej. formato inválido)
                    print(f"Error al agregar libro digital: {e}")

            elif tipo_opcion == "3":  # Cancelar y volver al menú principal
                print("Operación cancelada.")

            else:  # Si el usuario ingresa una opción inválida
                print("Opción no válida. Volviendo al menú principal.")

        # --- Opción 2: Eliminar libro ---
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a eliminar: ").strip()
            try:
                biblioteca.eliminar_libro(titulo)  # Intenta eliminar el libro
            except ValueError as e:  # Captura error si el libro no existe
                print(f"Error al eliminar libro: {e}")

        # --- Opción 3: Listar todos los libros ---
        elif opcion == "3":
            biblioteca.listar_libros()  # Muestra todos los libros (disponibles o prestados)
        
        # --- Opción 4: Buscar libro ---
        elif opcion == "4":
            titulo = input("Ingrese el título del libro a buscar: ").strip()
            libro = biblioteca.buscar_libro(titulo)  # Busca en la biblioteca
            if libro:  # Si lo encuentra, lo muestra
                print(libro)
            else:  # Si no existe
                print("No se encontró el libro.")

        # --- Opción 5: Marcar libro como prestado ---
        elif opcion == "5":
            titulo = input("Ingrese el título del a prestar: ").strip()
            try:
                biblioteca.prestar_libro(titulo)  # Intenta marcar como prestado
            except ValueError as e:  # Si ya estaba prestado o no existe
                print(f"Error al prestar libro: {e}")

        # --- Opción 6: Devolver libro ---
        elif opcion == "6":
            titulo = input("Ingrese el título del libro a devolver: ").strip()
            try:
                biblioteca.devolver_libro(titulo)  # Intenta devolver
            except ValueError as e:  # Si no existe o ya estaba disponible
                print(f"Error al devolver libro: {e}")

        # --- Opción 7: Guardar y salir ---
        elif opcion == "7":
            print("Guardando cambios y saliendo...")
            biblioteca.guardar_en_archivo()  # Guarda el estado actual en el archivo
            break  # Rompe el bucle y termina el programa

        # --- Opción inválida ---
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
