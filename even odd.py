# Odd even 
num=int(input("Enter a number"))
if (num%2==0):
    print("Num is even")
else:
    print("Num is odd")

# Prime no.
n=int(input("Enter a number"))
if n<=1:
    print("not prime")
else:
    for i in range (2,n):
        if n % i==0:
            print("not prime")
            break
    else:
        print("prime")

i = 0
for num in l1:
    if num != 0:
        l1[i] = num
        i += 1

while i < len(l1):
    l1[i] = 0
    i += 1

  
