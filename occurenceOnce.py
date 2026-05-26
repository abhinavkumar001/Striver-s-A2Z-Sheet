# def sum(nums):
#     n=len(nums)
#     print("Array length",n)
#     i=0
#     j=1
#     while(i<n-1):
#         j=i+1
#         while j<n:
#             if nums[i]==nums[j]:
#                 i+=1
#                 temp=nums[i]
#                 nums[i]=nums[j]
#                 nums[j]=temp
#                 j+=1
#             else:
#                     j+=1
#         i+=1           
#     print("J value is")
#     return nums[i]


    
nums=[1,3,1,-1,3]
# print("Final Answer: ",sum(nums))
xor=0
for i in nums:
    xor^=i
print(xor)