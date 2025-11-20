# Evaluación de Módulo 4

## Hans Schiess

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)

Este proyecto implementa un sistema de gestión de biblioteca utilizando **Programación Orientada a Objetos (POO)**. Permite administrar libros físicos y digitales, con persistencia de datos en un archivo de texto (`biblioteca.txt`).

---

## ✨ Funcionalidades

- **Agregar** libros físicos y digitales.
- **Eliminar** libros por título.
- **Listar** todos los libros, mostrando su estado (disponible o prestado).
- **Buscar** libros por título.
- **Marcar** un libro como **prestado**.
- **Devolver** un libro prestado.
- **Persistencia automática** en `biblioteca.txt`.

---

## 📂 Estructura de Archivos

```text
evaluacion_de_modulo_4/
│
├── libro.py              # Clase base Libro
├── libro_digital.py      # Clase LibroDigital (hereda de Libro)
├── biblioteca.py         # Clase Biblioteca (gestiona libros y archivo)
├── gestor_biblioteca.py  # Menú principal y punto de entrada
├── biblioteca.txt        # Archivo de datos (se genera automáticamente)
├── README.md             # Esta documentación
└── diagrama_clases.png   # Diagrama UML de las clases
```

---

## Diagrama de Clases (UML)

El siguiente diagrama muestra la relación entre las clases del sistema:

![Diagrama de Clases](diagrama_clases.png)

---

## 🚀 Ejecución

1. Asegúrate de tener **Python 3.8** o superior instalado.

    ```bash
    python --version
    ```

2. Desde la terminal, navega a la carpeta del proyecto.

3. Ejecuta el programa principal:

    ```bash
    python gestor_biblioteca.py
    ```

---

## 💻 Ejemplo de Uso

### 1. Agregar un libro físico

```terminal
--- Menú de Biblioteca ---
...
Seleccione una opción: 1

---  Agregar Libro ---
1. Libro físico
...
Seleccione el tipo de libro a agregar: 1
Ingrese el título: El Quijote
Ingrese el autor: Cervantes
Ingrese el año de publicación: 1605
Libro 'El Quijote' agregado a la biblioteca.
```

### 2. Agregar un libro digital

```terminal
Seleccione una opción: 1
...
Seleccione el tipo de libro a agregar: 2
Ingrese el título: Clean Code
Ingrese el autor: Robert C. Martin
Ingrese el año de publicación: 2008
Ingrese el formato (pdf, epub, mobi, azw, txt): pdf
Libro 'Clean Code' agregado a la biblioteca.
```

### 3. Ver todos los libros

```terminal
Seleccione una opción: 3
Título: El Quijote, Autor: Cervantes, Año de publicación: 1605, Estado: Disponible
Título: Clean Code, Autor: Robert C. Martin, Año de publicación: 2008, Estado: Disponible, Formato: PDF
```

---

## ⚠️ Manejo de Excepciones

El sistema captura y muestra mensajes claros ante errores comunes:

- **Libro no encontrado:** `No se encontró el libro con título 'Inexistente'.`
- **Libro ya prestado:** `El libro 'El Quijote' ya está prestado.`
- **Libro ya disponible:** `El libro 'Clean Code' ya estaba disponible.`
- **Biblioteca vacía:** `No hay libros registrados en la biblioteca.`

---

## 🛠️ Notas Técnicas

### 1. Formato de `biblioteca.txt`

Los datos se guardan con un formato específico, usando `|` como separador. Esto permite al programa leer y reconstruir los objetos correctamente.

- **Formato:** `tipo|titulo|autor|año|formato|estado`

- **Ejemplo libro físico:**
  
  ```terminal
  fisico|El Quijote|Cervantes|1605||disponible
  ```

  *(El campo de formato se deja vacío)*

- **Ejemplo libro digital:**
  
  ```terminal
  digital|Clean Code|Robert Martin|2008|pdf|disponible
  ```

### 2. Encapsulación (`__atributo`)

En Python, los atributos que comienzan con `__` (doble guion bajo) son tratados como **privados**. Esto se logra mediante un mecanismo llamado *name mangling*, que cambia internamente el nombre del atributo para evitar que sea accedido directamente desde fuera de la clase.

```python
class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo  # Atributo privado
```

Esta práctica refuerza la **encapsulación**, asegurando que los datos se modifiquen solo a través de métodos controlados (getters y setters).

### 3. Limpieza de Datos (`.strip()`)

Al cargar los libros desde `biblioteca.txt`, se utiliza `.strip()` para limpiar cada línea antes de procesarla.

```python
datos = linea.strip().split("|")
```

`.strip()` elimina espacios en blanco, tabulaciones y saltos de línea (`\n`) al inicio y al final de la cadena. Esto es crucial para evitar errores de comparación, ya que sin él, un estado podría ser leído como `"disponible\n"` en lugar de `"disponible"`.
