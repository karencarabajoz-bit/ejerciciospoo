notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25]
# Escriba su solución aquí
i= 0
suma= 0
aprobado= 0
nota_alta= notas[0]
nota_baja= notas[0]

for nota in notas :
 suma += nota #tenia agregado la lista de notas (notas )
 i+=1
   
 if nota >= 7.0:
     aprobado += 1

 if nota > nota_alta:
     nota_alta= 1

 if nota < nota_baja:
    nota_baja= nota

promedio= suma/ i
print(f"promedio: {promedio:.2f}")
print(f"nota mas alta: {nota_alta}")
print(f"nota mas baja:{nota_baja}")
print(f"aprobadas: {aprobado}")

#TAREA 
#menu usuario 



'''
FUNCIONES NORMAL
def  suma(  ):
      print("suma")___ instricicion 
    suma( )

CON PARAMETROS 
def suma(a,b):
    print(a+b)
suma(3,2)


def suma(a.b):
    return a+b
resultado = suma(5,3)
print(resultado)



def suma(*a.b):   -para tupla ** para diccionario 
    return a+b
resultado = suma(5,3)
print(resultado)

'''
















