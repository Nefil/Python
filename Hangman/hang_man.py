import random
lives = 6
words = ["choinka", "miasto", "impreza"]

choicen_word = random.choice(words)
print(choicen_word)

placeholder = ""
length = len(choicen_word)
for i in range(length):
    placeholder += "_"
print(placeholder)

placeholder2 = "_"
odgadniete = []

while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    print(f"You have {lives -1} lives left.")

    display = ""

    for letter in choicen_word:
        if letter in odgadniete:
            print("Podawałeś juz tą literę")
            print(f"Lista podanych liter: {odgadniete}")
        elif letter == guess:
            display += letter
            placeholder2 += letter
        elif letter in placeholder2:
            display += letter
        else:
            display += "_"
    odgadniete.append(guess)
    print(display)
    if guess not in choicen_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
            exit(0)