import random

#numero aleatorio
num = random.randint(0, 9)
#print(num)

num = random.random()
#print(num)



#generar un elemento aleatorio de una lista

lista = ['manzana', 'banana', 'cereza']
elemento = random.choice(lista)
#print(elemento)

lis = "post"
n1= 1
lista = []
valor = random.randint(n1, 150000)
lista.append(valor)
for value in lista: 
    if(value != lista):
        agregar = f"{lis}{valor}"
        print("el valor random se puede registrar: ",agregar)
    else:
        print("error el value esta repetido", value)



for x in [0, 1, 2]:
  pass# para evitar recibir un error.





lista = ['manzana', 'banana', 'cereza', 'dátiles', 'uvas']
muestra = random.sample(lista, 3)
#print(muestra)