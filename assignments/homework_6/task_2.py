#Task_2

import random

number_list_1 = []
number_list_2 = []

while len(number_list_1) < 10:
    number_list_1.append(random.randint(1, 10))
    number_list_2.append(random.randint(1, 10))
print(number_list_1)
print(number_list_2)
number_set = set(number_list_1) & set(number_list_2)
number_list_3 = list(number_set)
print(number_list_3)



