#Haga que la función FirstReverse( str ) tome el parámetro str
#que se está pasando y devuelva la cadena en orden inverso. Por ejemplo: 
#si la cadena de entrada es "Hello World and Coders", entonces su programa
#debería devolver la cadena sredoC dna dlroW olleH 


def FirstReverse(strParam):
    texto_al_reves = ""
    for char in strParam:
        texto_al_reves = char + texto_al_reves
  # code goes here
    return texto_al_reves

# keep this function call here 
print(FirstReverse("coderbyte"))