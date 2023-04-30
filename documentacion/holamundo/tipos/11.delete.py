
lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(5)

valor = 5

for value in lista: 
    if(value != valor):
        print("el valor random se puede registrar: ",value)
    else:
        print("error el value esta repetido", value)