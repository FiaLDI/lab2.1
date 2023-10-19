
## Вариант 17(7)

import math

if __name__ == "__main__":
    y = float(input("y = "))
    
    # Вычисление угла часовой стрелки
    angle_hour = y * 360 / (2 * math.pi)
    
    # Вычисление угла минутной стрелки
    angle_minute = angle_hour * 2
    
    # Определение количества полных часов
    full_hours = round(angle_hour / 30)
    
    # Определение количества полных минут
    full_minutes = round(angle_minute / 6)

    print(f"Угол для минутной стрелки: {angle_minute}")
    print(f"Количество полных часов: {full_hours}")
    print(f"Количество полных минут: {full_minutes}")
