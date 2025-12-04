class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        seenS = {}
        seenT = {}

        for word in s:
            seenS[word] = seenS.get(word, 0) + 1
        for word in t:
            seenT[word] = seenT.get(word, 0) + 1
        return seenS == seenT
