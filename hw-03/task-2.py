import random

def get_numbers_ticket(min, max, quantity):
    list = []
    try:
        if min < 1 or max > 1000 : 
           return list
        result = random.sample(range(min, max), quantity)
        return result
    except ValueError:
        return list

print(get_numbers_ticket(1, 10, 11))

  