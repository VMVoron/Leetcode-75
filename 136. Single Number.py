class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = sum(set(nums))
        sum_nums = sum(nums)

        return 2 * set_nums - sum_nums   
