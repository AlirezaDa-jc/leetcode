class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            print(nums[i])
            print(target - nums[i])
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                if i < nums.index(target - nums[i]):
                    return [i, nums.index(target - nums[i])]
                else:
                    return [nums.index(target - nums[i]), i]
        return [None, None]


if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([3, 2, 4], 6)
    print(result)
