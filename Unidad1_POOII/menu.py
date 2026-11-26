
def mostrar_titulo(numero):

    print("PREGUNTA", numero)


def pregunta_1():
    mostrar_titulo(1)  
    print("¿Qué imprime el siguiente código?")
    print('print("ab" * 3)')  
    print("Respuesta correcta: ababab")
    print("Explicación: el operador * repite una cadena.")


def pregunta_2():
    mostrar_titulo(2)
    print("¿Qué imprime el siguiente código?")
    print("print(type(10.0))")
    print("Respuesta correcta: <class 'float'>")
    print("Explicación: 10.0 tiene punto decimal, por eso es float.")


def pregunta_3():
    mostrar_titulo(3)
    print("¿Qué imprime el siguiente código?")
    print('frase = "aprendo Python en TEC"')
    print("print(len(frase.split()))")
    print("Respuesta correcta: 4")
    print("Explicación: split() separa por espacios y devuelve una lista de 4 palabras.")


def pregunta_4():
    mostrar_titulo(4)
    print("¿Qué imprime el siguiente código?")
    print("print(int(9.99))")
    print("Respuesta correcta: 9")
    print("Explicación: int() corta los decimales, no redondea.")


def pregunta_5():
    mostrar_titulo(5)
    print("¿Qué imprime el siguiente código?")
    print("a = [1, 2, 3]")
    print("b = a")
    print("b[0] = 5")
    print("print(a)")
    print("Respuesta correcta: [5, 2, 3]")

    print("Explicación: b = a no copia la lista; ambas variables apuntan a la misma lista.")


def pregunta_6():
    mostrar_titulo(6)
    print("¿Qué imprime el siguiente código?")
    print("saldo = 350")
    print("if saldo >= 1000:")
    print('    print("Oro")')
    print("elif saldo >= 100:")
    print('    print("Plata")')
    print("else:")
    print('    print("Básica")')
    print("Respuesta correcta: Plata")
   
    print("Explicación: 350 no es >= 1000, pero sí es >= 100.")


def pregunta_7():
    mostrar_titulo(7)
    print("¿Qué imprime el siguiente código?")
    print("total = 0")
    print("n = 1")
    print("while n <= 5:")
    print("    total += n")
    print("    n += 1")
    print("print(total)")
    print("Respuesta correcta: 15")
  
    print("Explicación: se suma 1 + 2 + 3 + 4 + 5 = 15; con n = 6 la condición es falsa.")


def pregunta_8():
    mostrar_titulo(8)
    print("¿Qué imprime el siguiente código?")
    print('notas = {"Ana": 10, "Luis": 8}')
    print("for nombre, nota in notas.items():")
    print('    print(f"{nombre}:{nota}", end=" ")')
    print("Respuesta correcta: Ana:10 Luis:8")
  
    print('Explicación: end=" " evita el salto de línea y deja un espacio entre cada resultado.')


def pregunta_9():
    mostrar_titulo(9)
    print("¿Qué imprime el siguiente código?")
    print("suma = 0")
    print("for n in range(1, 5):")
    print("    if n % 2 != 0:")
    print("        continue")
    print("    suma += n")
    print("print(suma)")
    print("Respuesta correcta: 6")
    print("Explicación: continue salta los impares; se suman solo 2 y 4.")


def pregunta_10():
    mostrar_titulo(10)
    print("¿Qué imprime el siguiente código?")
    print("for n in [1, 2, 3, 4]:")
    print("    if n == 3:")
    print("        break")
    print('    print(n, end=" ")')
    print("Respuesta correcta: 1 2")
 
    print("Explicación: cuando n vale 3, break termina el ciclo antes de imprimir.")


def pregunta_11():
    mostrar_titulo(11)
    print("Ejercicio 3. Estadística de notas")
    print("Dada la lista notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25],")
    print("calcule con un ciclo (sin usar sum, max ni min): el promedio con")
    print("2 decimales, la nota más alta, la más baja y cuántos estudiantes")
    print("aprobaron (nota >= 7).")

    notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25]

    contador = 0          
    suma = 0               
    aprobados = 0          
    nota_alta = notas[0]    
    nota_baja = notas[0]   

    for nota in notas:
        suma += nota        
        contador += 1      

        if nota >= 7:       
            aprobados += 1  

        if nota > nota_alta:    
            nota_alta = nota    

        if nota < nota_baja:   
            nota_baja = nota    

   
    promedio = suma / contador

    print("\nRespuesta correcta:")
    print("Promedio:", round(promedio, 2))
    print("Nota más alta:", nota_alta)
    print("Nota más baja:", nota_baja)
    print("Aprobados:", aprobados)

def mostrar_submenu():
    print("\n===== SUBMENÚ DE PREGUNTAS =====")

    for numero in range(1, 12):
        print(str(numero) + ". Pregunta " + str(numero))

    print("12. Regresar al menú principal")


def submenu_preguntas():
    opcion = ""

    while opcion != "12":
        mostrar_submenu() 

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            pregunta_1()    
        elif opcion == "2":
            pregunta_2()
        elif opcion == "3":
            pregunta_3()
        elif opcion == "4":
            pregunta_4()
        elif opcion == "5":
            pregunta_5()
        elif opcion == "6":
            pregunta_6()
        elif opcion == "7":
            pregunta_7()
        elif opcion == "8":
            pregunta_8()
        elif opcion == "9":
            pregunta_9()
        elif opcion == "10":
            pregunta_10()
        elif opcion == "11":
            pregunta_11()
        elif opcion == "12":
            print("Regresando al menú principal...")
        else:
            print("Opción no válida. Intente de nuevo.")



def ingresar_nombre():
    nombre = input("Ingrese su nombre: ")
    print("¡Bienvenido/a,", nombre + "!")
    return nombre



def menu_principal():
    nombre = ""  
    opcion = "" 

    while opcion != "3":
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ingresar nombre")
        print("2. Submenú de preguntas")
        print("3. Salir del programa")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = ingresar_nombre()
        elif opcion == "2":
            submenu_preguntas()
        elif opcion == "3":
            if nombre == "":
                print("¡Hasta luego!")
            else:
                print("¡Hasta luego,", nombre + "!")
        else:
            print("Opción no válida. Intente de nuevo.")

menu_principal()