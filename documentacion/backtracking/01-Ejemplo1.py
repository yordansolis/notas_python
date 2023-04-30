# A Python 3 program to
# demonstrate working of
# recursion 
#cuando la funcion vale 3 se le disminuye 1 y se vuenve a llamar asi misma
 
def printFun(test):
  
    if (test < 1):# primer identificar cuando se detenga 
        return
    else:
  
        print(test, end=" ")
        printFun(test-1)  # statement 2   -> esta funcion se llama asi mismo y va decrementando
        print(test, end=" ")#se imprimen los iterarios
        return
  
# Driver Code
test = 5
printFun(test)
  
# This code is contributed by
# Smitha Dinesh Semwal