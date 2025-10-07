# Desarrollar un programa para una discoteca
# que pregunte por la edad del cliente
# y verifique si tiene dinero para pagar la entrada (S/20)
# Validar que el ciente sea mayor de edad 
# y tenga dinero suficiente

# Solicito los datos
edad = int(input('Edad: '))
dinero = int(input('Dinero: '))
# Validar el ingreso a la discoteca
if edad>=18 and dinero>20:
    print('Ingresas')
else:
    print('No puedes ingresar')
    