import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def dfs(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root)
        dfs(root.left, result)
        dfs(root.right, result)
    return result

def bfs(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return result

def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color_value = 255 - int(255 * (i / num_colors))
        hex_color = "#{:02x}{:02x}{:02x}".format(color_value, color_value, color_value)
        colors.append(hex_color)
    return colors

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Генерація кольорів
    num_nodes = len(traversal)
    colors = generate_colors(num_nodes)

    # Присвоєння кольорів вузлам
    for idx, node in enumerate(traversal):
        node.color = colors[idx]

    # Відновлення кольорів для візуалізації
    colors = [node.color for node in traversal]
    labels = {node.id: node.val for node in traversal}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Виконання обходів
dfs_traversal = dfs(root)
bfs_traversal = bfs(root)

# Відображення дерева з використанням обходу в глибину (DFS)
print("Обхід в глибину (DFS):")
draw_tree(root, dfs_traversal)

# Відображення дерева з використанням обходу в ширину (BFS)
print("Обхід в ширину (BFS):")
draw_tree(root, bfs_traversal)
