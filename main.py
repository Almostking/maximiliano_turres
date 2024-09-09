from collections import deque

class SistemaGestionColas:
    def __init__(self):
        self.colas = {}

    def tomar_turno(self, servicio, cliente):
        if servicio not in self.colas:
            self.colas[servicio] = deque()
        self.colas[servicio].append((cliente, len(self.colas[servicio]) + 1))

    def atender_cliente(self, servicio):
        if servicio in self.colas and self.colas[servicio]:
            cliente_atendido, numero_turno = self.colas[servicio].popleft()
            print(f"Cliente atendido en {servicio}: {cliente_atendido}, Turno: {numero_turno}")
            return cliente_atendido
        else:
            print(f"No hay clientes en la cola de {servicio}.")
            return None

# Crear una instancia del sistema de gestión de colas
sistema_colas = SistemaGestionColas()

# Interacción con la consola
while True:
    print("\nOpciones:")
    print("1. Tomar turno")
    print("2. Atender cliente")
    print("3. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        servicio = input("Ingrese el servicio (administracion, facturacion, tecnologia, mercadeo): ")
        cliente = input("Ingrese el nombre del cliente: ")
        sistema_colas.tomar_turno(servicio, cliente)
        print(f"Se ha tomado el turno para {cliente} en {servicio}.")

    elif opcion == "2":
        servicio = input("Ingrese el servicio a atender (administracion, facturacion, tecnologia, mercadeo): ")
        sistema_colas.atender_cliente(servicio)

    elif opcion == "3":
        print("Saliendo del sistema de gestión de colas. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")