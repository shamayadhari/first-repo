l1=[0,2,0,3,4,0,7,8,0]
#All the zeros to be shifted at the end of the list and the non zero elements 
#to be shifted at start 
i=0
l2 = []
for i in l1:
    if i != 0:
        l2.append(i)

for i in l1:
    if i == 0:
        l2.append(i)

print(l2)

# Second method 
i = 0
for n in l1:
    if n != 0:
        l1[i] = n
        i += 1

while i < len(l1):
    l1[i] = 0
    i += 1


# Third method 
i=0
j=1

nums=
mp={}
l1=[]
for i in range len(nums):
var=target-nums[i]
