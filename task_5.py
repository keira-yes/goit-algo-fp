import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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

# Функція для візуалізації бінарної купи
def visualize_heap(heap_root, title):
    heap = nx.DiGraph()
    pos = {}
    heap.add_node(heap_root.id, color=heap_root.color, label=heap_root.val)
    pos[heap_root.id] = (0, 0)
    add_edges(heap, heap_root, pos)
    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для генерації кольорів від темних до світлих
def generate_color(step, total_steps):
    min_intensity = 60  # Мінімальне значення для інтенсивності, щоб уникнути білого кольору
    intensity = min_intensity + int((step / total_steps) * (255 - min_intensity))
    return f"#{intensity:02x}{intensity:02x}{255:02x}"

# Функції обходу дерева, які змінюють кольори вузлів
def dfs(node, colors, visited, step=0):
    if node and node.id not in visited:
        node.color = colors[step]
        visited.add(node.id)
        step += 1
        if node.left:
            step = dfs(node.left, colors, visited, step)
        if node.right:
            step = dfs(node.right, colors, visited, step)
    return step

def bfs(root, colors):
    queue = deque([(root, 0)])
    visited = set()
    while queue:
        node, step = queue.popleft()
        if node and node.id not in visited:
            node.color = colors[step]
            visited.add(node.id)
            queue.append((node.left, step + 1))
            queue.append((node.right, step + 1))

# Створення та візуалізація дерева з оновленими кольорами
def draw_heap():
    heap_root = Node(0)
    heap_root.left = Node(4)
    heap_root.left.left = Node(5)
    heap_root.left.right = Node(10)
    heap_root.right = Node(1)
    heap_root.right.left = Node(3)

    total_nodes = 6
    colors = [generate_color(i, total_nodes) for i in range(total_nodes)]
    visited = set()

    # Оновлення кольорів для DFS
    dfs(heap_root, colors, visited)
    visualize_heap(heap_root, 'DFS')

    # Оновлення кольорів для BFS
    bfs(heap_root, colors)
    visualize_heap(heap_root, 'BFS')

if __name__ == "__main__":
    draw_heap()
