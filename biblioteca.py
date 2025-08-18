from libro import Libro              # Importa la clase base Libro definida en otro módulo
from libro_digital import LibroDigital  # Importa la subclase LibroDigital (hereda de Libro)
import os                            # Módulo del sistema operativo (para verificar existencia de archivos)

class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.__libros = []           # Lista privada para almacenar objetos Libro y LibroDigital
        self.__archivo = archivo     # Ruta/nombre del archivo de persistencia (por defecto 'biblioteca.txt')
        self.cargar_desde_archivo()  # Al inicializar, intenta cargar libros desde el archivo

    def agregar_libro(self, libro: Libro):
        self.__libros.append(libro)  # Agrega el objeto libro a la lista interna
        # Muestra un mensaje confirmando que se agregó el libro correctamente
        print(f"Libro '{libro.get_titulo()}' agregado a la biblioteca.")  

    def eliminar_libro(self, titulo: str):
        if not self.__libros:  # Si la lista de libros está vacía
            raise ValueError("No hay libros registrados en la biblioteca.")  # Lanza excepción
        for libro in self.__libros:  # Recorre cada libro en la lista
            if libro.get_titulo().lower() == titulo.lower():  # Compara títulos ignorando mayúsculas/minúsculas
                self.__libros.remove(libro)  # Elimina el libro encontrado
                print(f"Libro '{titulo}' eliminado de la biblioteca.")  # Mensaje de confirmación
                return  # Sale del método tras eliminar
        raise ValueError(f"No se encontró el libro con título '{titulo}'.")  # Si no se encontró, lanza excepción

    def listar_libros(self, solo_disponibles=False):
        if not self.__libros:         # Si la lista está vacía
            print("No hay libros en la biblioteca.")  # Informa que no hay libros
            return                    # Sale del método
        for libro in self.__libros:   # Recorre todos los libros
            if solo_disponibles:      # Si el parámetro indica mostrar solo disponibles
                if libro.get_estado() == "disponible":  # Comprueba si el libro está disponible
                    print(libro)      # Imprime el objeto (usa su método __str__)
            else:
                print(libro)          # Si no se aplica filtro, imprime todos los libros

    def buscar_libro(self, titulo: str):
        for libro in self.__libros:   # Recorre la lista buscando coincidencias
            if libro.get_titulo().lower() == titulo.lower():  # Comparación insensible a mayúsculas
                return libro          # Devuelve el objeto encontrado
        return None                   # Si no lo encuentra, devuelve None

    def prestar_libro(self, titulo: str):
        if not self.__libros:  # Si no hay libros cargados
            raise ValueError("No hay libros registrados en la biblioteca.")
        libro = self.buscar_libro(titulo)  # Busca el libro por título
        if not libro:  # Si no existe
            raise ValueError(f"No se encontró el libro '{titulo}'.")
        if libro.get_estado() == "prestado":  # Si ya está prestado
            raise ValueError(f"El libro '{titulo}' ya está prestado.")
        libro.set_estado("prestado")  # Cambia el estado a "prestado"
        print(f"📚 Libro '{titulo}' marcado como prestado.")  # Confirma el préstamo

    def devolver_libro(self, titulo: str):
        if not self.__libros:  # Si no hay libros en la lista
            raise ValueError("No hay libros registrados en la biblioteca.")
        libro = self.buscar_libro(titulo)  # Busca el libro
        if not libro:  # Si no existe
            raise ValueError(f"No se encontró el libro '{titulo}'.")
        if libro.get_estado() == "disponible":  # Si ya estaba disponible
            raise ValueError(f"El libro '{titulo}' ya estaba disponible.")
        libro.set_estado("disponible")  # Cambia el estado a disponible
        print(f"Libro '{titulo}' devuelto correctamente.")  # Confirma devolución

    def guardar_en_archivo(self):
        # Abre/crea el archivo en modo escritura, sobrescribiendo el contenido anterior
        with open(self.__archivo , "w", encoding="utf-8") as archivo:
            for libro in self.__libros:     # Recorre todos los libros de la biblioteca
                if isinstance(libro, LibroDigital):  # Si el libro es digital
                    tipo = "digital"        # Marca el tipo como digital
                    formato = libro.get_formato()  # Obtiene el formato (pdf, epub, etc.)
                else:
                    tipo = "fisico"         # En caso contrario, es un libro físico
                    formato = ""            # No necesita formato
                # Escribe los campos en una línea separados por '|'
                # Orden: tipo | titulo | autor | año | formato | estado
                archivo.write(f"{tipo}|{libro.get_titulo()}|{libro.get_autor()}|{libro.get_anyo_publicacion()}|{formato}|{libro.get_estado()}\n")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.__archivo):  # Verifica si el archivo existe
            return                              # Si no existe, no hace nada

        # Abre el archivo en modo lectura
        with open(self.__archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:              # Recorre cada línea del archivo
                datos = linea.strip().split(";")  # Elimina espacios/saltos de línea y separa por ';'
                if len(datos) >= 5:            # Valida que tenga al menos 5 elementos
                    # Desempaqueta los datos: tipo, titulo, autor, año, estado y resto (ej. formato digital)
                    tipo, titulo, autor, anyo_publicacion, estado, *resto = datos
                try:
                    if tipo == "digital" and len(resto) > 0:  # Si es digital y hay formato
                        formato = resto[0]                    # Obtiene el formato
                        # Crea un objeto LibroDigital con los datos (convierte año a entero)
                        libro = LibroDigital(titulo, autor, int(anyo_publicacion), formato, estado)
                    else:
                        # Crea un objeto Libro físico con los datos
                        libro = Libro(titulo, autor, int(anyo_publicacion), estado)
                    self.__libros.append(libro)  # Agrega el objeto a la lista
                except ValueError as e:  # Si ocurre un error en la conversión o validación
                    print(f"Error al cargar el libro '{titulo}': {e}")  # Muestra error y continúa
