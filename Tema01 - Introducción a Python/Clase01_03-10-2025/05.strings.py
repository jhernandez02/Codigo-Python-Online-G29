mensaje = "Mi nuevo mensaje"
print(mensaje)
print('Primer caracter:', mensaje[0])
print('Primer espacio en blanco:', mensaje[2])
total = len(mensaje) # Obtenemos el total de caracteres
print('Total caracteres:', total)
print('Último caracter:', mensaje[total-1])
print('Penúltimo caracter:', mensaje[-2])

print('-----------------------')
mensaje = "Python es chevere"
print(mensaje)
print('Total caracteres:', len(mensaje))
# [start_index:stop_index:step]
print('mensaje[3:13:2] => ', mensaje[3:13:2])

print('-----------------------')
texto = "Mi nuevo MenSAJE"
print(texto)
print(texto.upper())    # convierte a mayúscula
print(texto.lower())    # convierte a minúscula
# convierte mayus a minus y minus a mayus
print(texto.swapcase())
# convierte todo a minus y mayus solo el primer caracter
print(texto.capitalize())