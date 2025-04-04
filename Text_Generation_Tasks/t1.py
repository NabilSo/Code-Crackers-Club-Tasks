import random

def splitt(file):
	lst=[]
	w=file.read()
	for i in w.split():
		lst.append(i) 
	return lst

def freq(file):
	num={}
	for i in splitt(file):
		if i in num:
			num[i] += 1
		else:
			num[i] = 1
	return num

def randtxt(file):
	w = splitt(file)
	r = []
	for i in range(random.randint(0,len(w))):
		x = random.randint(0,len(w))
		r.append(w(x)) 
	return w

f = open("sample_text.txt")

print(randtxt(f))