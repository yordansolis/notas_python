dominios = [1, 2, 3, 4, 5, 6, 7, 8, 9]
variables = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9']
asignacion = []

# es importante seleccionar los if con orden para que se vayan seleccionando
# verificar todas las restricciones y retornar verdadero si se cumplen las restricciones
def comprobar(pos_variable):
    # el no sirve para negarme la asignacion es como si fuera difetente o igual
    # n1 != n2  & n1 != n3
    if pos_variable == 0:
        # si se es igual a 4 se detiene si pasa al segundo intervalo
        print("1. posicion")
        if not asignacion[0] == 4:
           return False
        return True

        if not asignacion[0] == asignacion[1] or asignacion[0] == asignacion[2]:
          return False

        if not asignacion[0] == asignacion[3]:
          return False

        if not asignacion[0] == asignacion[5] or asignacion[0] == asignacion[6]:
          return False

        if not asignacion[0] == asignacion[7] or asignacion[0] == asignacion[8]:
          return False

        if not asignacion[0] == asignacion[9]:
          return False



    # n3 != n1 & n3 != n2
    if pos_variable == 2:
        print("2. posi")
        if not asignacion[1] == 9:
           return False
        return True

        if not asignacion[1] == asignacion[0] or asignacion[1] == asignacion[1]:
            return False

        if not (asignacion[1] == asignacion[2] or asignacion[1] == asignacion[3]):
            return False

        if not (asignacion[1] == asignacion[4] or asignacion[1] == asignacion[5]):
            return False

        if not (asignacion[1] == asignacion[6] or asignacion[1] == asignacion[7]):
            return False
        if not asignacion[1] == asignacion[8]:
            return False


    if pos_variable == 3:
        print("3. posi")
        if not asignacion[2] == 2:
            return False
        return True

        if not (asignacion[2] == asignacion[0] or asignacion[2] == asignacion[1]):
            return False

        if not (asignacion[2] == asignacion[3] or asignacion[2] == asignacion[4]):
            return False

        if not (asignacion[2] == asignacion[5] or asignacion[2] == asignacion[6]):
            return False

        if not (asignacion[2] == asignacion[7] or asignacion[2] == asignacion[8]):
            return False

        if not asignacion[2] == asignacion[9]:
            return False


        # n6 != n3 & n6 != n9
    if pos_variable == 4:
        print("4. posi")
        if not asignacion[3] == 3:
            return False
        return True

        if not (asignacion[3] == asignacion[0] or asignacion[3] == asignacion[1]):
            return False

        if not (asignacion[3] == asignacion[2] or asignacion[3] == asignacion[4]):
            return False

        if not (asignacion[3] == asignacion[5] or asignacion[3] == asignacion[6]):
            return False

        if not (asignacion[3] == asignacion[7] or asignacion[3] == asignacion[8]):
            return False

        if not asignacion[3] == asignacion[9]:
            return False




        # n7 != n8 & n7 != n4
        # n7 != n1 & n7 != n9
    if pos_variable == 5:

        print("5. posi")
        if not asignacion[4] == 5:
            return False
        return True

        if not (asignacion[4] == asignacion[0] or asignacion[4] == asignacion[1]):
            return False

        if not (asignacion[4] == asignacion[2] or asignacion[4] == asignacion[3]):
            return False

        if not (asignacion[4] == asignacion[4] or asignacion[4] == asignacion[6]):
            return False

        if not (asignacion[4] == asignacion[7] or asignacion[4] == asignacion[8]):
            return False

        if not asignacion[4] == asignacion[9]:
            return False





    if pos_variable == 6:

        print("6. posi")
        if not asignacion[5] == 7:
          return False
        return True

        if not asignacion[5] == 1:
            return False


        if not asignacion[5] == asignacion[0]:
            return False

        if not (asignacion[5] == asignacion[2] or asignacion[5] == asignacion[3]):
            return False

        if not (asignacion[5] == asignacion[4] or asignacion[5] == asignacion[5]):
            return False

        if not (asignacion[5] == asignacion[6] or asignacion[5] == asignacion[8]):
            return False

        if not asignacion[5] == asignacion[9]:
            return False








    if pos_variable == 7:

        print("7. posi", pos_variable)
        if not asignacion[6] == 8:
            return False
        return True

        if not (asignacion[6] == asignacion[0] or asignacion[6] == asignacion[1]):
            return False

        if not (asignacion[6] == asignacion[2] or asignacion[6] == asignacion[3]):
            return False

        if not (asignacion[6] == asignacion[4] or asignacion[6] == asignacion[5]):
            return False

        if not asignacion[6] == asignacion[6] or asignacion[6] == asignacion[7]:
            return False

        if not asignacion[6] == asignacion[9]:
            return False


    if pos_variable == 8:

        print("8. posi" )

        if not asignacion[7] == 1:
            return False
        return True

        if not (asignacion[7] == asignacion[0] or asignacion[7] == asignacion[2]):
            return False

        if not (asignacion[7] == asignacion[3] or asignacion[7] == asignacion[4]):
            return False

        if not (asignacion[7] == asignacion[5] or asignacion[7] == asignacion[6]):
            return False

        if not (asignacion[7] == asignacion[7] or asignacion[7] == asignacion[8]):
            return False

        if not asignacion[7] == asignacion[9]:
            return False



    if pos_variable == 9:
        print("9. posi" )
        print("La posicion", asignacion)

        if not asignacion[8] == 6:
            return False
        return True

        if not (asignacion[8] == asignacion[0] or asignacion[8] == asignacion[1]):
            return False

        if not (asignacion[8] == asignacion[2] or asignacion[8] == asignacion[3]):
            return False

        if not (asignacion[8] == asignacion[4] or asignacion[8] == asignacion[5]):
            return False

        if not (asignacion[8] == asignacion[7] or asignacion[8] == asignacion[8]):
            return False

        if not asignacion[8] == asignacion[9]:
            return False


        # verificar la restriccion para la fila de n6
        # verificar la restriccion para la columna de n6
        # verificar que los valores de n6, n5, n4 sean diferentes
        # verificar que los valores de n6, n3, n9 sean diferentes
        pass

    return True


# recibe 2 parametros
def backtracking(pos_variable, pos_dominio):
    if pos_variable <= len(asignacion) - 1:
        asignacion[pos_variable] = dominios[pos_dominio]
    else:
        asignacion.append(dominios[pos_dominio])

    # aqui imprimimos los valores
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