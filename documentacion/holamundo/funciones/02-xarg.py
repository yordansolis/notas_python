def suma(a , b):
    print(a + b)

suma(5, 8)    


def numeros(*num):
    result = 0 
    for n in num:
        result += n
    print(result)    

numeros(10, 10, 10, 10, 10, 10)      