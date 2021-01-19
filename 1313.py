#1313. Decompress Run-Length Encoded List

"""We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list. """


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        stk = []
        for x in range(1, len(nums), 2):
            a = nums[x-1]
            b = nums[x]
            stk += [b]*a



        return stk
    