import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(n):
    """Генерує n кольорів від темного до світлого синього."""
    colors = []
    for i in range(n):
        # Розрахунок яскравості: від 30 (темний) до 240 (світлий)
        lightness = int(30 + (i * (210 / (n - 1 if n > 1 else 1))))
        # Перетворення в HEX формат (відтінки синього/блакитного)
        hex_color = f'#{lightness:02x}96F0'
        colors.append(hex_color)
    return colors

def bfs_visualize(root):
    """Обхід в ширину (BFS) з використанням черги."""
    if not root: return
    
    queue = deque([root])
    visited_nodes = []
    
    while queue:
        node = queue.popleft()
        visited_nodes.append(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        
    colors = generate_colors(len(visited_nodes))
    for i, node in enumerate(visited_nodes):
        node.color = colors[i]
    
    draw_tree(root, title="BFS Traversal (Breadth-First Search)")

def dfs_visualize(root):
    """Обхід в глибину (DFS) з використанням стека."""
    if not root: return
    
    stack = [root]
    visited_nodes = []
    
    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        # Додаємо спочатку правий, потім лівий, щоб лівий обробився першим (LIFO)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        
    colors = generate_colors(len(visited_nodes))
    for i, node in enumerate(visited_nodes):
        node.color = colors[i]
    
    draw_tree(root, title="DFS Traversal (Depth-First Search)")

# Побудова дерева як у завданні 4
def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

# Виконання візуалізації
if __name__ == "__main__":
    # Для кожного обходу створюємо дерево заново, щоб скинути кольори
    bfs_root = build_sample_tree()
    bfs_visualize(bfs_root)
    
    dfs_root = build_sample_tree()
    dfs_visualize(dfs_root)