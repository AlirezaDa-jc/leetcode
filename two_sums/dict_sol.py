class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            else:
                num_dict[nums[i]] = i

        return [None, None]


if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([3, 2, 4], 6)
    print(result)
