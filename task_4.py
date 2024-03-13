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
    
def visualize_heap(heap_root):
    """Функція для візуалізації бінарної купи."""
    heap = nx.DiGraph()
    pos = {}  # Створюємо порожній словник для позицій вузлів

    # Додаємо корінь бінарної купи
    heap.add_node(heap_root.id, color=heap_root.color, label=heap_root.val)
    pos[heap_root.id] = (0, 0)

    # Викликаємо рекурсивну функцію для додавання решти вузлів та ребер
    add_edges(heap, heap_root, pos)

    # Створюємо список кольорів та міток для вузлів
    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    # Візуалізуємо купу
    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи та візуалізація
def draw_heap():
	heap_root = Node(0)
	heap_root.left = Node(4)
	heap_root.left.left = Node(5)
	heap_root.left.right = Node(10)
	heap_root.right = Node(1)
	heap_root.right.left = Node(3)    
	visualize_heap(heap_root)
    
if __name__ == "__main__":
    draw_heap()
