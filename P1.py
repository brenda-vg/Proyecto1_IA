"""
Nombre del programa: P1.py
Autor: Valdez Guzman Brenda
Fecha de creación: 2024-03-31
Version: 1.0

Descripción:
Este programa realiza el metodo de ucs paso a paso a través del mapa de Rumania

Uso:
Para ejecutar el programa, simplemente ejecuta este archivo Python desde la línea de comandos.
Utiliza 1 para la ejecución estandar, 2 para otras opciones de ejecucion

Requisitos:
Este programa requiere Python 3.x para ejecutarse.

"""

import heapq        # To use the priority queue
import itertools    # To check for all city combinations
import sys          # To finish the execution in the testing mode

class WeightedGraph:
    """
    Descripción:
    Esta clase representa un grafo ponderado no dirigido.

    Atributos:
    - graph: Un diccionario que tiene como llaves la ciudad, y como valores un segundo diccionario.
    Dicho segundo diccionario tiene como llaves los destinos a los que va a partir de dicha ciudad y el peso a dicho destino

    Métodos:
    - add_vertex(self, vertex): Agrega un vertice al grafo (al diccionario graph) en caso de no existir previamente
    - add_edge(elf, source, destination, weight): Agrega una arista al grafo, esto es, el camino entre source y destination, y cuánto pesa dicho camino.
            En un grafo no dirigido, agrega la arista a ambos diccionarios de vertices
    - get_vertices(self): Regresa una lista con todas las llaves (vertices) del diccionario graph
    - get_edges(self): Regresa una lista con todas las tuplas de la forma 'origen,destino,peso' (aristas)
    """
    def __init__(self):
        """
        Descripción:
        Constructor de la clase WeightedGraph.

        Parámetros:
        - graph: Un diccionario que tiene como llaves la ciudad, y como valores un segundo diccionario.
        Dicho segundo diccionario tiene como llaves los destinos a los que va a partir de dicha ciudad y el peso a dicho destino

        Es decir, graph tiene un diccionario de la forma
        {origen1: {destino1:valor1, destino2:valor2, ..., destino_n:valor_n }, origen2: {destino2_1:valor2_1, destino2_2:valor2_2, ..., destino2_n:valor2_n }}
        """

        self.graph = {}

    def add_vertex(self, vertex):
        """
        Descripción:
        Este método agrega un vertice al grafo en caso de no encontrarse previamente en él. Lo hace creando su diccionario

        Parámetros:
        - vertex: Una cadena (str) con el nombre del vértice
        """

        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, source, destination, weight):
        """
        Descripción:
        Este método agrega una arista al grafo.
        Para ello, primero agrega ambos vertices al grafo, y posteriormente agrega a ambos
        diccionarios el otro vértice como destino con el correspondiente peso

        Parámetros:
        - source: Uno de los vertices, en formato cadena (str)
        - destination: El otro vertice, en formato cadena (str)
        - weight: El peso entre ambos vertices, en formato entero (int)
        """
        self.add_vertex(source)
        self.add_vertex(destination)
        self.graph[source][destination] = weight
        self.graph[destination][source] = weight  # If it's undirected, add this line. Otherwise, erase it

    def get_vertices(self):
        """
        Descripción:
        Este método regresa una lista con todos los vertices del grafo.

        Parámetros:
        - No recibe ningun parámetro.

        Devolución:
        El valor devuelto son los vertices del grafo.
        Es de tipo lista (list), los valores de la lista son los vertices y son de tipo cadenas (str)
        """
        return list(self.graph.keys())

    def get_edges(self):
        """
        Descripción:
        Este método regresa una lista con todas las aristas del grafo.

        Parámetros:
        - No recibe ningun parámetro.

        Devolución:
        El valor devuelto son las aristas del grafo.
        Es de tipo lista (list), los valores de la lista son las aristas y son de tipo tuplas (tuple).
        Los valores de la tupla son (origen, destino, peso); Los tipos de la tupla son (str,str,int). 
        """
        edges = []
        for source in self.graph:
            for destination, weight in self.graph[source].items():
                edges.append((source, destination, weight))
        return edges

