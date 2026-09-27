class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_1 = -1
        index_2 = -1
        for i in range(len(nums) - 1):
            print(nums[i])
            print(range(i + 1, len(nums)))
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    index_1 = i
                    index_2 = j
                    break
        if index_1 == -1 or index_2 == -2:
            return None
        return [index_1, index_2]

if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([3,2,4] , 6)
    print(result)
