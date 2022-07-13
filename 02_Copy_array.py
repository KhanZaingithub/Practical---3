arr1 = [2,5,4,7,5]

arr2 = [None]*len(arr1)

for i in range(0,len(arr1)):
    arr2[i] = arr1[i]

print()

print(" Original array is ")
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")    

print()   

print(" New array is ")
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")