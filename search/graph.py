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
        if nx.is_empty(self): #if graph is empty, return None
            raise ValueError(f"Graph is empty")
        elif start not in self.nodes(): #if starting node is not in the graph
            raise ValueError(f"Start node does not exist in this graph")
        elif end!=None and nx.has_path(self,start,end):
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
            if end in visited: #end==None or 
                return list(visited)
            #else: 
            #    return None
        elif end==None:
            if len(list(nx.connected_components(self))) == 1:
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
                return list(visited)
            elif len(list(nx.connected_components(self))) != 1:
                final_list = [] 
                for i in list(nx.connected_components(self)):
                    starting_node = list(i)[0] #pick any node (here i chose the first one of each component as the source node)
                    visited = [starting_node]
                    Q = [(starting_node,[starting_node])] #keep track of starting node and the path
                    while len(Q) != 0:
                        v,path = Q.pop(0)
                        if v==None:
                            return path
                        else: 
                            N = list(self.neighbors(v))
                            for i in N:
                                if i not in visited:
                                    visited.append(i)
                                    Q.append((i,path+[i]))
                    final_list.append(visited)
                return final_list
        elif end not in self.nodes(): #if ending node is not present in the graph
            if end != None:
                raise ValueError(f"End node does not exist in this graph")



            #return None
    def shortest_dist(self,start,end):
        shortest_path = nx.shortest_path(self,start,end)
        return shortest_path

G = nx.read_adjlist('data/test_network.adjlist', delimiter=';')
list1 = Graph.bfs(G,'31486345') #comment
#components = list(nx.connected_components(G))
#print(list1)
#print(len(G.nodes()))
#if nx.has_path(G,'31486345','Nevan Krogan'):
#    print("path exists")
#    print(nx.shortest_path(G,'31486345','Nevan Krogan'))
#print(list(G.neighbors('31486345')))
#nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=200, font_size=7)
#plt.show()
