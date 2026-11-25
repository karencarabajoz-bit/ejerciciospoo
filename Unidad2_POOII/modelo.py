class Medicamento:
    def __init__(self, codigo, nombre, precio, cajas):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cajas = cajas


    def validar_venta(self, cantidad):
        if cantidad <=0:
            return False, "La cantidad debe ser mayor a cero"
        if cantidad > self.cajas:
            return False, f"solo hay {self.cajas} cajas"
        return True,""

    def vender(self, cantidad):
        valido, mensaje = self.validar_venta(cantidad)
        if not valido:
            return False, mensaje
        self.cajas -= cantidad
        return True, self.cajas
    
    def __str__(self):
        return f"{self.nombre}(${self.precio:.2f})-{self.cajas} cajas"

class GestionMdicamento:
    def __init__(self):
        self.vender_medicamentos= []

    def registrar(self, nombre, precio, cajas):
        if nombre.strip()== "":
            return False ,"el nombre no puede estar vacio"
        if precio<= 0:
            return False, "el precio debe ser mayor a cero"
        if cajas <0:
            return False, "Las cajasa no pueden ser nagativo"

        codigo = len(self.vender_medicamento)+ 1
        self.medicamentos.append(Medicamento(codigo, nombre, precio, cajas))
        return True, codigo
    def buscar(self, codigo):
        for med in self.vender_medicamentos:
            if med.codigo == codigo:
                return True, med
        return False, "no existe ese codigo"

    def vender(self, codigo, cantidad):
        encontrado, resultado_busqueda= self.buscar(codigo)
        if not encontrado:
            return False, resultado_busqueda

        med = resultado_busqueda
        return med.vender(cantidad)
     
        





   
