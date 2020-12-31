import random
lalpha=[]
ualpha=[]
digits=[]
spchar=[]
p=[]
for i in range(65,91):
  lalpha.append(chr(i))
for i in range(97,122):
  ualpha.append(chr(i))
for i in range(49,58):
  digits.append(chr(i))
for i in range(33,48):
  spchar.append(chr(i))
a=int(input("enter length of password"))
b=int(input("how many letters"))
c=int(input("how many digits"))
d=a-(b+c)
letters=[]
letters=lalpha+ualpha
l=[]
dig=[]
char=[]
for i in range(0,b):
  l.append(random.choice(letters))
for i in range(0,c):
  dig.append(random.choice(digits))
for i in range(0,d):
  char.append(random.choice(spchar))
p=l+dig+char
pas=""
for i in range(0,a):
  x=random.choice(p)
  pas=pas+x
  ind=p.index(x)
  p.remove(ind)

print(pas)

