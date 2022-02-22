class Solution:
    #Heapify function to maintain heap property.
    def upheap(self, arr, n, i):
        parent = self.parent(i)
        if i>0 and arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            self.upheap(arr, n, parent)
    def downheap(self, arr, n, i):
        minChildPos = self.leftChild(i)
        if minChildPos >= n :
            return
        if self.rightChild(i) < n  and arr[minChildPos] > arr[self.rightChild(i)]:
            minChildPos = self.rightChild(i)
        if arr[i] > arr[minChildPos]:
            arr[i], arr[minChildPos] = arr[minChildPos], arr[i]
            self.downheap(arr,n,minChildPos)
        
    def heapify(self,arr, n, i):
        self.upheap(arr,n,i)
        self.downheap(arr,n,i)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n):
            self.upheap(arr, n, i)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        while n > 0:
            self.remove(arr,n,0)
            n-=1
        arr.reverse()

    def insert(self, arr,n, elem):
        arr.append(elem)
        self.upheap(arr, n, n- 1)
    
    def remove(self, arr,n, i):
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
        self.heapify(arr, n-1, i)
        
    def getMin(self, arr):
        return arr[0]
    
    def leftChild(self, i):
        return (2*i) + 1
    
    def rightChild(self, i):
        return (2*i) + 2

    def parent(self, i):
        return (i-1)//2