
dominios = [1, 2, 3, 4, 5, 6, 7, 8, 9]
variables = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9']
asignacion = []

#verificar todas las restricciones y retornar verdadero si se cumplen las restricciones
def comprobar(pos_variable):
    
    if pos_variable == 0:

        if not asignacion[0] == 4:
             return False
    
        if len(asignacion) >= 3:
            if not asignacion[0] + asignacion[1] + asignacion[2] == 15:
                return False
    
        if not (asignacion[1] == asignacion[0] or asignacion[1] == asignacion[2]):
            return False

    if pos_variable == 1:
         
        print("n2")
        if len(asignacion) >= 3:
           if not asignacion[0] +  asignacion[1] + asignacion[2] == 15:
              return False

        if not (asignacion[1] == asignacion[0] or asignacion[1] == asignacion[2]):
              return False

    if pos_variable == 2:
        print("n3")
        
        if len(asignacion) >= 3:
          if not asignacion[0] + asignacion[1]+ asignacion[2] == 15:
            return False

        if not (asignacion[2] == asignacion[0] or asignacion[2] == asignacion[1]):
            return False

    if pos_variable == 3:
        print("n4")
        if len(asignacion) >= 5:
         if not asignacion[3] + asignacion[4] + asignacion[5] == 15:
            print("not n3&plus;n4&plus;n5 = 15")
         return False

    #  if not (asignacion[3] == asignacion[4] or asignacion[3] == asignacion[5]):
    # return False

        #if pos_variable == 4:
    # print("n5")
        #if not asignacion[pos_variable] == 5:
    # return False

    # if pos_variable == 5:
        #print("n6")
        #if len(asignacion) >= 5:
        #verificar la restriccion para la fila de n6
        #verificar la restriccion para la columna de n6
        #verificar que los valores de n6, n5, n4 sean diferentes
        #verificar que los valores de n6, n3, n9 sean diferentes
        pass

    return True

#recibe 2 parametros
def backtracking(pos_variable, pos_dominio):
    
    if pos_variable <= len(asignacion) - 1:
      asignacion[pos_variable] = dominios[pos_dominio]
    else:  
        asignacion.append(dominios[pos_dominio])


    #aqui imprimimos los valores
    print(asignacion)
    input()
    if comprobar(pos_variable):
        if len(set(asignacion)) == len(variables):
            return asignacion

        backtracking(pos_variable + 1, 0)
    else:
        if pos_dominio == len(dominios) - 1:
            domini_variable_anterior = dominios.index(asignacion[pos_variable - 1])
            print("Dominio anterior", domini_variable_anterior)
            asignacion.pop()
            backtracking(pos_variable - 1, domini_variable_anterior + 1)
        else:
            backtracking(pos_variable, pos_dominio + 1)

backtracking(0, 0)