from modelos.cliente import Cliente
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo
)
from modelos.reserva import Reserva
from utils.logger import registrar_log


while True:

    print("\n=== SOFTWARE FJ ===")
    print("1. Registrar cliente")
    print("2. Reservar sala")
    print("3. Alquilar equipo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCIÓN 1
    if opcion == "1":

        try:

            nombre = input("Ingrese nombre del cliente: ")
            correo = input("Ingrese correo: ")

            cliente = Cliente(nombre, correo)

            print("Cliente registrado correctamente")

            registrar_log("Cliente registrado")

        except Exception as e:

            print(f"Error: {e}")

            registrar_log(f"ERROR cliente: {e}")

    # OPCIÓN 2
    elif opcion == "2":

        try:

            nombre = input("Nombre del cliente: ")
            correo = input("Correo: ")

            cliente = Cliente(nombre, correo)

            horas = int(input("Horas de reserva: "))

            servicio = ReservaSala("Sala VIP", 50000, horas)

            reserva = Reserva(cliente, servicio, horas)

            reserva.confirmar()

            print("\nRESERVA EXITOSA")
            print(reserva.mostrar_reserva())

            registrar_log("Reserva de sala realizada")

        except Exception as e:

            print(f"Error: {e}")

            registrar_log(f"ERROR reserva: {e}")

    # OPCIÓN 3
    elif opcion == "3":

        try:

            nombre = input("Nombre del cliente: ")
            correo = input("Correo: ")

            cliente = Cliente(nombre, correo)

            dias = int(input("Días de alquiler: "))

            servicio = AlquilerEquipo(
                "Computador Gamer",
                80000,
                dias
            )

            reserva = Reserva(cliente, servicio, dias)

            print("\nALQUILER EXITOSO")
            print(reserva.mostrar_reserva())

            registrar_log("Alquiler realizado")

        except Exception as e:

            print(f"Error: {e}")

            registrar_log(f"ERROR alquiler: {e}")

    # OPCIÓN 4
    elif opcion == "4":

        print("Gracias por usar Software FJ")

        registrar_log("Sistema finalizado")

        break

    else:

        print("Opción inválida")