print('--Ejemplo Bucle--')
pacientes = ('Silvia','Carlos','Miguel','Karen','Luis','Ana')
atendidos = 0 # 1,2,3,4,5,6
totalPacientes = len(pacientes) # 6
print('totalPacientes:', totalPacientes)

while atendidos<totalPacientes:
    print('atendidos:', atendidos)
    print('Atendiendo a', pacientes[atendidos])
    atendidos += 1
    print('---------------')

print('Pacientes atendidos:', atendidos)