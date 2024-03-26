# Cree un bucle For de Python.
for i in range(1,10):
  print(i)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(a,b,c):
  return a+b+c

suma(5,6,8)

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma = lambda a,b,c: a+b+c
print(suma(5,6,8))



#-Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for l_nombre in lista_nombre:
  if nombre in l_nombre:
    print(f"{nombre} está en la lista")
  else:
    print(f"{nombre} no está en la lista")