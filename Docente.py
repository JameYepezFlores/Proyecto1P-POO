from Persona import Persona


class Docente(Persona):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion)
        self._numero_libros = numero_libros

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, numero_libros):
        self._numero_libros = numero_libros

    def pedir_libro(self):
        if self._numero_libros < 10:
            self._numero_libros += 1
            return True
        return False

    def devolver_libro(self):
        if self._numero_libros > 0:
            self._numero_libros -= 1
            return True
        return False


if __name__ == "__main__":
    docente = Docente("987654321", "Livington", "Gallardo", "livi@example.com", "0987654321", "Avenida Principal", 8)

    # Obtener y modificar atributos de docente
    print(docente.nombre)
    docente.nombre = "samuel"
    print(docente.nombre)

    print(docente.numero_libros)
    docente.numero_libros = 10
    print(docente.numero_libros)

    # Llamar a los métodos pedir_libro() y devolver_libro()
    if docente.pedir_libro():
        print("Libro pedido exitosamente")
    else:
        print("No se puede pedir más libros")

    print("Número de libros:", docente.numero_libros)

    if docente.devolver_libro():
        print("Libro devuelto exitosamente")
    else:
        print("No hay libros para devolver")

    print("Número de libros:", docente.numero_libros)

    # Imprimir el objeto docente
    print(docente)