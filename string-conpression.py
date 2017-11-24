# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.


# Follow up:
# Could you solve it using only O(1) extra space?

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur = chars[0]
        num = 1
        result = ""
        for i in chars[1:]:
            if i == cur:
                num += 1
            else:
                result += cur if num == 1 else cur + str(num)
                cur = i 
                num = 1
        result += cur if num == 1 else cur + str(num)
        chars = list(result)
        return len(result)


if __name__ == "__main__":
    print(Solution().compress(["a","a","b","b","c","c","c"]))