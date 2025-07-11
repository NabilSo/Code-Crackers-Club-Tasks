from re import split


def split_words(text):
    with open(text,"r") as f:
        c = f.read()
    return c.split()

def markovchain2(mkvlst):
    sp = split_words(mkvlst)
    d = {}
    for i in range(len(sp)-2):
        a = (sp[i]+" "+sp[i+1])
        if a not in d :
            d[a] = []
        d[a].append(sp[i+2])
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
    txt = markovchain2(txt)
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
    return  ' '.join(rslst)


f = "sample_text.txt"

print(suggestionfuncv2(f))
