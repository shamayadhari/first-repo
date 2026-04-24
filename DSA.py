# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class SLL:
#     def __init__(self,head=None):
#         self.head = head

#     def is_empty(self):
#         return self.head==None

#     def insert_at_Begining(self,data):
#         new_node = Node(data,self.head)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_pos(self,data,val):
#         temp=self.next
#         while temp.next and temp.data!=val:
#             temp=temp.next
#         if temp is None:
#             print("POS is not in list")

#     def insert_at_last(self,data):
#         n=Node(data)
#         if not self.is_empty():
#             temp = self.head
#             while temp.next is not None:
#                 temp=temp.next
            
#             temp.next = n
#         else:
#             self.start = n
        
#     def delete_at_begining(self):
#         temp = self.head
#         self.head = self.head.next

#     def delete_Node(self,data):
#         dummy = Node(0)
#         dummy.next = self.head
#         curr = dummy
#         temp = curr.next
#         while temp:
#             if temp.data == data:
#                 curr.next =temp.next
#                 del temp
        
#             curr = curr.next
#             temp = temp.next


    
#     def search(self,data):
#         temp = self.head
#         while temp is not None:
#             if temp.item == data:
#                 return temp
            
#             print(temp.item)
#             temp = temp.next
#         return None
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end=" -> ")
#             temp = temp.next
#         print("None")
    


# # mylist = SLL()
# # mylist.insert_at_Begining(10)
# # mylist.insert_at_Begining(90)
# # mylist.insert_at_Begining(30)
# # mylist.insert_at_last(40)
# # mylist.delete_at_begining()
# # mylist.delete_Node(30)
# # mylist.display()

# class node:
#     def __init__(self,data=None,next=None,prev=None):
#         self.data=data
#         self.next=next
#         self.prev=None

# class DLL:
#     def __init__(self,head=None):
#         self.head=head

#     def insert_at_begining(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return 
#         new_node.Pre=self.head 
#         self.head.Prev=new_node
#         self.head=new_node

#     def insert_at_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return
#         temp=self.head
#         while temp.next:
#             temp=temp.next 

# def insert_at_pos(self,data,val):
#     new_node=Node(data)
#     temp=self.head
#     while temp.next and temp.data!=val:
#         temp=temp.next
#     if temp is None:
#         print("Val is not list")
#     new_node.Pre=temp
#     new_node.next=temp.next
    
# #diff between singly and doubly linked list 
# #''     ''    singly and circular  ''   ''
# #''      ''   doubly and circular  ''   ''

# class stack:
#     def __init__(self):
#         self.stack=[]

#     def push(self,data):
#         self.stack.aapend(data)

#     def pop(self):
#         if len(self.stack==0):
#             print("Underflow")
#         else:
#             self.stack.pop()

#     def peek(self):
#         if len(self.stack==0):
#             print("Underflow")
#         else:
#            print(self.stack[-1])

#     def empty(self):
#         if len(self.stack)==0:
#                 print("Stack is empty")
#         else:
#                 print("not empty")

#     def size(self):
#             print (len(self.stack))

#     def display(self):
#         while len(self.stack)>0:
#             print(self.peek())
#             self.pop()

# s=stack()
# s.pop()
# s.empty()
# s.push(22)
# s.display()
            
# #Reverse 
# def reverse(self,head):
#     curr=head
#     temp=None
#     prev=None
#     while curr is not None:
#         temp=curr.next
#         curr.next=prev
#         prev=curr
#         curr=temp
#         return prev
# def isplaindrome():

# SEARCHING 

# def serach(list,key):
#     for i in range(len(list)):
#         if list[i]==key:
#             return 1

# #merge sort 

# class Solution(object):
#     def sortArray(self, nums):
#         if len(nums) <= 1:
#             return nums
        
#         mid = len(nums) // 2
#         left = self.sortArray(nums[:mid])
#         right = self.sortArray(nums[mid:])
        
#         return self.merge(left, right)
    
#     def merge(self, left, right):
#         result = []
#         i = j = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
        
#         result.extend(left[i:])
#         result.extend(right[j:])
        
#         return result
    
# #Bubble sort
# class Solution(object):
#     def bubbleSort(self, nums):
#         n = len(nums)
        
#         for i in range(n):
#             swapped = False
            
#             for j in range(0, n - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                     swapped = True
            
#             if not swapped:
#                 break
        
#         return nums

arr=[1,-2,3,0,-4,7,6,2,9]   
def selectionsort(arr):
    n=len(arr)

    for i in range(n):
        min_index=i 
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
selectionsort(arr)
print(arr)

#Tree 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
root.left=Node(5)
root.right=Node(6)

# BFS (Breadth first search - Pre order (Root left right), Inorder (Left root right), Postorder ()
# DFS (Depth first search)

def preoder(self,root):
    l1=[]
    if root is None:
        return 1
    traverse(root,1)

#POST ORDER 

def post(self,root):
    l1=[]
    self.traverse(root,l1)
    return l1
def traverse(self,root,l1):
        if root is None:
            return
        self.traverse(root.left,l1)
        self.traverse(root.right,l1)
        l1.append(root.val)

#CONSTRUCT TREE
l1=int(input("Enter the number of nodes in tree: "))
nodes = []  
for i in range(l1):
    data = int(input(f"Enter the value of node {i+1}: "))
    nodes.append(Node(data))
for i in range(l1):
    left_index = int(input(f"Enter the index of left child for node {i+1} (or -1 if no left child): "))
    right_index = int(input(f"Enter the index of right child for node {i+1} (or -1 if no right child): "))
    if left_index != -1:
        nodes[i].left = nodes[left_index]
    if right_index != -1:
        nodes[i].right = nodes[right_index]

#Sir's method for construct tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
l1=int(input("Enter the number of nodes in tree: "))
root=fromTree(l1)
def fromTree(l1):
    if not l1:
        return None
    val=l1.pop(0)
    if val is None:
        return None 
    mains=Node(val)
    mains.left=fromTree(l1)
    mains.right=fromTree(l1) 
    return mains


#Again sir's method for construct tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Traverse:

    def build(self,values):
        if not values:
            return None

        val = values.pop(0)

        if val is None:
            return None

        root = Node(val)
        root.left = self.build(values)
        root.right = self.build(values)

        return root

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)



values = [1, 2, 4, None, None, 5, None, None, 3, None, 6]
T = Traverse()
root = T.build(values)
T.inorder(root)     
    

#GRAPH 
class Graph:
    def __init__(self):
        dict={}
    def add(self,s,d):
        if s is not in self.dict:
            self.dict[s]=[]
            