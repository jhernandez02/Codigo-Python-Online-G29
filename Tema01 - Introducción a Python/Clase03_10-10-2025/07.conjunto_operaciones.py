deportesSet1 = {'fútbol','tennis','voley','natación'}
deportesSet2 = {'fútbol','voley','baseball','judo'}

print('--Intersección--')
print('&:', deportesSet1 & deportesSet2)
print('intersection(): ', deportesSet1.intersection(deportesSet2))

print('--Unión--')
print('|:', deportesSet1 | deportesSet2)
print('union():', deportesSet1.union(deportesSet2))

print('--Diferencia--')
print('deportesSet1:', deportesSet1)
print('deportesSet2:', deportesSet2)
print('set1.diff(set2):', deportesSet1.difference(deportesSet2))
print('set2.diff(set1):', deportesSet2.difference(deportesSet1))

print('--Suma de diferencias--')
print('^:', deportesSet1 ^ deportesSet2)