class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        Calculate the greatest common divisor (GCD) of two strings.
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # Define a recursive function to compute the GCD
        # This could be replaced with the built-in math.gcd() function
        # However, a custom implementation is used due to specific requirements
        # a and b are length of strings
        a = len(str1)
        b = len(str2)
      
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
            # for example
            # a = 8, b = 16
            # start
            # 16 8 ,8  2, 2, 2, b =0 -> a = 2 = gcd
            # the last digit becomes the first when mixing

        # Check if str1 + str2 forms a palindrome
        # ensures that the pattern of characters in both strings is compatible for them to have a common divisor string
        # https://algo.monster/liteproblems/1071
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate the GCD of the lengths of str1 and str2
        # Return the substring of str1 up to the computed GCD
        return str1[: gcd(a, b)]
