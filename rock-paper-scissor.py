import random
import sys

def game():

    print("This is basic rock paper scissor game\n"
          "***RULES***\n"
          "For 'Rock': Just write '1'\n"
          "For 'Paper': Just write '2'\n"
          "For 'Scissor': Just write '3'\n")

    number = random.randint(1,3)
    numbers = [1,2,3]
    dict = {1: "Rock", 2: "Paper", 3: "Scissor"}


    player = int(input("Please give your answer(1/2/3): "))

    if player not in numbers:
        print("Please enter only 1, 2 or 3!")
        return

    print("Player's choice: ", dict[player])
    print("CPU's choice: ", dict[number])

    if  player == 1:
       if number == 1:
           print("Rock --- Rock ###DRAW###")
       elif number == 2:
           print("Rock --- Paper ###CPU WINS###")
       elif number == 3:
           print("Rock --- Scissor ###PLAYER WINS###")

    if  player == 2:
       if number == 1:
           print("Paper--- Rock ###PLAYER WINS###")
       elif number == 2:
           print("Paper --- Paper ###DRAW###")
       elif number == 3:
           print("Paper --- Scissor ###CPU WINS###")

    if  player == 3:
       if number == 1:
           print("Scissor --- Rock ###CPU WINS###")
       elif number == 2:
           print("Scissor --- Paper ###PLAYER WINS###")
       elif number == 3:
           print("Scissor --- Scissor ###DRAW###")

game()