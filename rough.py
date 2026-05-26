matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row=len(matrix)
col=len(matrix[0])
print(f"{row} and {col}")
for i in range(0,row):
  for j in range(i,col):
    t=matrix[j][i]
    matrix[j][i]=matrix[i][j]
    matrix[i][j]=t
i=0;k=0
j=col-1
while(i<row):
  t=matrix[i][j]
  matrix[i][j]=matrix[i][k]
  matrix[i][k]=t
  i+=1
print(matrix)

