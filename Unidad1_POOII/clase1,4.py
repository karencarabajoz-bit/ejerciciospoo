#declaracion de funciona
'''
def saludar():
    print("hola karen")
saludar() 

# con parametros 

def calcular_edad(anio_nacimiento,anio_actual):
    print(f"la edad es : {anio_actual-anio_nacimiento}")


a= int(input("ingrese el año de nacimiento:"))
b= int(input("ingrese el año actial:"))
calcular_edad(a,b)

#finciones con retorno 
def calcular_iva(precio,valor_iva):
    return precio*valor_iva
resultado= calcular_iva(10,0.15)
print(resultado)

#funcion con valores por defecto 

def calcular_iva(precio,iva= 0.15):
    return precio*iva
resultado= calcular_iva(100)
print(f"el iva es : {resultado}")

resultado = calcular_iva(100, 0.14)
print(f"el iva es : {resultado}")

#listas 
def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print(F"el numero {e} es par")
        else :
            print(f"el numero {e} es impar")

lista_numeros= range (0,10)
calcular_par(lista_numeros)
# lista de pares
def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print(F"el numero {e} es par")
        else :
            print(f"el numero {e} es impar")

lista_numeros= range (0,10,2)
calcular_par(lista_numeros)


lista_numero= range(5,0,-1)
for e in lista_numero:
    print(e, end=(" "))

# funciones con tuplas 
def suma_numeros(*a):
    return sum(a)
print(suma_numeros(1,2,3))

#diccionarios 
def estudiantes(**lista_estudienates):
    for nombre, edad in lista_estudienates.items():
        print("el estudiente", nombre, "tiene",edad, "años")
estudiantes(veronica=20 , juan=67, maria=80, domenica=20, karen= 19, kevin=22, pablo= 20)
'''
#diccionarios 
def estudiantes(**lista_estudienates):
    suma_edades = 0
    for nombre, edad in lista_estudienates.items():
        print("el estudiente", nombre, "tiene",edad, "años")
        suma_edades += edad
    print(f"suma de edades{suma_edades}")
estudiantes(veronica=20 , juan=67, maria=80, domenica=20, karen= 19, kevin=22, pablo= 20)

print("+***************************************")



