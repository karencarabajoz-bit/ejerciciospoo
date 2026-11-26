class Medicamento:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Código: {self.codigo} | {self.nombre:<12} | Precio: ${self.precio:.2f}")

class Farmacia:
    def __init__(self):
        self.inventario = [
            Medicamento(101, "Paracetamol", 2.50),
            Medicamento(102, "Ibuprofeno", 3.80),
            Medicamento(103, "Amoxicilina", 7.20),
            Medicamento(104, "Loratadina", 4.10)
        ]

    def iniciar(self):

        while True:
            print("\n=== FARMACIA 'SAN JOSÉ' ===")
            for med in self.inventario:
                med.mostrar()
            print("-" * 35)
            print("1. Venta Normal (Precio + 12% IVA)")
            print("2. Venta con Descuento (20% de descuento)")
            
            opcion = input("Elija una opción (1 o 2): ")
            if opcion in ("1", "2"):
                break
            print(">> Opción inválida. Por favor, intente de nuevo.")

        codigo = int(input("\nIngrese el código del medicamento: "))
        encontrado = next((m for m in self.inventario if m.codigo == codigo), None)

        if encontrado:
            print(f"\nMedicamento: {encontrado.nombre}")
            print(f"Precio base: ${encontrado.precio:.2f}")
            
            if opcion == "1":
                total = encontrado.precio * 1.12
                print("Tipo: Venta Normal (+12% IVA)")
            else:
                total = encontrado.precio * 0.80
                print("Tipo: Venta con Descuento (-20%)")
                
            print(f"TOTAL A PAGAR: ${total:.2f}")
        else:
            print("El código ingresado no existe.")

if __name__ == "__main__":
    app = Farmacia()
    app.iniciar()