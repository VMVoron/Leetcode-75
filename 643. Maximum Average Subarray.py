from decimal import Decimal

class Solution:
    def findMaxAverage(self, nums, k):
        ans = s = sum(nums[:k])

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)

        # Используем Decimal для точного деления
        return Decimal(ans) / Decimal(k)
