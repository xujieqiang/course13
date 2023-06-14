print("回文测试！！")

number=int(input("请输入一个整数：："))

top=-1


def push(val):
	global top	
	top+=1
	stack.append(val)


def pop():
	global top
	d=stack[top]
	top-=1	
	stack.pop()
	return d



stack=[]
data=number
while data %10>0:
	x=data%10
	#print (x)
	push(x)	
	data=int(data/10)

栈的高度=top+1

二分之一栈的长度_=int(栈的高度/2)
print()
print(stack)
print()
hw=True
for i in range(二分之一栈的长度_):
	#print(top)
	x=pop()
	print(i,"-->",x,"-->",stack[i])
	if x!=stack[i]:
		hw=False

print()
if hw==True:
	print(number," 是回文数！")
else:
	print(number," 不是回文数！")