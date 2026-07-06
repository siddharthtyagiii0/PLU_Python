'''
Create an undirected graph with the following edges:
* A – B
* A – C
* B – D
* C – D
Display the adjacency list of the graph.
'''
graph = {}

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "D"]
graph["D"] = ["B", "C"]

print("Adjacency List:")
for vertex in graph:
    print(vertex, ":", graph[vertex])