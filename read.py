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