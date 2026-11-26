class Alimento:
    def __init__(self, codigo, nombre, peso_unidad,stock):
        self.codigo= codigo
        self.nombre= nombre
        self.peso_unidad= peso_unidad
        self.stock= stock

class Entrega:
    def __init__(self, numero, codigo_alimento, familia, cantidad, kg_entregados , fecha, estado="ACTIVA"):
        self.numero= numero
        self.codigo_alimento= codigo_alimento
        self.familia= familia
        self.cantidad= cantidad
        self.kg_entregados= kg_entregados
        self.fecha= fecha
        self.estado= estado

class BancoAlimentos:
    def __init__(self):
        self.alimentos= []
        self.entregas= []
        self.cargar()

        
