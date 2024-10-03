a=list(map(int, input("Введите числа списка: ").split()))
print("Ваш список: ", a)
b=[i**2 for i in a]
print("Квадраты чисел вашего списка:", b)