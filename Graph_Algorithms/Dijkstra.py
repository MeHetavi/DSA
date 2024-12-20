import heapq
import math
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph,start):
    priority_queue = []
    
    distance = {node: math.inf for node in graph}
    distance[start] = 0
    path = {node: None for node in graph}
    priority_queue = []
    
    heapq.heappush(priority_queue, (0, start))
    node = start

    while priority_queue != []:
        shortest_dist, node = heapq.heappop(priority_queue)
        for reachable in graph[node]:
            if (graph[node][reachable]+shortest_dist) < distance[reachable] :
                path[reachable] = node
                distance[reachable] = graph[node][reachable]+shortest_dist
                heapq.heappush(priority_queue, (distance[reachable], reachable))        
    print(distance,path)

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

graph = {
    0: {1: 4, 2: 4},
    1: {0: 4, 2: 2},
    2: {0: 4, 1: 2, 3: 3, 4: 1},
    3: {2: 3, 5: 2},
    4: {2: 1, 5: 3},
    5: {2: 6, 3: 2, 4: 3}
}
dijkstra(graph,start = list(graph.keys())[0])
# # Graph dictionary

G = nx.Graph()

for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

edge_labels = nx.get_edge_attributes(G, 'weight')

pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_weight='bold', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Weighted Graph")
plt.show()