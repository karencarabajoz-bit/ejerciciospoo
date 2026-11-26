class VistaBancoAlimentos:
    def mostrar_menu(self):
        print("\n ---BANCO DE ALOMENTOS PARROQUIAL---")
        print("1. Registrar Alimento ")
        print("2. Mostrar Alimentos ")
        print("3. Entregar a una familia ")
        print("4. Buscar por nombre ")
        print("5. Anular Entrega ")
        print("6. Mostrar Entrega ")
        print("7. Reporte General ")
        print("8. Salir")
        return input("Eliga una Opcion: ")

    def pedir_alimento(self):
        nombre= input("Ingrese el nombre del alimento ")