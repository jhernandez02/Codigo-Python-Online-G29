notas = (9,11,16,18,17,13,10,15,16,9,13,9,13)
total = len(notas)
print('Total de notas: ', notas)

# Hallamos cuantas veces se repite la nota 13
print('Cantidad de 13s:', notas.count(13))

# Hallamos la máxima nota
maxima_nota = max(notas)
print('Nota máxima:', maxima_nota)

# Hallamos la mínima nota
minima_nota = min(notas)
print('Nota mínima:', minima_nota)

# Hallamos cuantas veces se repite la nota mínima
print('Tota de notas mínimas:', notas.count(minima_nota))

# Hallamos el promedio de notas
suma_notas = sum(notas)
print('Suma de notas: ', suma_notas)
promedio_notas = suma_notas/total
print('Promedio Notas: ', promedio_notas)