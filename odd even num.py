import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

modified_numbers = [num * 2 for num in random_numbers if num % 2 == 0]

print(modified_numbers)