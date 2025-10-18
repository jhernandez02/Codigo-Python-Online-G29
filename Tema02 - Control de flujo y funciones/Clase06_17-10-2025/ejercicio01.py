# Crear un programa en Python, que lea el nombre de un curso, 2 notas (calificaciones),
# que calcule el promedio y la condición de aprobado si el promedio es igual o mayor a 13.

nombreCurso = input('Curso: ')
nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))

promedio = (nota1+nota2)/2
print("Promedio:",promedio)

if promedio<13:
    print('Desaprobado')
else:
    print('Aprobado')