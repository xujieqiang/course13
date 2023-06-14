

top=-1
print("第13课 课程演示")

def push(val):
	global top
	top+=1
	stack.append(val)


def pop():
	global top
	if top<=-1:
		print("栈已经空了，没有可以弹出的")
		return -1
	else:
		x=stack[top]
		top-=1
		stack.pop()
		return x


def getTop():
	global top
	if top<=-1:
		print("栈已经空了，无法获取栈顶")
		return -1
	else:
		return stack[top]

# 定义一个栈，为空栈
stack=[]

# 压入栈
for i in range(10):
	push(i)


print("原始的栈：",stack)
print()
print("top  栈顶是：",top)
print()
print("栈顶元素是::",getTop())
print()
print("===============================================")

pop()
pop()
pop()
pop()


push(9)
push(8)
push(7)


print()
print("9，8，7按顺序压入栈，\n压入后栈的表：",stack)
print()
print("top  栈顶是：",top)
print()
print("栈顶元素是::",getTop())
print()
print("===============================================")

print()
print("元素全部出栈后的顺序是：")
l=len(stack)
for i in range(l):
	rs=pop()
	print(rs ,end="")
	if i<l-1:
		print(" --->  ",end="")

print()
print()
print("================================================")
print()
print("出栈后，栈中的元素::")
print("可以看到元素为空： ",stack)
print()
print()




