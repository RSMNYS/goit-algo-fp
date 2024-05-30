from collections import deque

def dfs_edges(graph, start_vertex):
    visited = set([start_vertex])
    stack = [(start_vertex, iter(graph[start_vertex]))]
    edges = []

    while stack:
        parent, children = stack[-1]
        try:
            child = next(children)
            if child not in visited:
                visited.add(child)
                edges.append((parent, child))
                stack.append((child, iter(graph[child])))
        except StopIteration:
            stack.pop()

    return edges


def bfs_edges(graph, start):
    visited = set([start]) 
    queue = deque([start]) 
    edges = []  

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                edges.append((vertex, neighbor)) 

    return edges

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def all_pairs_dijkstra(graph):
    all_pairs_shortest_paths = {}
    for node in graph.nodes:
        all_pairs_shortest_paths[node] = dijkstra(graph, node)
    return all_pairs_shortest_paths


