'''
Una expresión generadora en Python es una forma concisa de crear un generador, 
un tipo especial de iterador. 
A diferencia de las comprensiones de lista que usan corchetes [], 
las expresiones generadoras usan paréntesis (). 
Esto permite generar valores uno por uno (bajo demanda), 
en lugar de construir una lista completa en memoria, 
lo que las hace muy eficientes en cuanto a memoria, 
especialmente con grandes conjuntos de datos. 
'''
lista = [10,20,30,40,50]
# Expresión generadora (crea un generador, no una lista)
generador = (x**2 for x in range(10))
print(type(generador))
print(generador)
print(next(generador)) # Output: 0 => 0^2
#print(next(lista)) # Error, no se puede
print(next(generador)) # Output: 1 => 1^2
print(next(generador)) # Output: 4 => 2^2
print(next(generador)) # Output: 9 => 3^2

numero = 40
encontrado = False
'''
for item in lista:
        if(item==numero):
            encontrado = True
            break
'''
generador2 = (True for item in lista if item==numero)
encontrado = next(generador2, False)
print('encontrado:',encontrado)
