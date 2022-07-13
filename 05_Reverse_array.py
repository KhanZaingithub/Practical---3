arr = [2,5,4,7]

print()

print(" Original array is ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")  
print()
print(" Reverse array is ")
for i in range(len(arr)-1,-1,-1):  #-1  -1 is used for decreasing i by 1
    print(arr[i],end=" ")