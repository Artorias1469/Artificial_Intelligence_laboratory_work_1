#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решение задачи коммивояжёра методом полного перебора.
Для начального города на построенном графе.
"""

from itertools import permutations

# Матрица расстояний между городами
distance_dict = {
    "Париж": {"Париж": 0, "Франкфурт-на-Майне": 572, "Лиль": 219, "Дортмунд": float("inf"), "Дрезден": float("inf"),
              "Лейпциг": float("inf"), "Берлин": float("inf"), "Магдебург": float("inf"), "Ганновер": float("inf"),
              "Амстердам": float("inf"), "Бремен": float("inf")},
    "Франкфурт-на-Майне": {"Париж": 572, "Франкфурт-на-Майне": 0, "Лиль": float("inf"), "Дортмунд": 219,
                           "Дрезден": 460, "Лейпциг": float("inf"), "Берлин": float("inf"),
                           "Магдебург": float("inf"), "Ганновер": float("inf"), "Амстердам": float("inf"),
                           "Бремен": float("inf")},
    "Лиль": {"Париж": 219, "Франкфурт-на-Майне": float("inf"), "Лиль": 0, "Дортмунд": 365, "Дрезден": float("inf"),
             "Лейпциг": float("inf"), "Берлин": float("inf"), "Магдебург": float("inf"),
             "Ганновер": float("inf"), "Амстердам": 287, "Бремен": float("inf")},
    "Дортмунд": {"Париж": float("inf"), "Франкфурт-на-Майне": 219, "Лиль": 365, "Дортмунд": 0,
                 "Дрезден": float("inf"), "Лейпциг": float("inf"), "Берлин": float("inf"), "Магдебург": 354,
                 "Ганновер": 214, "Амстердам": float("inf"), "Бремен": float("inf")},
    "Дрезден": {"Париж": float("inf"), "Франкфурт-на-Майне": 460, "Лиль": float("inf"), "Дортмунд": float("inf"),
                "Дрезден": 0, "Лейпциг": 112, "Берлин": float("inf"), "Магдебург": float("inf"),
                "Ганновер": float("inf"), "Амстердам": float("inf"), "Бремен": float("inf")},
    "Лейпциг": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": float("inf"),
                "Дортмунд": float("inf"), "Дрезден": 112, "Лейпциг": 0, "Берлин": 188, "Магдебург": float("inf"),
                "Ганновер": float("inf"), "Амстердам": float("inf"), "Бремен": float("inf")},
    "Берлин": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": float("inf"),
               "Дортмунд": float("inf"), "Дрезден": float("inf"), "Лейпциг": 188, "Берлин": 0,
               "Магдебург": 153, "Ганновер": float("inf"), "Амстердам": float("inf"), "Бремен": float("inf")},
    "Магдебург": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": float("inf"),
                  "Дортмунд": 354, "Дрезден": float("inf"), "Лейпциг": float("inf"), "Берлин": 153,
                  "Магдебург": 0, "Ганновер": 146, "Амстердам": float("inf"), "Бремен": float("inf")},
    "Ганновер": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": float("inf"),
                 "Дортмунд": 214, "Дрезден": float("inf"), "Лейпциг": float("inf"), "Берлин": float("inf"),
                 "Магдебург": 146, "Ганновер": 0, "Амстердам": float("inf"), "Бремен": 124},
    "Амстердам": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": 287, "Дортмунд": float("inf"),
                  "Дрезден": float("inf"), "Лейпциг": float("inf"), "Берлин": float("inf"),
                  "Магдебург": float("inf"), "Ганновер": float("inf"), "Амстердам": 0, "Бремен": 354},
    "Бремен": {"Париж": float("inf"), "Франкфурт-на-Майне": float("inf"), "Лиль": float("inf"),
               "Дортмунд": float("inf"), "Дрезден": float("inf"), "Лейпциг": float("inf"), "Берлин": float("inf"),
               "Магдебург": float("inf"), "Ганновер": 124, "Амстердам": 354, "Бремен": 0},
}

# Задаем начальный город
start_city = "Париж"


def solve_tsp(distance_dict, start_city):
    cities = list(distance_dict.keys())
    n = len(cities)
    start_index = cities.index(start_city)

    # Генерация всех возможных маршрутов (перестановок) кроме начального города
    min_route_length = float("inf")
    best_route = []

    # Генерируем все перестановки всех городов, исключая начальный
    for perm in permutations([i for i in range(n) if i != start_index]):
        route = [start_index] + list(perm) + [start_index]
        route_length = sum(distance_dict[cities[route[i]]][cities[route[i + 1]]] for i in range(n))

        # Обновляем лучший маршрут, если найден маршрут с меньшей длиной
        if route_length < min_route_length:
            min_route_length = route_length
            best_route = [cities[i] for i in route]

    return best_route, min_route_length


if __name__ == "__main__":
    # Выводим лучший маршрут и его длину
    best_route, min_length = solve_tsp(distance_dict, start_city)
    print(f"Лучший маршрут: {' -> '.join(best_route)} с длиной {min_length} км")
