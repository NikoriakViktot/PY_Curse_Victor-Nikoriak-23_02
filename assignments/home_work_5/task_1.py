
#Task_1

import random

your_number = int(input("Вгадайте число від 1 до 10: "))
our_number = random.randint(1, 10)
if our_number == your_number:
    print(f'Наймовірно! Ви вгадали! число комп`ютера: {our_number}, Ваше число теж {your_number}')
else: print(f'Ви були дуже близько, але ні, число комп`ютера: {our_number}, Ваше число {your_number}')