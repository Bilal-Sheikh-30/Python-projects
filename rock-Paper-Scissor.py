  # without user interaction

# import random
# option1 = ("rock", "paper", "scissors")
# pl1 = random.choice(option1)
# print("player 1:",pl1)
# pl2 = random.choice(option1)
# print("player 2:",pl2)
# if (pl1 == "rock" and pl2 == "scissors") or (pl1 == "scissors" and pl2 == "paper") or (pl1 == "paper" and pl2 == "rock"):
#     print("*** player 1 won ***")
# elif pl1 == pl2:
#     print("** game draw **")
# else:
#     print("*** player 2 won ***")


#       with user interaction

print("""
    r--->   Rock
    p--->   Paper
    s--->   Scissor""")
pl1 = input("\nplayer 1 ---> ").lower()
pl2 = input("player 2 ---> ").lower()
if (pl1 == "r" and pl2 == "s") or (pl1 == "s" and pl2 == "p") or (pl1 == "p" and pl2 == "r"):
    print("player 1 won")
elif pl1 == pl2:
    print("game draw")
else:
    print("player 2 won")