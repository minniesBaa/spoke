import random
words = ""
with open("words.txt", "r") as file:
    words = file.read()
data = words.splitlines()
getword = lambda: random.choice(data)
wl = [getword()]
middlechar = wl[0][2]
for i in range(3):
    word = "     "
    while word[2] != middlechar:
        word = getword()
    wl.append(word)
with open("puzzle.txt") as file:
    file.write(str(wl))