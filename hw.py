import cmath
import math
a = float(input("Введите длину превой стороны:"))
b = float(input("Введите длину второй стороны:"))
c = float(input("Введите Cos угла между ними:"))
print(cmath.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(c)))