import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def insert_node(root, key):
    if root is None:
        return Node(key)
    else:
        if root.left is None:
            root.left = insert_node(root.left, key)
        elif root.right is None:
            root.right = insert_node(root.right, key)
        else:
            # This simplistic insertion maintains the tree shape but does not ensure heap properties
            if height(root.left) <= height(root.right):
                root.left = insert_node(root.left, key)
            else:
                root.right = insert_node(root.right, key)
        return root

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def build_heap(elements):
    if not elements:
        return None
    root = Node(elements[0])
    for element in elements[1:]:
        insert_node(root, element)
    return root

# Візуалізація бінарної купи
elements = [10, 15, 30, 40, 50, 100, 40]
heap_root = build_heap(elements)
draw_tree(heap_root)
