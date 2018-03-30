c=[]
for i in range(0,1000):
	if i%3==0:
		c.append(i)
	if i%5==0 and i%3!=0:
		c.append(i)
d=sum(c)
print(d)
