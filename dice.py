import random
def digit(num):
    for i in num:
        return i
#   DICE
print(f"your number is: {random.choice(range(1,7))}")


#   high probability of 6
dice = (1, 2, 3, 4, 5, 6)
ans = random.choices(dice, weights=(1, 1, 1, 1, 1, 6), k=1)
print("ans:",digit(ans))

#   high probability of 1
dice = (1, 2, 3, 4, 5, 6)
ans = random.choices(dice, weights=(6, 1, 1, 1, 1, 1), k=1)
print("ans:",digit(ans))

#   high probability of 6
dice = (1, 2, 3, 4, 5, 6)
ans = random.choices(dice, weights=(1, 1, 2, 4, 3, 1), k=1)
print("ans:",digit(ans))

#   random.choices returns a list. Digit function is used to convert that list into number