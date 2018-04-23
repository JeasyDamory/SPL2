# Grundlagen-python.py
import random
# Kommentare erfolgen mit hashtags

# Ausgabe von Daten
print("Hello World")

# Variablen definieren (kann ohne Typ erfolgen)
home = "Earth"

print(home, "to World: ", "Hello!")

# Eingabe
who = input("And who are you? ")

# und gibt den Text wieder aus
if (who == "me"):
    print("Hey you!")
else:
    print("Hey", who, "!")

favouriteNum = input("What is your favourite number? ")
print("Nice! I like the number", favouriteNum, "as well.")
print("But I still like the bigger number,", int(favouriteNum)+10, ", a lot more!")

round = input("How many rounds should we play? ")
round = int(round)


for i in range(1, round+1):

    winner = " "
    whoWins = 0
    computerWins = 0

# generate random number
    randomNum = random.randint(1,6)

# if random number is 1,3 or 5: I win
# otherwise: computer wins

    if (randomNum == 1 or randomNum == 3 or randomNum == 5):
        winner = who
        whoWins += 1
    else: 
        winner = "computer"
        computerWins += 1


    print("Round", i, "of", round, ": Winner =", winner, " - diced was: ", randomNum)

if (whoWins > computerWins):
    print("You win!")
elif (whoWins == computerWins):
    print("Tie!")
elif (computerWins > whoWins):
    print("Computer wins!")

print("Game Over")