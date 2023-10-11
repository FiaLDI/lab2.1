
## Вариант 17(7)

from cmath import pi


if __name__ == "__main__":
    y = int(input())
    tanmin = (y * 60) / 2 * pi
    fulltime = tanmin // (pi / 6)
    fullmin = (tanmin % (pi/6)) * 2
    print(f"Угол минутной стрелки - {tanmin}")
    print(f"Полные часы - {fulltime}")
    print(f"Полные минуты - {fullmin}")
