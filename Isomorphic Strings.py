class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        c = []
        for i in range(len(s)):
            c.append(s[i]+t[i])
        if len(set(s)) == len(set(t)) and len(set(s)) == len(set(c)):
            return True
        else:
            return False
