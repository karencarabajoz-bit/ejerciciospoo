notas= [10,8,9,5]
#insertolista 
print(notas[1])
notas.append(20)
notas.insert(1,10)
print(len(notas))
print(max(notas))
print(min(notas))
notas.remove(9)
notas= sorted(notas)
print(notas[2:])
print(notas[:2])
print(notas[:-1])

meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

print(meses[0])
print(meses[-1])


estudiante={
    "cedula": "0107293910",
    "nombre": "karen",
    "correo": "karen@gmail.com",
    "celular": "09098787876",
    "notas":[10,8,9,8]

}
print(estudiante["cedula"])
print(estudiante.get("nombre"))
print(estudiante["celular"])

print(estudiante.keys())


conjuntosa={1,1,5,4,6,8}
conjuntosb={1,9,6,5,4}
print(conjuntosa & conjuntosb )





























