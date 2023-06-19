from Persona import Persona


class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion)
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, numero_libros):
        self._numero_libros = numero_libros

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    def pedir_libro(self):
        if self._activo and self._numero_libros < 5:
            self._numero_libros += 1
            return True
        return False

    def devolver_libro(self):
        if self._numero_libros > 0:
            self._numero_libros -= 1
            return True
        return False


if __name__ == "__main__":
    estudiante = Estudiante("123456789", "Domenica", "Anchundia", "dome@example.com", "1234567890", "Calle 123", 2,
                            True, "Ingeniería")
    # Obtener y modificar atributos de estudiante
    print(estudiante.nombre)
    estudiante.nombre = "Maylin"
    print(estudiante.nombre)

    print(estudiante.numero_libros)  # 2
    estudiante.numero_libros = 4
    print(estudiante.numero_libros)  # 4

    # Llamar a los métodos pedir_libro() y devolver_libro()
    if estudiante.pedir_libro():
        print("Libro pedido exitosamente")
    else:
        print("No se puede pedir más libros")

    print("Número de libros:", estudiante.numero_libros)

    if estudiante.devolver_libro():
        print("Libro devuelto exitosamente")
    else:
        print("No hay libros para devolver")

    print("Número de libros:", estudiante.numero_libros)

    # Imprimir el objeto estudiante
    print(estudiante)