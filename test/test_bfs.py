# write tests for bfs
from search import graph
import networkx as nx 
import pytest

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = graph.Graph('data/tiny_network.adjlist')
    path_list = graph.Graph.bfs(G,'Martin Kampmann')
    G_other = nx.read_adjlist("data/tiny_network.adjlist",create_using=nx.DiGraph, delimiter=";")
    networkx_bfs = [x[1] for x in nx.bfs_edges(G_other,source='Martin Kampmann')]
    networkx_bfs.insert(0,'Martin Kampmann') #my bfs method includes the starting node in the path but networkx bfs does not. Here I am just adding the starting node to the networkx bfs result to check if I performed bfs correctly
    assert networkx_bfs == path_list 
    assert len(path_list) != 0 #ensure that list is not empty
    assert len(set(graph.Graph.node_list(G))) == len(set(path_list)) #converted it to set to ensure no repeats. This test is to ensure that bfs is traversing through the whole graph

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    G = graph.Graph('data/citation_network.adjlist')
    path = graph.Graph.bfs(G,'31486345','Tony Capra')
    assert path != None 
    assert graph.Graph.shortest_dist(G,'31486345','Tony Capra') == path #ensure that bfs returns shortest path traversal
    G1 = graph.Graph('data/test_network.adjlist')
    path1 = graph.Graph.bfs(G1,'31806696','Marina Sirota') 
    assert path1 == None #test to ensure that bfs returns None for disconnected start and end nodes 
    try:
        path2 = graph.Graph.bfs(G,'3180','Marina Sirota') #starting node 3180 doesn't exist in the graph 
        assert False, "Expected an exception for a nonexistent node"
    except ValueError as e:
        assert str(e) == "Start node does not exist in this graph", f"Unexpected error message: {e}"
    path3 = graph.Graph.bfs(G1,'31486345')
    assert len(path3) == 2 #check that the traversal list has 2 lists within it since test_network.adjlist contains a disconnected graph.
