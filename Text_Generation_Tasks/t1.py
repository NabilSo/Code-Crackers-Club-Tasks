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
    #if sp[-1] not in d:
        #d[sp[-1]] = []
    return d

def suggestion(dc,word):
    ans = ''
    i = 0
    if word in dc:
        while True and i < len(dc[word]) :
            ans = input("suggested word : " + dc[word][i] + " add it ? (y/n) ('.' to finish ): ")
            if ans == "y":
                return dc[word][i]
                break
            if ans == "n":
                i+=1
                continue
            if ans == ".":
                return "."
                exit
    return "."

def suggestionfuncv2(txt):
    print("write a word (dot to finish) : ")
    txt = markovchain(txt)
    inp = input()
    rslst = []
    i=0
    rslst.append(inp)
    a = ""
    while rslst[len(rslst)-1] != "." :
        a = suggestion(txt,rslst[i])
        if a:
            rslst.append(a)
        i += 1
    return rslst



f = "tst.txt"

print(markovchain(f))
#print(suggestionfuncv2(f))


#print(randtxt(content))
