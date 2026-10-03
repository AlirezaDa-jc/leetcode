class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        dic = {}
        arr1_pointer = 0
        arr2_pointer = 0
        total_len = len(nums1) + len(nums2)

        for i in range(total_len):
            if arr2_pointer >= len(nums2) or (
                arr1_pointer < len(nums1)
                and nums1[arr1_pointer] < nums2[arr2_pointer]
            ):
                dic[i] = nums1[arr1_pointer]
                arr1_pointer += 1
            else:
                dic[i] = nums2[arr2_pointer]
                arr2_pointer += 1

        if total_len % 2 != 0:
            return float(dic[total_len // 2])
        else:
            return (dic[total_len // 2 - 1] + dic[total_len // 2]) / 2.0
