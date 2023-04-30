#and cuando se tiengan dos condicines en Tru A Y B =2
#or si uno de los 2 es True devuelve true

gas = False 
encendido = True
edad = 18
if gas and encendido: 
    print("No puedes cocimar")

 
if gas or encendido: 
    print("Puedes cocinar sin gas")   



gas = True 
encendido = True
edad = 18

if gas and encendido and edad >= 18: 
    print("Eres mayor has lo que gustes")




gas = False 
encendido = True
edad = 18

if not gas and (encendido and edad > 17): 
    print("Puedes avanzar")





 
