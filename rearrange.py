arr = [1,2,-3,-1,-2,3]
n=len(arr)
i=0
j=1
while(i<j and j<n):
  if(arr[i]>=0 and arr[j]>=0):
    j+=1
    i+=1
  elif (arr[i]<0 and arr[j]<0):
    j+=1
    # i+=1
    # arr[i],arr[j]=arr[j],arr[i]
  elif (arr[i]<0 and arr[j]>=0):
    arr[i],arr[j]=arr[j],arr[i]
    i=j+1
    j=i+1
  else:
    i=j+1
    j=i+1
print(arr)