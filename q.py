import queue

q=queue.Queue(10)

print("队列总的可以容纳的个数：",q.maxsize)
print()
q.put(123)
q.put(456)
q.put(66)
q.put(63)
q.put(43)

print("第一个进去的是： 123，先得到：",q.get())
print("第二个进去的是： 456，再得到：",q.get())


print()
print("查看队列中还存有的元素： ")
print(q.queue)


