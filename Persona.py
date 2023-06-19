from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @abstractmethod
    def pedir_libro(self):
        pass

    @abstractmethod
    def devolver_libro(self):
        pass

    def __str__(self):
        return f"{self._nombre} {self._apellido}"