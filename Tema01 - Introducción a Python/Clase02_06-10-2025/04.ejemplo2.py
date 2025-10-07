# Tenemos una lista de invitados
# Cada invitado deberá brindra su nombre 
# y el programa debera indica si esta o no en la lista
invitados = ['Luis','Carlos','Miriam','Sara','Alan']
nombre = input('Ingrese su nombre: ')
existe = nombre in invitados
print('Permitir ingreso: ', existe)