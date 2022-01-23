input=str(input("please enter a string"))
frq={}

for i in input:
  if i in input:
    frq[i]=frq.get(i,0)+1

print(dict(sorted(frq.items())))
