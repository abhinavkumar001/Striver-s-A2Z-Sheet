class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, 3, 1, 4,5,2]
    print("Minimum jumps required:", sol.jump(nums))
