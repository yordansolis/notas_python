class Solution: 
    """
        explicaccion de ring i [1, 3, 0, 2]
                    left d [2, 0, 3, 1]
    """
        #resolver
    def solvenNQuees(self, n: int) -> list[list[str]]:
        solutions =[]#solucion toma vacia
        state =[]#el estado igual
        self.search(state, solutions, n)#llamos la clase buscar para el parametro n
        return solutions #devolvemos la bucsqueda 

    #toma un estado y devuelve un valor boolean 
    #valido si un esado se puede usar como solicion final 
    #ninguna de las reinas puede atacarse entre ellas 
    def is_valid_state(self, state, n): #funcion de state valid
        # comprueba sin es una solcion valida
        return len(state) == n
        #busca una funcion recursova
        #verifica que si el estadom de una solicion es valida
    def get_candidates(self, state, n):#las r no pueden atacarse entre si
        if not state: #si el estado no esata vacio
            return range(n)
        
        #esta vacio proxima posicion en  llenar 
        position = len(state)#ya que esta la primera podemos colocar la segunda
        cantidates = set(range(n))
        #rechazamos los cantidatos
        for row, col in enumerate(state): #para que se enumere el estado
             #descartamos el idice de la columna si esta ocupad
             cantidates.discard(col)#el discard es como el remover
             dist = position - row
             #aqui condicionamos que las colunas no puedan ser atacadas
             cantidates.discard(col + dist)
             cantidates.discard(col - dist)
        return cantidates
    

        #buscar recursiva
    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):#si es true nos generara las soluciones
            #si es valida registra la solcion 
            state_string = self.state_to_string(state)#llama la  funcion
            solutions.append(state_string)
            # return  #luefo se insertara aqui 
            return 
        #si la solcion no es valida contruiremos buscando un candidato
        #aqui se agrega una condicion de candidato para la segunda reina
        for candidate in self.get_candidates(state, n):
            #recore
            state.append(candidate)#agregamos al candidato
            self.search(state, solutions, n)#hace una busca recursiva
            state.pop()#ponen el estado como el original vacio
    
    
    def state_to_string(self, state, n):
        #Output: [[".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret    
             
   
#print(solvenNQuees())
