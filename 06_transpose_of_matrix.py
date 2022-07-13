A = [[5,4,3],
     [2,4,6],
     [4,7,9]]

trans = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for a in range(len(A)):
 for b in range(len(A[0])):
    trans[b][a] = A[a][b]

print(" Original array is : ")
for a in range(len(A)):
  for b in range(len(A[0])):
    print(trans[a][b],end=" ") 
  print()    
print(" Transpose array is : ")
for a in range(len(A)):
  for b in range(len(A[0])):
    print(A[a][b],end=" ") 
  print()    
  