from modelos.cliente import Cliente
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva
from modelos.excepciones import *
from utils.logger import registrar_log


print("=== SISTEMA SOFTWARE FJ ===\n")


# OPERACIÓN 1
try:

    cliente1 = Cliente("Pipe", "pipe@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 50000, 3)

    reserva1 = Reserva(cliente1, servicio1, 3)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

    registrar_log("Reserva confirmada correctamente")

except Exception as e:

    print(f"Error: {e}")

    registrar_log(f"ERROR: {e}")


print("\n-----------------\n")


# OPERACIÓN 2
try:

    cliente2 = Cliente("", "correo_invalido")

except Exception as e:

    print(f"Error detectado: {e}")

    registrar_log(f"ERROR cliente inválido: {e}")


print("\n-----------------\n")


# OPERACIÓN 3
try:

    servicio2 = AlquilerEquipo("Computador Gamer", 80000, 2)

    print(servicio2.descripcion())

    print(f"Costo: {servicio2.calcular_costo()}")

    registrar_log("Alquiler de equipo realizado")

except Exception as e:

    print(f"Error: {e}")

    registrar_log(f"ERROR: {e}")


print("\n-----------------\n")


# OPERACIÓN 4
try:

    servicio3 = AsesoriaEspecializada("Python", 100000, 0)

except Exception as e:

    print(f"Error detectado: {e}")

    registrar_log(f"ERROR asesoría: {e}")
    
   
print("\n-----------------\n")


# OPERACIÓN 5
try:

    cliente3 = Cliente("Ana", "ana@gmail.com")

    servicio4 = ReservaSala("Sala Ejecutiva", 70000, 5)

    reserva2 = Reserva(cliente3, servicio4, 5)

    print(reserva2.mostrar_reserva())

    registrar_log("Reserva pendiente creada")

except Exception as e:

    print(f"Error: {e}")

    registrar_log(f"ERROR: {e}")


print("\n-----------------\n")


# OPERACIÓN 6
try:

    servicio5 = AlquilerEquipo("", 50000, 1)

except Exception as e:

    print(f"Error detectado: {e}")

    registrar_log(f"ERROR servicio inválido: {e}")


print("\n-----------------\n")


# OPERACIÓN 7
try:

    cliente4 = Cliente("Carlos", "carlos@gmail.com")

    servicio6 = AsesoriaEspecializada("Java", 120000, 4)

    reserva3 = Reserva(cliente4, servicio6, 4)

    reserva3.cancelar()

    print(reserva3.mostrar_reserva())

    registrar_log("Reserva cancelada correctamente")

except Exception as e:

    print(f"Error: {e}")

    registrar_log(f"ERROR: {e}")


print("\n-----------------\n")


# OPERACIÓN 8
try:

    cliente5 = Cliente("Laura", "lauragmail.com")

except Exception as e:

    print(f"Error detectado: {e}")

    registrar_log(f"ERROR correo inválido: {e}")

else:

    print("Cliente creado correctamente")

finally:

    print("Operación de validación finalizada")


print("\n-----------------\n")


# OPERACIÓN 9
try:

    servicio7 = ReservaSala("Sala Premium", -50000, 2)

except Exception as e:

    print(f"Error detectado: {e}")

    registrar_log(f"ERROR precio inválido: {e}")


print("\n-----------------\n")


# OPERACIÓN 10
try:

    cliente6 = Cliente("Mario", "mario@gmail.com")

    servicio8 = AlquilerEquipo("Proyector", 40000, 3)

    reserva4 = Reserva(cliente6, servicio8, 3)

    reserva4.confirmar()

    print(reserva4.mostrar_reserva())

    registrar_log("Reserva final completada")

except Exception as e:

    print(f"Error: {e}")

    registrar_log(f"ERROR final: {e}") 