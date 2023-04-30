// vemos el tipo de dato 
// y vemos la ubicacion  de la variable en la memoria 
a=5
type(a)
<class 'int'>
id(a)
1466051527024
a=8
id(a)
1466051527120
id(a)
1466051527120
id(8)
1466051527120
'referencia a la zona de memoria donde hay  un valor exacto'
'referencia a la zona de memoria donde hay  un valor exacto'
aH=1.5
type(aH)
<class 'float'>
a='hola';
type(a)
<class 'str'>
'los datos son imutables, no se pueden cambiar'
'los datos son imutables, no se pueden cambiar'

----------------  

text = "hola"
print(text)
hola
mivar=('a','b','c')
print(mivar)
('a', 'b', 'c')
id(mivar)
1631159143616
type(mivar)
<class 'tuple'>

*********************
mivar=('a','b','c')
print(mivar)
('a', 'b', 'c')
id(mivar)
1631159143616
type(mivar)
<class 'tuple'>
mivar[0]='h'
-----------
las listas si

lista = ['a','b','c']
print(lista)
['a', 'b', 'c']
lista[0] = 'p'
print(lista)
['p', 'b', 'c']
---------- 

asi podemos agregar algo a una lista 

----------
lista = ['a','b','c']
print(lista)
['a', 'b', 'c']
lista[0] = 'p'
print(lista)
['p', 'b', 'c']

lista.append('o')
lista.append('gaga','agua') // esto generara un error 
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lista.append('gaga','agua')
TypeError: list.append() takes exactly one argument (2 given)

//nota la forma correcta bes anexar 1  a  1 
lista.append('papa')
print(lista)
['p', 'b', 'c', 'o', 'papa']

//  asi sacamos algo de una lista 

lista.remove('p')
print(lista)
['b', 'c', 'o', 'papa']

// asi concadenamos 2 listas 

abc = ['a','b','c']
xyz =['papa','queso','sopa']
abc.append(xyz)
print(abc)
['a', 'b', 'c', ['papa', 'queso', 'sopa']]
abc.append(xyz)
print(abc)
['a', 'b', 'c', ['papa', 'queso', 'sopa'], ['papa', 'queso', 'sopa']]
 







