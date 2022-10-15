

class Heap:
    def __init__(self,list):
        self.heap=list
        self.create_heap()

    def getLeft(self,index):
        return index*2+1

    def getRight(self,index):
        return index*2+2

    def getParent(self,index):
        return (index-1)//2

    def swim(self,index):

        node_value = self.heap[index]

        #可以不用马上交换位置，把父节点的值赋值给当前节点，直到找到最后的位置或堆顶时。
        while index > 0 and node_value < self.heap[self.getParent(index)]:
            self.heap[index] = self.heap[self.getParent(index)]
            index = self.getParent(index)
        self.heap[index] = node_value


    def create_heap(self):
        #遍历每个节点进行上浮操作
        if len(self.heap) <= 1:
            return
        for i in range(1, len(self.heap)):
            self.swim(i)

    def insert(self,num):

        self.heap.append(num)
        self.swim(len(self.heap)-1)


    def sink(self,index):

        node_value = self.heap[index]

        while self.getLeft(index) < len(self.heap):

            temp_index = self.getLeft(index)
            min_value = self.heap[temp_index]

            if self.getRight(index) < len(self.heap) and self.heap[self.getRight(index)] < min_value:

                temp_index = self.getRight(index)
                min_value = self.heap[temp_index]

            if min_value < node_value:

                self.heap[index] = min_value
                index = temp_index

            else:
                break
        self.heap[index] = node_value

    def pop(self):
        top = self.heap[0]
        tail = self.heap[-1]
        self.heap[0] = tail
        self.heap.pop()
        self.sink(0)
        return top


if __name__ == '__main__':
    heap = Heap([5,9,0,3,8,4,2,7,6])
    print(heap.heap)
    heap.insert(1)
    print(heap.heap)
    heap.pop()
    print(heap.heap)





