x="aabbcccccaaabbbbb"
y=[]
count=1
for e in range(len(x)-1):
  if(x[e]==x[e+1]):
    count+=1
  else:
    y.append(x[e-1])
    y.append(str(count))
    count=1
y.append(x[e+1])
y.append(str(count))
if(len(x)==len(y)):
  print(x)
else:
  print("".join(y))    
