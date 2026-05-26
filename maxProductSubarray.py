def maxProductSubArray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        curr = arr[i]
        if curr < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(curr, max_prod * curr)
        min_prod = min(curr, min_prod * curr)

        result = max(result, max_prod)

    return result

arr = [2, 3, -2, 4]
print(maxProductSubArray(arr))