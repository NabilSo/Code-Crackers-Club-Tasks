import random

def split_words(text):
    with open(text,"r") as f:
        c = f.read()
    return c.split()

def freq(file):
    num={}
    for i in split_words(file):
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return num

def randtxt(text):
    words = split_words(text)
    r = []
    for _ in range(random.randint(1, len(words))):
        x = random.randint(0, len(words) - 1)
        r.append(words[x])
    return ' '.join(r)

def markovchain(mkvlst):
    sp = split_words(mkvlst)
    d = {}
    for i in range(len(sp)-1):
        if sp[i] not in d :
            d[sp[i]] = []
        d[sp[i]].append(sp[i+1])
    if sp[-1] not in d:
        d[sp[-1]] = []
    return d


f = "sample_text.txt"

print(markovchain(f))

#print(randtxt(content))
