import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import traversal
import random 

from graph_algorithms import dfs_edges, bfs_edges, all_pairs_dijkstra

## Завдання 1

# Створення графа
G = nx.Graph()

# Додавання станцій (вершин)
stations = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5"]
G.add_nodes_from(stations)

# Додавання з'єднань (ребер)
connections = [("Станція 1", "Станція 2"), ("Станція 2", "Станція 3"), ("Станція 3", "Станція 4"),
               ("Станція 4", "Станція 5"), ("Станція 5", "Станція 1"), ("Станція 1", "Станція 3")]
G.add_edges_from(connections)

# Візуалізація графа
plt.figure(figsize=(8, 8))
nx.draw_circular(G, with_labels=True, node_color='lightblue', edge_color='gray', font_size=15, node_size=2000)
plt.title("Транспортна мережа міста")
# plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:", list(G.degree()))


## Завдання 2

# DFS шлях власна реалізація
dfs_path = list(dfs_edges(G, "Станція 1"))

print("DFS шлях власна реалізація:", dfs_path)

# DFS шлях
dfs_path = list(traversal.dfs_edges(G, source="Станція 1"))
print("DFS шлях", dfs_path)

# BFS шлях власна реалізація
bfs_path = list(bfs_edges(G, "Станція 1"))
print("BFS шлях власна реалізація:", bfs_path)

# BFS шлях
bfs_path = list(traversal.bfs_edges(G, source="Станція 1"))
print("BFS шлях:", bfs_path)



## Завдання 3

# Додавання ваг до ребер
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)


# Обчислюємо найкоротші шляхи між усіма парами вершин
shortest_paths_all_pairs = all_pairs_dijkstra(G)

# Друк результатів
for start, paths in shortest_paths_all_pairs.items():
    print(f"\nНайкоротші шляхи від {start}:")
    for destination, length in paths.items():
        print(f"{start} -> {destination}: {length}")
