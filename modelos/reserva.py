class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Cancelada":
            raise Exception("No se puede confirmar una reserva cancelada")

        self.estado = "Confirmada"

    def cancelar(self):

        if self.estado == "Confirmada":
            raise Exception("No se puede cancelar una reserva confirmada")

        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.descripcion()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo: {self.servicio.calcular_costo()}"
        )