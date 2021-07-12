count=0
data=[]
with open ('reviews.txt','r')as a:
	for line in a:
		data.append(line)
		count+=1
		if count % 1000 == 0:
			print(len(data))
print('總共有',len(data),'筆留言')
sum=0
for p in data:
	sum=sum+len(p)
	g=sum/len(data)
	g=int(g)
print('平均約',g,'個字')
dog=[]
for d in data:
	if len(d)<100:
		dog.append(d)
print('總共有',len(d),'比留言小於100個字')
cat=[]
for h in data:
	if 'good' in h:
		cat.append(cat)
print('一共有',len(cat),'比留言含有good')
	



