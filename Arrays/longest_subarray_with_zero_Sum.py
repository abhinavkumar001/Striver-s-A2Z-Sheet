'''
Problem: Length of the longest subarray with zero Sum
Solve: The best algorithm uses HashMap (Dictionary) with Prefix Sum.

Time Complexity:

Brute Force → O(N)^2
Optimal → O(N)
We use a Dictionary (HashMap) because it gives: Very fast searching
                                                Time Complexity O(1)
                                                A dictionary helps us do this instantly. Did the prefix sum appear before
'''

def longestZeroSumSubarray(arr):
    prefix_sum = 0
    index_map = {}   # stores first occurrence of prefix_sum
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: subarray from 0 to i has sum 0
        if prefix_sum == 0:
            max_len = i + 1

        # Case 2: prefix_sum seen before
        elif prefix_sum in index_map:
            max_len = max(max_len, i - index_map[prefix_sum])

        # Store first occurrence only
        else:
            index_map[prefix_sum] = i

    return max_len
arr = [9, -3, 3, -1, 6, -5]
print(longestZeroSumSubarray(arr))