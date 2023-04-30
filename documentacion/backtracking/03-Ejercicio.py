# escriba un programa donde el factuarail de n sea >2 
#5! = 5 x 4 x 3 x 2 x 1 = 120
#la idea es que se vaya decrementando hasta cuando llegue a 0 or 0

def factorial(n):
 # n se guarda en la pila con el valor de 5 y se va ir decrementando 
    if (n == 0 or n == 1):#cuando => n=0 or n=1    :la funcion se detiene
        return 1         
    else:
        return  n * factorial(n - 1)#esta funcion va ir decrementando  5,4 3,2,1 hasta que llegue a 1 
                                    #f(n -1)SU VALOR INICIAL = 4
                                    #n = 5      

if __name__=='__main__':
    n=5
    print("el facotrial de ", n , " is" , factorial(n))