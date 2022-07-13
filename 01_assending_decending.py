arr = [5,2,8,7,1]
temp = 0

print ("Elements of original array is : ")
for i in range(0,len(arr)):
    print(arr[i],end=" ") # to write in one line

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
         temp = arr[i]
         arr[i] = arr[j]
         arr[j] = temp
print()

print(" Elements of array in ascending order : ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

for c in range(0,len(arr)):
    for k in range(c+1,len(arr)):
        if(arr[c]<arr[k]):
         temp = arr[c]
         arr[c] = arr[k]
         arr[k] = temp
print()    

print(" Elements of array in descending order : ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")