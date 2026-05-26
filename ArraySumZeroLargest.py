N = 8
array = [6, -2, 2, -8, 1, 7, 4, -10]
max=0
i=0
sum=array[i]
while(i<N):
    total=0
    j=i
    while(j<N):
        total+=array[j]
        if total==0:
            count=j-i+1
            if count>max:
                max=count
        j+=1
    i+=1
print(max)

