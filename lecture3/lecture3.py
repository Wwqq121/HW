a = input("Графусы Цельсия(С) или Фаренгейта(F): ")
a = a.strip()
chose = "CF"
if a[0] not in chose:
	print("Ввели неверно!")
	exit(1)
if not len(a) == 1:
	print("Ввели неверно!")
	exit(2)
n = input("Введите температуру: ")
if not n.isdigit():
	print("Введите число!")
	exit(3)
number = float(n)
if a in "C":
	r = number * 1.8 + 32
	print("Результат: " + str(r) + " F")
if a in "F":
	result = (number - 32) / 1.8
	print("Результат " + str(result) + " C")