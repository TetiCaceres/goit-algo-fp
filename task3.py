import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Бінарна купа (піраміда)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдено кращий шлях — пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перегляд сусідів
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Оновлення найкоротшого шляху
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ===== Створення графа =====
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

# Початкова вершина
start_vertex = 'A'

# Виконання алгоритму
shortest_paths = dijkstra(graph, start_vertex)

# Виведення результату
print("Найкоротші шляхи від вершини", start_vertex)
for vertex, distance in shortest_paths.items():
    print(f"До {vertex}: {distance}")
