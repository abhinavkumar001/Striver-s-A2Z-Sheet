
def maxProductSubArray(arr):
    prod=arr[0]
    max_prod=arr[0]
    result=arr[0]
    for i in range(1,len(arr)):
        curr = arr[i]
        if curr < 0:
            prod,max_prod = max_prod,prod
        max_prod = max(curr,max_prod*curr)
        prod = min(curr,prod*curr)
    return max(result,max_prod)


arr= [1,2,-3,0,-4,-5]
print(f"Maximum product of the SubArray is:{maxProductSubArray(arr)}")