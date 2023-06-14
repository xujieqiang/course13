# abcdcba
a=input("请输入一个判断是否是回文:")

长度_=len(a)
length=0
start=-1
end=-1
def findhw():
	global b
	global length
	global start
	global end
	i=0	
	 
	while i<长度_-1:
		j=i+1
		while j<长度_ :
			rs=Isequal(i,j)
			lle=-1
			if rs:
				lle=j-i+1
			if lle>length:
				length=lle
				start=i
				end=j
			j+=1
		i+=1
	# print(b[start:end])
	if start ==-1 or end==-1:
		return None
	return b[start:end+1]



# 偶数个数
def  Isequal(i,j):
	global b
	k=int((j-i+1)/2)
	ls=i
	hs=j
	n=0
	while n<k:
		if b[ls+n]!=b[hs-n]:
			#print("bad")
			return False
		n+=1
	return True
	

b=[]
for i in range(长度_):
	b.append(a[i])
# print("substr:",b[2:4])
print(str(b))
j=findhw()
print("-->",j)
huiwen=""
for k in j:
	huiwen+=k

print(huiwen)
