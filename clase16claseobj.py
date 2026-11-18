#crear una clase 
class Libro:
    pass

libro1= Libro()
print(type(libro1))

#crear constructor de la clase 
class Libro:
    def __init__(self, nombre, autor, estado,listalibros):
        self.nombre= nombre
        self.autor= autor
        self.estado= estado
        self.listalibros= listalibros
    def mostrar(self):
        print("nombre libro", self.nombre, "Autor", self.autor)
    def cambiar_estado(self, estado1):
        self.estado= estado1
    def mostrar_lista(self):
        for e in self.listalibros:
            print(e)
    def __str__(self):
        return f"nombre: {self.nombre},autor{self.autor}, estado {self.estado}"


libro2= Libro("python intermedio" ,"Sandoval", "Disponible",['python basico', 'python intermedio'])
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("prestado")
print(libro2)
libro2.estado="disponible"
print(libro2.nombre)
libro2.mostrar_lista()


