class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible."

    def mostrar(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} - {self.autor} ({self.anio}) - {estado}"

class LibroDigital (Libro):
    def __init__(self, titulo, autor, anio, formato, tamañoMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamañoMB = tamañoMB 

    def prestar(self):
        return f"El libro digital '{self.titulo}' está disponible."
    
    def mostrar(self):
        return f"{self.titulo} - {self.autor} ({self.anio}) - Digital {self.formato} - {self.tamañoMB} MB"
    

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro.mostrar())

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro.mostrar())
        else:
            print("No se encontraron libros de ese autor.")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(libro.prestar())
                return
        print("Libro no encontrado.")

    
biblioteca = Biblioteca("Biblioteca Central")


libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
libro3 = LibroDigital("Como ser millonario", "Remigio Miranda", 2023, "PDF", 5)


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

print("LISTADO DE LIBROS")
biblioteca.listar_libros()

print("\nBUSCAR POR AUTOR")
biblioteca.buscar_por_autor("Gabriel García Márquez")

print("\nPRESTAR LIBRO FÍSICO")
biblioteca.prestar_libro("Cien Años de Soledad")

print("\nPRESTAR LIBRO DIGITAL")
biblioteca.prestar_libro("Python Básico")

print("\nLISTADO FINAL")
biblioteca.listar_libros()