def uniform_cost_search(graph_i, start, goal):
    """
    Descripción:
    Esta función ejecuta una busqueda de costo uniforme a partir de un grafo, un vertice de inicio y un vertice de meta

    Parámetros:
    - graph_i: Recibe una instancia de WeightedGraph
    - start: Recibe una ciudad de inicio (str)
    - end: Recibe una ciudad de llegada (str)

    Devolución:
    Devuelve una tupla con dos valores de tipo (int,str), de la forma (costo, trayectoria)
    """
    step = 0
    frontier = [(0, start, start)]  # Priority queue of (cost, node)
    explored = set()
    cost_so_far = {start: 0} # Dictionary to track lowest cost to each node

    if FLAG_PRINT:
        print('------------------ Paso: {level} \t - \t Ciudades exploradas: {node}'.format(level=step,node=''))
        print('Costo:\tTrayectoria')
        print('{costo}:\t{path}'.format(costo=0,path=start))
        print()

    while frontier:
        cost, current_node, prev_path = heapq.heappop(frontier)

        step += 1

        if current_node == goal:
            return cost, prev_path

        # If the currend node was not explored, we explore it.
        if current_node not in explored:
            explored.add(current_node)

            for neighbor, weight in graph_i.graph[current_node].items():
                if neighbor not in explored:

                    new_cost = cost+weight
                    new_path = '{previous}-{appended}'.format(previous=prev_path,appended=neighbor)

                    # This line makes that you can't add costlier paths to an already reached destination
                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        if neighbor in cost_so_far:
                            if FLAG_PRINT:
                                print('The previous cost to {n} was {pc}, now it is {nc} \nWe erase the previous path to {n}'.format(n=neighbor,pc =cost_so_far[neighbor], nc=new_cost, pp=prev_path))
                        cost_so_far[neighbor] = new_cost
                        # Remove previous path from the frontier if it exists
                        # Creates a whole new frontier but only includes the ones that are not the neighbor
                        frontier = [(c, n, p) for c, n, p in frontier if n != neighbor]


                        # If you don't want that feature, you erase the lines above but this push must be maintained
                        heapq.heappush(frontier, (new_cost, neighbor, new_path))
        else:
            #TODO: Note: Due to the condition that avoid several costlier paths to reached cities,
            # now it is impossible to reach this condition. However, if the mentioned condition was removed,
            # this line would be necessary
            print('THIIIIIIIIIIS was already explored')
            print(current_node)

        if FLAG_PRINT:
            # Once the frontier is completely updated, we print it
            # If the current node was ALREADY explored, we print the frontier nonetheless 
            print('------------------ Paso: {level} \t - \t Ciudades exploradas: {node}'.format(level=step,node=current_node))
            print('Costo:\tTrayectoria')
            for element in frontier:
                print('{costo}:\t{path}'.format(costo=element[0],path=element[2]))
            print()

    return float('inf'),''  # If goal is not reachable

def RomaniaFill():
    """
    Descripción:
    Esta función crea un grafo graph_i y lo llena con el mapa de Rumania.
    Para usar un grafo distinto, no usar esta funcion

    Parámetros:
    No recibe parámetros.

    Devolución:
    Devuelve una instancia de WeightedGraph con el grafo del mapa de Rumania.

    """
    graph_i = WeightedGraph()

    graph_i.add_edge('Oradea', 'Zerind', 71)
    graph_i.add_edge('Oradea', 'Sibiu', 151)
    graph_i.add_edge('Zerind', 'Arad', 75)
    graph_i.add_edge('Arad', 'Timisoara', 118)
    graph_i.add_edge('Arad', 'Sibiu', 140)
    graph_i.add_edge('Timisoara', 'Lugoj', 111)
    graph_i.add_edge('Sibiu', 'Rimnicu Vilcea', 80)
    graph_i.add_edge('Sibiu', 'Fagaras', 99)
    graph_i.add_edge('Lugoj', 'Mehadia', 70)
    graph_i.add_edge('Rimnicu Vilcea', 'Craiova', 146)
    graph_i.add_edge('Rimnicu Vilcea', 'Pitesti', 97)
    graph_i.add_edge('Fagaras', 'Bucharest', 211)
    graph_i.add_edge('Mehadia', 'Dobreta', 75)
    graph_i.add_edge('Dobreta', 'Craiova', 120)
    graph_i.add_edge('Craiova', 'Pitesti', 138)
    graph_i.add_edge('Pitesti', 'Bucharest', 101)
    graph_i.add_edge('Bucharest', 'Giurgiu', 90)
    graph_i.add_edge('Bucharest', 'Urziceni', 85)
    graph_i.add_edge('Urziceni', 'Hirsova', 98)
    graph_i.add_edge('Urziceni', 'Vaslui', 142)
    graph_i.add_edge('Hirsova', 'Eforie', 86)
    graph_i.add_edge('Vaslui', 'Iasi', 92)
    graph_i.add_edge('Iasi', 'Neamt', 87)

    return graph_i

