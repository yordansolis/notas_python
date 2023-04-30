# la serie de fibonaci es la que se suma el numero actual por el numero anterior

#lo funcion va a ejercutarse hasta cuando sea 0
def fibonaci(n):

    if (n == 0):
       return 0
    if (n == 1 or n == 2):
        return 1 
    else:     
        return   fibonaci(n - 1) + fibonaci(n - 2)# 4 + 3

n = 5

print("Fibonacci series of 5 numbers is :",end=" ")
  
# for loop to print the fibonacci series.
for i in range(0,n): 
  
    print(fibonaci(i),end=" ")# 0 ,1 ,2 ,3, 4 ,5 

