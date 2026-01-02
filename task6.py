def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            total_cost += data["cost"]
            total_calories += data["calories"]
            selected_items.append(name)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    # Таблиця DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - cost] + calories
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних страв
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= items[names[i - 1]]["cost"]

    selected_items.reverse()
    return selected_items, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Жадібний алгоритм:")
    print("Страви:", greedy_result[0])
    print("Калорійність:", greedy_result[1])

    print("\nДинамічне програмування:")
    print("Страви:", dp_result[0])
    print("Калорійність:", dp_result[1])
