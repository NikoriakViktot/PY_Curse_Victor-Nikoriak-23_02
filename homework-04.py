#Task1
var1 = input("Please enter a word:") #рпросим ввести желаемое слово
if len(var1) < 1: #проверяем на длинну строки
    print("please another word") #просим ввести другое слово так как слишком короткое
elif len(var1) > 2: #снава выполняем проверку на длинну строки
    print(var1[:2] + var1[-2:]) #выполняем задание для первых двух символов и последних

#Task2
number_phone = input("Please enter a number:") #просим ввести номер телефона
if len(number_phone) < 10: #проверяем количество сиволов номера телефона
    print("please another number") #номер не подходит по формату
number_phone.isdigit()

