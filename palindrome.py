arr=[1,4,4,1]
i=0
j=len(arr)-1
while i<=j:
    if arr[i]==arr[j]:
      print("not palindrome")
    else: 
       print("Palindrome")
       