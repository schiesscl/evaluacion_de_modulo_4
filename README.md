# M4_Evaluación del módulo

Este proyecto implementa un sistema de gestión de biblioteca utilizando **Programación Orientada a Objetos (POO)** en **Python 3.12.2**.  
Permite gestionar libros físicos y digitales, con persistencia de datos en un archivo `biblioteca.txt`.

---

## Funcionalidades

- Agregar libros físicos y digitales.
- Eliminar libros por título.
- Listar todos los libros, mostrando su **estado** (disponible o prestado).
- Buscar libros por título.
- Marcar un libro como **prestado**.
- Devolver un libro prestado.
- Persistencia automática en `biblioteca.txt`.

---

## Estructura de Archivos

```text
biblioteca_gestor/
│
├── libro.py              # Clase Libro
├── libro_digital.py      # Clase LibroDigital (hereda de Libro)
├── biblioteca.py         # Clase Biblioteca (gestiona lista y archivo)
├── gestor_biblioteca.py  # Menú principal para interactuar con la biblioteca
├── biblioteca.txt        # Archivo de persistencia de datos (se genera solo)
├── README.md             # Documentación del proyecto
└── diagrama_clases.drawio  # Diagrama UML de las clases
```

---

## Ejecución del Programa

1. Asegúrate de tener **Python 3.12.2** instalado.  
   Verifica con:

   ```bash
   python --version
   ```

2. Entra a la carpeta del proyecto:

   ```bash
   cd biblioteca_gestor
   ```

3. Ejecuta el programa principal:

   ```bash
   python gestor_biblioteca.py
   ```

---

## Menú Principal

Al ejecutar, verás:

```terminal
--- Gestor de Biblioteca ---
1. Agregar libro
2. Eliminar libro
3. Ver todos los libros
4. Buscar libro
5. Marcar libro como prestado
6. Devolver libro
7. Salir
Elige una opción:
```

---

## Ejemplo de Uso

### 1. Agregar un libro físico

```terminal
Elige una opción: 1

--- Agregar Libro ---
1. Libro físico
2. Libro digital
3. Cancelar
Elige el tipo de libro: 1
Título: El Quijote
Autor: Cervantes
Año de publicación: 1605
Libro 'El Quijote' agregado correctamente.
```

### 2. Agregar un libro digital

```terminal
Elige una opción: 1

--- Agregar Libro ---
1. Libro físico
2. Libro digital
3. Cancelar
Elige el tipo de libro: 2
Título: Clean Code
Autor: Robert C. Martin
Año de publicación: 2008
Formatos permitidos: pdf, epub, mobi, azw, txt
Formato: pdf
Libro 'Clean Code' agregado correctamente.
```

### 3️. Ver todos los libros

```terminal
Elige una opción: 3
Título: El Quijote, Autor: Cervantes, Año: 1605, Estado: Disponible
Título: Clean Code, Autor: Robert C. Martin, Año: 2008, Estado: Disponible, Formato: PDF
```

### 4️. Prestar un libro

```terminal
Elige una opción: 5
Título a prestar: El Quijote
Libro 'El Quijote' marcado como prestado.
```

### 5️. Devolver un libro

```terminal
Elige una opción: 6
Título a devolver: El Quijote
Libro 'El Quijote' devuelto correctamente.
```

---

## Manejo de Excepciones

El sistema captura y muestra mensajes claros cuando ocurren errores:

- Intentar eliminar un libro inexistente:

  ```terminal
  Error: No se encontró el libro con título 'Inexistente'.
  ```

- Prestar un libro que ya está prestado:
  
  ```terminal
  Error: El libro 'El Quijote' ya está prestado.
  ```

- Devolver un libro que no estaba prestado:
  
  ```terminal
  Error: El libro 'El Quijote' ya estaba disponible.
  ```

- Biblioteca vacía al intentar eliminar/prestar/devolver:

  ```terminal
  Error: No hay libros registrados en la biblioteca.
  ```

---

## 🛠️ Notas Técnicas

### 1. Uso de atributos con doble guion bajo (`__atributo`)

En Python, los atributos que comienzan con doble guion bajo (`__`) se vuelven **privados** mediante un mecanismo llamado *name mangling*.  
Esto significa que internamente Python cambia el nombre para que no se pueda acceder directamente desde fuera de la clase.  
Por ejemplo:

```python
class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo  # atributo privado
```

Esto evita accesos accidentales desde fuera de la clase y fomenta la **encapsulación**.  
La forma correcta de acceder o modificar estos atributos es mediante **getters y setters**.

---

### 2. Uso de `.strip()` al leer el archivo

Cuando el sistema carga los libros desde `biblioteca.txt`, se utiliza `.strip()`:

```python
datos = linea.strip().split("|")
```

- `.strip()` elimina los **espacios en blanco**, saltos de línea `\n` y tabulaciones que pueda tener la línea al final o inicio.  
- Esto asegura que los datos se procesen correctamente sin errores por caracteres “invisibles”.  

Ejemplo práctico:

```python
linea = "El Quijote|Cervantes|1605|disponible\n"
print(linea.split("|"))
# ['El Quijote', 'Cervantes', '1605', 'disponible\n']

print(linea.strip().split("|"))
# ['El Quijote', 'Cervantes', '1605', 'disponible']
```

Sin `.strip()`, el estado habría quedado como `"disponible\n"` con salto de línea incluido, lo que rompe las comparaciones.

## Hans Schiess

Desarrollado como actividad práctica de **Programación Orientada a Objetos**.  
Compatible con **Python 3.12.2**.
