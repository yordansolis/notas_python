#Las listas se utilizan para almacenar varios elementos en una sola variable.


#asi unimos dos listas 
abc = ['a','b','c']
xyz =['papa','queso','sopa']
abc.append(xyz)
print(abc)

#Para determinar cuántos elementos tiene una lista, use la len()función:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print('-----------------')
list1 = ["abc", 34, True, 40, "male"]
print(list1)

print('-----------------')
#puede acceder a ellos consultando el número de índice:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print('-----------------')
#imprime el primer elemento del ultimo indice 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])




#Esto devolverá los artículos de la posición 2 a la 5.
#Recuerda que el primer ítem es la posición 0,
#y tenga en cuenta que el artículo en la posición 5 NO está incluido
print('-----------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print('-----------------')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print('-----------------')

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print('-----------------')
#remplazar el valor de un  elemto en especifico en una lista
thislist = ["queso", "pan", "heuvos","ron"]
thislist[1] = "atum"
print(thislist)


print('-----------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


print('-----------------')
#inserta un valor en especifico en una lista
thislist = ["quibdo", "istmina", "tado"]
thislist.insert(2, "LLOTO")
print(thislist) 


print('-----------------')
#Para agregar un elemento al final de la lista, use el método append() :

thislist = ["COCO", "CHOCOLATE", "cherry"]
thislist.append("AGUA")
print(thislist)

print('-----------------')
#Para agregar elementos de otra lista a la lista actual
thislist = ["apple", "banana"]
tropical = ["mango", "pineapple"]
thislist.extend(tropical)
print(thislist)


#El pop()método elimina el índice especificado.
print('-----------------')
thislist = ["MAC", "APPLE", "NOKIA"]
thislist.pop(1)
print(thislist)


#Si no especifica el índice, el pop()método elimina el último elemento.
#   -> thislist.pop() 
# #print(thislist)

print('-----------------')
#del ELIMINA LA LISTA
thislist = ["apple", "banana", "cherry"]
del thislist

#El clear()método vacía la lista.
#thislist.clear()