def get_problem(graph_i):
    """
    Descripción:
    Esta función pide al usuario que elija una ciudad de inicio y una ciudad de llegada.

    Parámetros:
    - graph_i: Recibe una instancia de WeightedGraph para verificar que los vertices pertenezcan al grafo a trabajar

    Devolución:
    Devuelve una tupla con dos valores de tipo (str,str), de la forma (ciudad_inicio, ciudad_llegada)
    """
    start_vertex = end_vertex = 'False' #This line is to simulate a do-while instead of a while

    #This keeps asking for a start_vertex until the vertex given is part of the vertices
    while start_vertex not in graph_i.get_vertices():
        start_vertex = input('¿Desde qué ciudad desea partir? ')

    #This keeps asking for an end_vertex until the vertex given is part of the vertices
    while end_vertex not in graph_i.get_vertices():
        end_vertex = input('¿A qué ciudad desea llegar? ')

    return start_vertex, end_vertex

def check_combinations(graph_i):
    """
    Descripción:
    Esta función busca la trayectoria y costo de todos los pares de ciudades posibles en el grafo.

    Parámetros:
    - graph_i: Recibe una instancia de WeightedGraph

    Devolución:
    No devuelve ningún valor, imprime todos los resultados.
    """
    city_pairs = get_city_pairs(graph_i.get_vertices())
    print("Pares de ciudades:")
    for pair in city_pairs:
        if FLAG_PRINT:
            print('-----------------------------------------------------------------------')
        print()
        print(pair)
        #Notemos que revisa en ambos ordenes (de A a B y de B a A)
        #porque el algoritmo explora aristas distintas dependiendo de la dirección 

        #Revisa de la ciudad0 a la ciudad1
        cost,path = uniform_cost_search(graph_i,pair[0],pair[1])
        if FLAG_PRINT:
            print('La solucion es: ',end='')
        print(cost,path)
        if FLAG_PRINT:
            print('\n\n')

        #Revisa de la ciudad1 a la ciudad0
        cost,path = uniform_cost_search(graph_i,pair[1],pair[0])
        if FLAG_PRINT:
            print('La solucion es: ',end='')
        print(cost,path)
        if FLAG_PRINT:
            print('\n\n')

def get_city_pairs(city_list):
    """
    Descripción:
    Esta función genera todas las combinaciones posibles que tengan 2 elementos

    Parámetros:
    - city_list: Una lista de todos los vertices de un grafo

    Devolución:
    Devuelve una lista (list) cuyos valores son tuplas (tuple) con dos elementos (ciudad1, ciudad2) de tipos (str,str)
    """

    # Generar todas las combinaciones posibles de 2 elementos (pares)
    city_pairs = list(itertools.combinations(city_list, 2))
    return city_pairs

# GLOBAL VARIABLES
# Esta variable en True genera las busquedas paso a paso, en False imprime unicamente el costo y la trayectoria
FLAG_PRINT = True


def main():     # The graph instance used is the RomaniaFill() and asks for two cities
    """
    Descripción:
    Esta función usa el grafo de Rumania y pregunta por dos ciudades, ejecuta la busqueda paso a paso

    Parámetros:
    Nada.

    Devolución:
    Nada.
    """

    graph_i = RomaniaFill()

    print("Ciudades:", graph_i.get_vertices())
    print()

    start_vertex, end_vertex = get_problem(graph_i)
    cost, path = uniform_cost_search(graph_i, start_vertex, end_vertex)
    if cost != float('inf'):
        print('De {start} a {end}'.format(start=start_vertex, end=end_vertex))
        print('Costo: {costo}'.format(costo=cost))
        print('Trayectoria: {trayectoria}'.format(trayectoria=path))
    else:
        print('No se puede alcanzar la ciudad elegida')

def try_out():
    """
    Descripción:
    Esta función usa el grafo de Rumania.
    Permite buscar entre dos ciudades o buscar entre todos los pares de ciudades,
    También permite buscar con la bandera FLAG_PRINT en True o en False

    Parámetros:
    Nada.

    Devolución:
    Nada.
    """

    global FLAG_PRINT   #Hace que sucesivas ediciones de FLAG_PRINT modifiquen la variable global y no una local

    print('Welcome to the temporal checking mode')
    print('What would you want to do?')
    print('1. Check standard functioning (main)')
    print('2. Check functioning')
    option_choosen = input()
    
    if option_choosen == '1':
        main()
    elif option_choosen == '2':
        print('Would you like to')

        print('1. Find the solution between two cities')
        print('2. Find the solution between all cities')
        op_two_or_all = input()
        if op_two_or_all != '1' and op_two_or_all != '2':
            print('No time to check for an invalid option choice, so bye bye')
            sys.exit()

        vbs = input('Do you want to use the verbose mode? Y/N: ')
        if vbs == 'Y':
            FLAG_PRINT = True
        else:
            FLAG_PRINT = False

        if op_two_or_all == '1':
            main()
        else:
            graph_i = RomaniaFill()
            check_combinations(graph_i)
    else:
        print('No valid option was choosen, au revoir')

# EJECUCION
try_out()
