arr = [2,5,4,7]

max = arr[0]

for i in range(0,len(arr)):
    if(arr[i]>max):
        max = arr[i]

print(f"{max} is the largest element in array ")        

min = arr[0]

for i in range(0,len(arr)):
    if(arr[i]<min):
        min  = arr[i]
print(f"{min} is the smallest element in array ")         