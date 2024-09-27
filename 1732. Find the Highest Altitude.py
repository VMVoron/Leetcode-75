class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s = 0
        max = 0 
        for i in gain:
          s = s + i
          if s > max:
            max = s
        return max
