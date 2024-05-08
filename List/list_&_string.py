a = 'udit'
b = list(a)
print(b)

ab = 'udit udit udit'
bc = ab.split()
print(bc)

abc = 'udit-udit-udit'
delimiter = '-'
bcd = abc.split(delimiter)
print(bcd)

print(delimiter.join(bcd))