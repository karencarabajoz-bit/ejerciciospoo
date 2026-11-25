class controladorFarmacia:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.menu()

            if opcion == "1":
                try:
                    nombre, precio, cajas = self.vista.pedir_datos_registro()
                    ok, resultado = self.modelo.registrar( nombre, float(precio), int(cajas) )
                    if ok:
                        self.vista.mostrar_mensaje(
                            f"Registrado con el código {resultado}."
                        )
                    else:
                        self.vista.mostrar_error(resultado)
                except ValueError:
                    self.vista.mostrar_error("Ingrese valores numéricos válidos.")

            elif opcion == "2":
                try:
                    self.vista.mostrar_tabla(self.modelo.medicamentos)
                except ValueError:
                    self.vista.mostrar_error("tabla vacia")

            elif opcion == "3":
                try:
                    codigo, cantidad = self.vista.pedir_datos_venta()
                    ok, resultado = self.modelo.vender(int(codigo), int(cantidad))
                    if ok:
                        self.vista.mostrar_mensaje( f"Venta realizada. Quedan {resultado} cajas.")
                    else:
                        self.vista.mostrar_error(resultado)
                except ValueError:
                    self.vista.mostrar_error("Ingrese valores numéricos válidos.")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Hasta pronto.")

            else:
                self.vista.mostrar_mensaje("Opción no válida.")