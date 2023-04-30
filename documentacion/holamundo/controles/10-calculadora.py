msj = """
Benvenidos a la calculadora
Para salir escribe Salir
Las operaciones son: sum , rest, mult, div
"""
salir = ""
print(msj)
valorG = ""

while True:
    if not valorG:
        valorG = input("Oye ingresa numero: ")
        if valorG.lower() == "salor":
         break
    valorG = int(valorG)

    operacion = input("Ingrese operacion: ")
    if operacion.lower() =="salir":
        break

    n2 = input("Ingrese el siguiente numero: ")
    if n2.lower() =="salir":
        break
    n2 = int (n2)
    if operacion.lower() == "suma":             
        valorG += n2
    elif operacion.lower() == "rest":   
        valorG -= n2
    elif operacion.lower() == "milt":           
        valorG *= n2
    elif operacion.lower() == "div":
        valorG /= n2
    else:
        print("El valor no es valido")
        break

    print(f"el valor es {valorG}")
