
print('------------')
#actualiza los valores en mayuscula
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
    print(x.upper())
print('------------')

#Los objetos de lista tienen un sort()método que ordenará la
# lista de forma alfanumérica,
# ascendente, de forma predeterminada:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


print('------------')
#Para ordenar de forma descendente, use el
# argumento de palabra clave reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)



print('------------')

#Únete a dos listas:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


print('------------')
#Agregue list2 en list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)


#Use el extend()método para agregar list2 al final de list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

