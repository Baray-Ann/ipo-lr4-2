a=list(map(int, input("Введите числа списка: ").split())) #Ввод списка с клавиатуры, с функцией map() преобразовывающей элементы списка в тип данных int, и функцией .split() разделяющей вводимые элементы
print("Ваш список: ", a) #Вывод списка на консоль
b=[i**2 for i in a] #Генератор списка, с помощью которого мы возводим элементы списка в квадрат
print("Квадраты чисел вашего списка:", b) #Вывод на консоль преобразованного списка
