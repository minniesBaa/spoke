import inflect
import json
p = inflect.engine()
e = lambda a: p.plural(a)
raw = []
with open("wordgen_assets/toplural.txt", "r") as f:
    raw = f.read()
data = raw.splitlines()
pluralized = []
c = 0
for i in data:
    c += 1
    t = e(i).lower()
    if len(t) == 5:
        pluralized.append(t)
        print(i)
with open("wordgen_assets/5letterwords.txt") as f:
    pluralized.extend(f.read().splitlines())
print("Serializing to JSON...")
with open("wordgen_assets/plural.json", "w") as f:
    f.write(json.dumps(pluralized))