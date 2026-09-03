class Libro:
    def __init__(self, titulo, autor, cantidad_paginas, estado_prestamo):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        self.estado_prestamo = estado_prestamo

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.cantidad_paginas}, Estado de préstamo: {self.estado_prestamo}"
    
    def prestar(self):
        if self.estado_prestamo == "disponible":
            self.estado_prestamo = "prestado"
            return True
        else:
            return False
    def devolver(self):
        if self.estado_prestamo == "prestado":
            self.estado_prestamo = "disponible"
            return True
        else:
            return False

def principal():
    libro1 = Libro("El Quijote", "Miguel de Cervantes", 863, "disponible")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417, "prestado")

    print(libro1)
    print(libro2)

    if libro1.prestar():
        print(f"Se ha prestado el libro: {libro1.titulo}")
    else:
        print(f"No se puede prestar el libro: {libro1.titulo}")

    if libro2.devolver():
        print(f"Se ha devuelto el libro: {libro2.titulo}")
    else:
        print(f"No se puede devolver el libro: {libro2.titulo}")

if __name__ == "__main__":
    principal()
    