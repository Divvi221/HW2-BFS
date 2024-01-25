# write tests for bfs
from search import graph
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
    path_list = graph.Graph.bfs(G,'Atul Butte')
    assert len(path_list) != 0
    assert len(set(G.nodes())) == len(set(path_list)) #converted it to set to ensure no repeats

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
    print(path)
    assert path != None
    assert graph.Graph.shortest_dist(G,'31486345','Tony Capra') == path
    G1 = graph.Graph('data/test_network.adjlist')
    path1 = graph.Graph.bfs(G1,'31806696','Marina Sirota') 
    assert path1 == None
    try:
        path2 = graph.Graph.bfs(G,'3180','Marina Sirota') #starting node doesn't exist in the graph 
        assert False, "Expected an exception for a nonexistent node"
    except ValueError as e:
        assert str(e) == "Start node does not exist in this graph", f"Unexpected error message: {e}"
