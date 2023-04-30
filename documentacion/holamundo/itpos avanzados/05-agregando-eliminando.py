
mascotas = [
    "Pulga",
      "melisa",
        "chachito",
          "feliz", 
           "melisa"
           ]

mascotas.insert(1, "meliza triste")
mascotas.append("meliza feliz")# agrega un elemento al final        
print(mascotas)
mascotas.remove("melisa")
print(mascotas)

del mascotas[0]
print(mascotas)
print("-----", mascotas)



mascotas.clear()
print(mascotas)
