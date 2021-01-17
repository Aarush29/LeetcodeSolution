#946. Validate Stack Sequences

"""Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack."""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        y = 0
        for x in pushed:
            stk.append(x)
            while stk and stk[-1] == popped[y]:
                y += 1
                stk.pop()

        return len(stk) == 0
