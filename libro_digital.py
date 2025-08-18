from libro import Libro  # Importa la clase base Libro para herencia

# Definición de la clase LibroDigital que hereda de Libro
class LibroDigital(Libro):
    # Lista de formatos de archivo válidos para los libros digitales
    FORMATOS_VALIDOS = ["pdf", "epub", "mobi", "azw", "txt"]

    def __init__(self, titulo: str, autor: str, anyo_publicacion: int, formato: str, estado: str = "disponible"):
        # Llamamos al constructor de la clase padre (Libro) para inicializar los atributos heredados
        super().__init__(titulo, autor, anyo_publicacion, estado)
        # Usamos el setter para validar y asignar el formato al atributo privado
        self.set_formato(formato)

    # Getter: permite obtener el valor del atributo privado __formato
    def get_formato(self) -> str:
        return self.__formato

    # Setter: establece el valor del atributo __formato con validación
    def set_formato(self, formato: str):
        # Limpia espacios y convierte el formato a minúsculas
        formato_limpio = formato.strip().lower()
        # Verifica que no sea un string vacío
        if not formato_limpio:
            raise ValueError("El formato no puede estar vacío.")
        # Verifica que el formato esté dentro de la lista de permitidos
        if formato_limpio not in self.FORMATOS_VALIDOS:
            raise ValueError(f"Formato no válido. Formatos permitidos: {', '.join(self.FORMATOS_VALIDOS)}")
        # Si pasa la validación, se asigna al atributo privado
        self.__formato = formato_limpio

    # Sobrescribimos el método __str__ para incluir el formato en la representación del libro
    def __str__(self) -> str:
        # Llamamos al __str__ de la clase base y le agregamos la información del formato en mayúsculas
        return f"{super().__str__()}, Formato: {self.__formato.upper()}"
