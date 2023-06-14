class 链表节点:
	def __init__(self,val):
		self.value=val
		self.next=None



Node=None


# 默认的头节点是空的，就是没有节点
头节点_=None

#  True 是空的，  而False是 有头节点的
def 链表是否为空():
	global 头节点_
	if 头节点_ !=None:
		return False
	return True


def 插入节点(val):
	global 头节点_
	node1=链表节点(val)
	node1.next=头节点_
	头节点_=node1
	
		

def 链表长度():
	global 头节点_
	current=头节点_
	节点数_=0
	while current!=None:
		节点数_+=1
		current=current.next

	return 节点数_


def 从链表尾部插入节点():

插入节点(10)

插入节点(20)

插入节点(230)




print(链表长度())
