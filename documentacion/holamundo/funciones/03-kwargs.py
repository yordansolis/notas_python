def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])

get_product(id="9", 
            name="iPhone",
            color="red")    