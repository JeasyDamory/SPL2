# Grundlagen-python.py

# Kommentare erfolgen mit hashtags

# Ausgabe von Daten
print("Hello World")

# Variablen definieren (kann ohne Typ erfolgen)
heimat = "Earth"

print(heimat, "to World: ", "Hello!")

# Eingabe
wer = input("And who are you? ")

# und gibt den Text wieder aus
if (wer == "ich"):
    print("Hey", "you")
else:
    print("Hey", wer, "!")

favouriteNum = input("What is your favourite number? ")
print("Nice! I like the number", favouriteNum, "as well.")
print("But I still like the bigger number,", int(favouriteNum)+10, ", a lot more!")