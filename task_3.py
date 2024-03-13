import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_with_heap(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = [(0, start)]  # Бінарна купа для оптимізації вибору вершин

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(unvisited)

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return distances

def visualize_graph(graph):
    G = nx.DiGraph()

    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(vertex, neighbor, weight=weight)

    # Візуалізація графа
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=20, font_weight="bold", arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Weighted Graph")
    plt.show()

def main():
    # Створення графа
    graph = {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 8: 2},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    }

    # Візуалізація графа
    visualize_graph(graph)

    # Використання алгоритму Дейкстри та обчислення найкоротших шляхів
    start_vertex = 0
    shortest_paths = dijkstra_with_heap(graph, start_vertex)

    # Виведення результатів
    print(f"Найкоротші шляхи з вершини {start_vertex}:", shortest_paths)

if __name__ == "__main__":
    main()
