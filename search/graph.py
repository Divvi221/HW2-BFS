import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if nx.has_path(G,start,end):
            visited = [start]
            Q = [(start,[start])] #keep track of starting node and the path
            while len(Q) != 0:
                v,path = Q.pop(0)
                if v==end:
                    return path
                else: 
                    N = list(self.neighbors(v))
                    for i in N:
                        if i not in visited:
                            visited.append(i)
                            Q.append((i,path+[i]))
            if end==None or end in visited:
                return list(visited)
            else: 
                return None
        else:
            return None
#        if end is None:
#            Q = []
#            visited = []
#            Q.append(start)
#            visited.append(start)
#            while len(Q) != 0:
#                v = Q.pop()
#                N = list(self.neighbors(v))
#                for i in N:
#                    if i not in visited:
#                        visited.append(i)
#                        Q.append(i)
#            return visited
#        else:
#            Q = []
#            visited = []
#            Q.append(start)
#            visited.append(start)
#            while len(Q) != 0:
#                v = Q.pop()
#                N = list(self.neighbors(v))
#                for i in N:
#                    if i not in visited and i!=end:
#                        visited.append(i)
#                        Q.append(i)
#                    else:
#                        break
#            return visited



#G = nx.read_adjlist('data/tiny_network.adjlist', delimiter=';')
#list1 = Graph.bfs(G,'Charles Chiu')
#print(len(list1))
#print(len(G.nodes()))
#if nx.has_path(G,'31486345','Nevan Krogan'):
#    print("path exists")
#    print(nx.shortest_path(G,'31486345','Nevan Krogan'))
#print(list(G.neighbors('31486345')))
#nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=200, font_size=7)
#plt.show()
