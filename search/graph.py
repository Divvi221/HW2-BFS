import networkx as nx

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
        if nx.is_empty(self.graph)==True: #if graph is empty, return None
            raise ValueError(f"graph is empty")
        
        elif start not in self.graph.nodes(): #if starting node is not in the graph
            raise ValueError(f"Start node does not exist in this graph")
        
        elif end!=None and nx.has_path(self.graph,start,end): #if there is a path between start and end node, perform bfs to get the shortest path
            visited = [start]
            Q = [(start,[start])] #keep track of starting node and the path
            while len(Q) != 0:
                v,path = Q.pop(0)
                if v==end:
                    return path
                else: 
                    N = list(self.graph.neighbors(v))
                    for i in N:
                        if i not in visited:
                            visited.append(i)
                            Q.append((i,path+[i]))
            if end in visited: #end==None or 
                return list(visited)

        elif end==None: #if end is none, traverse through the whole graph

            if nx.is_weakly_connected(self.graph): #if it is a connected graph
                visited = [start]
                Q = [(start,[start])] #keep track of starting node and the path
                while len(Q) != 0:
                    v,path = Q.pop(0)
                    if v==end:
                        return path
                    else: 
                        N = list(self.graph.neighbors(v))
                        for i in N:
                            if i not in visited:
                                visited.append(i)
                                Q.append((i,path+[i]))
                return list(visited)
            
            elif nx.is_weakly_connected(self.graph)==False: #if it is an unconnected graph
                final_list = [] 
                for i in list(nx.weakly_connected_components(self.graph)):
                    starting_node = list(i)[0] #pick first one of each component as the source node
                    visited = [starting_node]
                    Q = [(starting_node,[starting_node])] #keep track of starting node and the path
                    while len(Q) != 0:
                        v,path = Q.pop(0)
                        if v==None:
                            return path
                        else: 
                            N = list(self.graph.neighbors(v))
                            for i in N:
                                if i not in visited:
                                    visited.append(i)
                                    Q.append((i,path+[i]))
                    final_list.append(visited)
                return final_list
            
        elif end not in self.graph.nodes(): #if ending node is not present in the graph
            if end != None:
                raise ValueError(f"End node does not exist in this graph")

    def shortest_dist(self,start,end): #calculate shortest distance using nx (used for testing)
        shortest_path = nx.shortest_path(self.graph,start,end)
        return shortest_path
    
    def node_list(self): #return a list of nodes using nx (used for testing)
        list_node = self.graph.nodes()
        return list_node
