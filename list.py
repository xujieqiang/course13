####################################
# 一个名字为a  的列表，是个空的列表
#####################################

a=[]

for i in range(6):
	a.append(i)

print("a列表的数据：",a)
print()

print("列表里的第二项： ",a[1])
print("列表里的第三项： ",a[2])


print("=========================")
a[1]=101
a[2]=32
print("修改后的第二项： " ,a[1])
print("修改后的第三项： ",a[2])


a.append(334)
print("==========================")
print("添加一项后，a列表是这样的: ",a)

