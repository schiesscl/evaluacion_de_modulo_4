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
        # Verifica si el archivo existe antes de intentar leerlo
        if not os.path.exists(self.__archivo):
            return  # Si no existe, sale del método sin hacer nada

        # Abre el archivo en modo lectura
        with open(self.__archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:  # Lee línea por línea
                # Elimina espacios y saltos de línea, luego divide por '|'
                datos = linea.strip().split("|")
                
                # Valida que tenga al menos 5 campos (mínimo para un libro físico sin formato)
                if len(datos) >= 5:
                    # Extrae los campos básicos
                    tipo = datos[0]
                    titulo = datos[1]
                    autor = datos[2]
                    anyo_publicacion = datos[3]
                    # Maneja el formato de forma segura (puede estar vacío o no existir)
                    formato = datos[4] if len(datos) > 4 else ""
                    # Maneja el estado de forma segura (debe estar en la posición 5)
                    estado = datos[5] if len(datos) > 5 else "disponible"
                    
                    try:
                        # Si es digital Y tiene formato válido (no vacío)
                        if tipo == "digital" and formato:
                            libro = LibroDigital(titulo, autor, int(anyo_publicacion), formato, estado)
                        else:
                            # Caso libro físico o digital sin formato
                            libro = Libro(titulo, autor, int(anyo_publicacion), estado)
                        
                        # Agrega el libro a la lista sin imprimir mensaje
                        self.__libros.append(libro)
                    
                    except ValueError as e:
                        # Captura errores de validación (formato inválido, año no numérico, etc.)
                        print(f"⚠️ Error al cargar el libro '{titulo}': {e}")
