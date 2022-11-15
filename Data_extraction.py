import json
import random

i, j, k = 0, 0, 0

while i < 100 or j < 100 or k < 100:
    file = random.randint(0, 348)

    with open("splitdata/" + str(file) + ".json", encoding="utf-8") as f:
        data = json.load(f)

    e = random.randint(0, 19999)
    stars = str(int(data[e]["stars"]))
    
    if stars == "1" and i < 100:
        name = stars + "_" + "review" + str(i) + ".txt"
        f = open(name, "x", encoding="utf-8")
        f.write(data[e]["text"])
        f.close()
        i += 1
    
    if stars == "3" and j < 100:
        name = stars + "_" + "review" + str(j) + ".txt"
        f = open(name, "x", encoding="utf-8")
        f.write(data[e]["text"])
        f.close()
        j += 1
        
    if stars == "5" and k < 100:
        name = stars + "_" + "review" + str(k) + ".txt"
        f = open(name, "x", encoding="utf-8")
        f.write(data[e]["text"])
        f.close()
        k += 1