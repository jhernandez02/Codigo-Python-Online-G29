tupla = (2, 4, "Paman Sports", (1,2), ("Futbol", 4, (5,8)))
print('elem1: ', tupla[0])
print('elem2: ', tupla[1])
print('elem3: ', tupla[2])
print('elem4: ', tupla[3])
print('elem5: ', tupla[4])

# Mostramos el primer y segundo de la tupla (1,2)
print(tupla[3][0]) # Output: 1
print(tupla[3][1]) # Output: 2

# Mostramos el primer y segundo de la tupla (5,8)
print(tupla[4][2]) # Output: => (5,8)
print(tupla[4][2][0]) # Output: => 5
print(tupla[4][2][1]) # Output: => 8