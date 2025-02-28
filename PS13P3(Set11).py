f = open("Code/PS13P3(11).txt", "r")
lastn = []
score = []
lastname = f.readline()

while lastname != "":
    lastn.append(lastname.rstrip("\n")) 
    scores = float(f.readline())  
    score.append(scores)  
    lastname = f.readline()

f.close()

l = len(lastn)

def low(lastn, score):
    low_var = 999  
    lowindex = 0
    for y in range(l):
        if score[y] < low_var:
            lowindex = y
            low_var = score[y]
    print(f"{lastn[lowindex]} has the lowest score of {score[lowindex]}.")

def high(lastn, score):
    high_var = -1  
    highindex = 0
    for x in range(l):
        if score[x] > high_var:
            highindex = x
            high_var = score[x]
    print(f"{lastn[highindex]} has the highest score of {score[highindex]}.")

print(lastn, score)
high(lastn, score)
low(lastn, score)
