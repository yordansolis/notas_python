animal = "chanCHito feliz"
print(animal.upper())
print(animal.lower())#covierte en minuscula
print(animal.capitalize())#pone solo la primera letra en mayuscula
print(animal.title())

perrito = "  perriTo feliz"
print(perrito)
print(perrito.strip())#elimina los spacios en los str
print(perrito.strip().capitalize())
print(perrito.find("To"))
print(perrito.find("z"))#devvuelve el indice donde se encuentra
print(perrito.replace("T", "t"))
print("pe" in  perrito)#devuelve un boolean
print("pe" not in  perrito)#devuelve false lo niega boolean

datos = "programas"
text= "l"

print(datos.find(text))#find nos sirve para buscar parametros 

if datos.find(text) > 0:
    print("true")
else:
    print("no encontro parametos")

