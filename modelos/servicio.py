from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not nombre.strip():
            raise ValueError("El servicio debe tener nombre")

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass