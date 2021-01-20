#1160. Find Words That Can Be Formed by Characters

"""You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 """

 class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = collections.Counter
        summ = 0
        ab = c(chars)
        for x in words:
            a = c(x)
            if all(a[y] <= ab[y] for y in x):
                summ += len(x)

        return summ
