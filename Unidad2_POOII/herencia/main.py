from estudiante import Estudiante
from docente import Docente

estudiante= Estudiante("Karen", "Carabajo", "0107391930" , "0193838389", "karen@gmail.com", 19, "ricaurte", "TDSU", [8,9,7,8,9])
print(estudiante.validar_edad())
print(estudiante.promedio())

estudiante2= Estudiante("Dome", "Crespo", "0763474740" , "0193838349", "dom@gmail.com", 20, "rucaurte", "TDSU", [9,10,7,8,9])
print(estudiante2.validar_edad())
print(estudiante2.promedio())

estudiante3= Estudiante("camila", "Carabajo", "07345474740" , "019384569", "cami@gmail.com", 16, "rucaurte", "TDSU", [9,8,7,8,8])
print(estudiante3.validar_edad())
print(estudiante3.promedio())

estudiante4= Estudiante("kevin", "Chicaiza", "07345456740" , "0122345678", "kevin@gmail.com", 21, "cuenca", "TDSU", [9,10,10,8,8])
print(estudiante4.validar_edad())
print(estudiante4.promedio())

estudiante5= Estudiante("pancho", "val", "07234456740" , "0122545678", "pan@gmail.com", 17, "cuenca", "TDSU", [9,9,9,8,8])
print(estudiante5.validar_edad())
print(estudiante5.promedio())
print(estudiante5)


docente= Docente("veronica", "segarra","192929292","838383839","vero@gmail.com",40,"cuenca","base de datos", 20)
print(docente.validar_edad())
print(docente.calcular_salario())
print(docente)

docente2= Docente("diana", "romero","192929292","838383839","vero@gmail.com",40,"cuenca","base de datos", 20)
print(docente2.validar_edad())
print(docente2.calcular_salario())
print(docente2)

docente3= Docente("iliana", "correa","192929292","838383839","vero@gmail.com",40,"cuenca","base de datos", 20)
print(docente3.validar_edad())
print(docente3.calcular_salario())
print(docente3)

docente4= Docente("veronica", "chimbo","192929292","838383839","vero@gmail.com",40,"cuenca","base de datos", 20)
print(docente4.validar_edad())
print(docente4.calcular_salario())
print(docente4)

docente5= Docente("carmen", "tacuri","192929292","838383839","vero@gmail.com",40,"cuenca","base de datos", 20)
print(docente5.validar_edad())
print(docente5.calcular_salario())
print(docente5)

