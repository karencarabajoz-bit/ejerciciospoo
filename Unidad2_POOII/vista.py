class VistaFarmacia:
    def menu(self):
        print("\n=== FARMACIA 'SAN JOSÉ' ===")
        print("1. Registrar medicamentos " )
        print("2. Mostrar medicamento")
        print("3. Vender medicamento")
        print("4. Salir")
        return input("Seleccione una opcion: ").strip()

    def pedir_datos_registro(self):
        nombre = input("Nombre: ").strip()
        precio = input("Precio: ").strip()
        cajas = input("cajas: ").strip()
        return nombre, precio, cajas

    def pedir_datos_venta(self):
        codigo = input("codigo: ").strip()
        cantidad = input("Cantidad: ").strip()
        return codigo, cantidad 

    def mostrar_tabla(self, medicamentos):
        print(f"\n{'Codigo':<8}{'Nombre':<15}{'Precio':<10}{'Cajas':<6}  ")
        print("-"*40)
        for med in medicamentos:
            print(f"{med.codigo:<8}{med.nombre:<15}${med.precio:<9.2f}{med.cajas:<6}")
   
    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
        
            