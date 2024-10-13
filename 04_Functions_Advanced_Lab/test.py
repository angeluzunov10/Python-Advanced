# Функциите носят функционалност на код, който ако трябва да се промени, то той ще се промени само на едно място.
#
# Функцията се пише един път, но може да бъде извиквана на различни места, с различни аргументи.
#
# дефиницията на функцията се прави с def
#
# когато извикваме функцията, пишем името и и накрая в (поставяме изисканите от нея аргументи)
#
#
# 			PACKING ARGUMENTS
# *args **kwargs
#
# това се нарича пакетиране
#
# ------ *args - искам неограничен брой аргументи - работи с 0, 1 или много аргументи(args може да бъде заменено с някакво друго име, значението идва от звездичките, но над 90% се използва args)
#
# def sum_nums(*args):
# 	total_sum = 0
# 	for el in args:
# 		total_sum += el
# 	return total_sum
# това ще сумира колкото и елемента да са подадени
#
# можем да кажем, че функцията има задължително 2 елемента и от там нататък върви през аргументите, ако има такива
#
# def sum_nums(a, b, *args):
# 	total_sum = a + b
# 	for el in args:
# 		total_sum += el
# 	return total_sum
#
# ------ *kwargs - позволява ни да подаваме наименувани вече променливи, като отново не се ограничаваме от техния брой - работи с 0, 1 или много аргументи(key-loaded)
#
# това се свежда до dictionary, key-value двойки
#
#
# def greet_me(**kwargs):
# 	for key, value in kwargs.items():
# 		print(f"{value}, {key}")
#
#
# greet_me(Petter="Hello", George="Bye")
#
# това ще отпечата:
# =>Hello, Peter
#   Bye, George
#
#
# 			UNPACKING ARGUMENTS
#
# Пак можем да използваме */**, но при извикването на самата функция, като това вече ще има съвсем различно действие(разпакетиране)
#
# def print_nums(a, b, c):
# 	print(a, b, c)
#
# nums = [1, 2, 3]
# a, b, c = nums
# print_nums = (*nums)
#
# ВАЖНО!!!
# Когато разпакетираме при ** трябва да се съобразим, че ключовете и стойностите в речника трябва да съвпадат с имената на параметрите на функцията при нейното извикване! В случая обаче, не е задължително да ги извикваме под ред, тъй като те са си вързани и няма как при ключ key1 да се извика стойността value2
#
# пример:
# def some_func(name, age):
# 	print(f"{name} is {age} years old")
# person = {'age': 20, 'name': 'Peter'}
# some_func(**person)
#
# => Peter is 20 years old
#
# ВАЖНО!!!
#
# При дефиниция на функцията имаме ПАРАМЕТРИ
# При извикване на функцията имаме АРГУМЕНТИ
#
#
# 			СОРТИРАНЕ
#
# sorted() - сортира параметрите на даден iterable обект. При сортиране на речник обаче можем да сортираме по ключ или по стойност
#
# people = {"Peter": 21, "George": 18, "John": 45}
#
# print(sorted(people)) => ["George", "John", "Peter"] - извади ми само ключовете, сортирани по азбучен ред
#
# print(sorted(people.items(), key= lambda kvp: kvp[0])) => [("George", 18), ("John", 45), ("Peter", 21)] - сортирай ми ги по азбучен ред по ключ (ключа е : kvp[0])
#
# print(sorted(people.items(), key= lambda kvp: kvp[1])) => [("George", 18), ("Peter", 21), ("John", 45)] - сортирай ми ги по азбучен ред по стойност (стойността е : kvp[1])
#
# ако желая да се сортира обратно на азбучния ред се добавя трети параметър в sorted(), наречен reverse= True/False
#
# print(sorted(people.items(), key= lambda kvp: kvp[0], reverse=True)) => [("John", 45), ("Peter", 21), ("George", 18)] - сортирай ми ги обратно на азбучния ред по ключ (ключа е : kvp[0]). Това важи и за обратно сортиране по стойност (kvp[1])
#
#
#
# ВАЖНО!!!
#
# Когато пиша return, то това директно излизаше от функцията, без да минава през останалото парче код в нея и без да итерира още един път през цикъла в нея.
# Ако искам да ми се изпълнят всички неща пиша print() вътре в нея и при извикването и долу вече тези неща ще си се изпълнят.
#
# 			NESTED FUNCTIONS
#
# Inner Functions and Closures
#
# Функциите могат да бъдат и вложени (Nested Functions)
#
# Вложената функция не съществува извън функцията, в която е дефинирана, т.е. ако извикаме вътрешна функция извън функцията, в която тя е дефинирана, то тя няма да просъществува
#
# Можем да достъпим на кое място в паметта е запазена дадена функция, като когато я извикаме не пишем скобите зад нея
#
# def a():
# 	def b ():
# 		returh "Hello"
# 	return b
#
# result = a() # това ни връща return-a на ф-ята
# print(result)
#
# => <function a.<locals>.b at 0x1025a74c0> ------> това е референция към функцията
#
# за да принтирам "Hello" в случая трябва просто да допиша в print(result())
#
# Lexical Closures
#
# Вътрешната функция има знание какво се намира във външната функция
#
#
#
