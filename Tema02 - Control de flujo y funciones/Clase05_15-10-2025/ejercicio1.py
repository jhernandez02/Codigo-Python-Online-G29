# Elabore una función que tome como argumento
# dos números enteros y devuelva el mayor
# Ej 10 y 5 => 10
def devolverMayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input('Número1: '))
num2 = int(input('Número2: '))
numMayor = devolverMayor(num1,num2)
print("El número mayor es:", numMayor)
