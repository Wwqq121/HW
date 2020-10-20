f = open("D:/text.txt", 'w')
n = (input("Введите число: "))   
n = n.strip()
if not n.isdigit():
	print("Ввели неверно!")
	exit(1)
numbers = list(range(2, int(n) + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, int(n) + 1, number):
            numbers[candidate-2] = 0    
a = list(filter(lambda x: x != 0, numbers)) + '\n'
result = str(a)
f.write(result)
f.close()