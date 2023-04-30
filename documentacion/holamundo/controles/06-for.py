
#for numero in range(5):
#   print(numero, numero * "hola mundo ")

buscar = 10 
for numero in range(5):#range 5  es un iterable
    print(numero)
    if numero == buscar:
        print("encontrado" , buscar)
        break #detiene la ejecucuion 
else: 
    print("No encontrado :( ")