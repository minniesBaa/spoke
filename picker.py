import random
import json
words = ""
with open("wordgen_assets/5letterwords.txt", "r") as file:
    words = file.read()
data = words.splitlines()
getword = lambda: random.choice(data)
wl = [getword()]
middlechar = wl[0][2]
itr = 0
for i in range(3):
    word = "     "
    while (word[2] != middlechar) or ("q" if i == 0 else "valuethatwonteverbeinaword") in word:
        word = getword()
        itr += 1
        if itr > 20000:
            exit()
    wl.append(word)

out = json.dumps(wl)
with open("puzzle.txt", "w") as file:
    file.write(out)