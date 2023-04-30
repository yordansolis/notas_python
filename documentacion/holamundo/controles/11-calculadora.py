msj="""
Benvenidos a la calculadora
Para salir escribe Salir
Las operaciones son: sum , rest, mult, div
"""
print(msj)

resultado = ""

while True: 
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int (resultado)
        op = input ("Ingresa operacion: ")
        if op.lower() == "salir":
            break
        n2 = input("Ingresa suguiente numero")
        if n2.lower() == "salir":
            break
        n2= int(n2)

        if op.lower() == "suma":
            resultado += n2
        elif op.lower() == "rest":
           resultado -= n2  
        elif op.lower() == "milt":
           resultado *= n2 
        elif op.lower() == "div":
           resultado /= n2  
        else:
            print("Operacion no valida")       
            break

        print(f"el resultado es {resultado}")