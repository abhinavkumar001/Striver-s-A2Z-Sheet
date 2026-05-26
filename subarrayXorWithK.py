#Count the number of subarrays with given xor K
# A = [4, 2, 2, 6, 4]
# k = 6
# count=0
# freq={0:1}
# prefixXor=0
# for nums in A:
#     prefixXor^=nums
#     target = prefixXor^k
#     if target in freq:
#         count+=freq[target]
#     freq[prefixXor] = freq.get(prefixXor,0)+1
# print(count)


arr = [1,2,3]
k = 3
count=0
i=0
j=1
n=len(arr)
c=arr[0]
while(i<j and j<n):
  c=c+arr[j]
  if c==k:
    count+=1
    i+=1
    c=arr[i]
  elif c>k:
    i+=1
  j+=1
  if j==n:
    i+=1
    if i<n:
        c=arr[i]
    j=i+1

print(count)
