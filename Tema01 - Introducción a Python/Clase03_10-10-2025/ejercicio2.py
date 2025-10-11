# Solicitar el nombre de un mes
# y mostar la cantidad de días que tiene ese mes
# Ejemplo -> abril
# Output -> 30

nombreMes = input('ingrese el mes: ')
meses = {
    'enero':31,
    'febrero':28,
    'marzo':31,
    'abril':30,
    'mayo':31
}
if nombreMes in meses.keys():
    print(meses[nombreMes])
else:
    print('El mes no existe')