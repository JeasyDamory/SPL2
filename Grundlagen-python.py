# Grundlagen-python.py

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
    print("Round", i, "of", round, ": Winner:", who)