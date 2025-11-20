# Definición de la clase Libro (representa un libro físico o digital)
class Libro:
    def __init__(self, titulo: str, autor: str, anyo_publicacion: int, estado: str = "disponible"):  # ✅ CAMBIO 1
        # Atributos privados de la clase (encapsulación con __)
        self.__titulo = titulo
        self.__autor = autor
        self.__anyo_publicacion = anyo_publicacion
        # Validación del estado: solo puede ser "disponible" o "prestado"
        if estado.lower() not in ["disponible", "prestado"]:
            raise ValueError("El estado debe ser 'disponible' o 'prestado'.")  # ✅ CAMBIO 2
        # Se guarda el estado en minúsculas para un manejo consistente
        self.__estado = estado.lower()
        
    # --- Métodos GETTER (accesores) ---
    # Devuelven el valor de los atributos privados
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_anyo_publicacion(self) -> int:
        return self.__anyo_publicacion

    def get_estado(self) -> str:
        return self.__estado

    # --- Métodos SETTER (mutadores) ---
    # Permiten modificar los atributos privados de forma controlada
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autor(self, autor: str):
        self.__autor = autor

    def set_anio_publicacion(self, anyo_publicacion: int):
        self.__anyo_publicacion = anyo_publicacion

    def set_estado(self, estado: str):
        # Validación: el estado solo puede ser "disponible" o "prestado"
        if estado.lower() not in ["disponible", "prestado"]:
            raise ValueError("El estado debe ser 'disponible' o 'prestado'.")  # ✅ CAMBIO 3
        self.__estado = estado.lower()
        
    # Representación en formato legible del objeto Libro
    def __str__(self) -> str:
        return (f"Título: {self.__titulo}, "
                f"Autor: {self.__autor}, "
                f"Año de publicación: {self.__anyo_publicacion}, "
                f"Estado: {self.__estado.capitalize()}")
