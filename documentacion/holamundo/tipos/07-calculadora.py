n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa segundo numero: ")

n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
el restado de la suma es {suma}.
el restado de la resta es {resta}.
el restado de la multiplicacion es {mult}.
el restado de la division es {div}.
"""
print(mensaje)

msj = f"""
    *
*********
 *******
  *****
   ***
    *
"""
print(msj)

print("-------------------------")
juego =  "   *"
print(juego)
print(juego.strip() * 7)
print("",juego.strip()*5)
print(" ",juego.strip()*3)
print("  ",juego.strip())
