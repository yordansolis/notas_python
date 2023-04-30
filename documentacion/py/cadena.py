#La len()función devuelve la longitud de una cadena:
a = "Hello, mundo"
print(len(a))
#nos impri ellos
b = "Hello, World!"
print( "si  " +b[1:6])

print('---------------------')
#Compruebe si "gratis" está presente en el siguiente texto:

txt = "hola mundo aprendiendo python!"
print("python" in txt)


print('---------------------')

coco = "hola me gusta el coco !"
val = ("coco" in coco)
if val == True:
   print("jejej sii el coco ")


#ejemlo 2 
# print('---------------------')
# si  se encuentra oye imprima
# #
print('---------------------')

pescado = "oye comes pescado!"
if "oye" in pescado:
  print("Yes, 'free' pescado.")


  print('---------------------')

  #
  #inicia desde la posicion 1 y llega hasta la posicion 8
  #
  b = "Hello, World!"
print(b[1:8])

print('---------------------')
#
# El upper()método devuelve la cadena en mayúsculas:
# #
a = "Hello, World!"
print(a.upper())


#El lower()método devuelve la cadena en minúsculas:
# El strip()método elimina cualquier espacio en blanco desde el principio o el final:
print('---------------------')
a = "Hello, World!"
print(a.split(",")) 
#Asi conectamos cadenas 
print('---------------------')
a = "Hello"
b = "World"
c = a + " " + b
print(c)

print('---------------------')

#Use el format() metodo para conectar numeros en cadenas
age = 36
txt = "mi nombre es pablo is {}"
print(txt.format(age))


print('---------------------')
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))