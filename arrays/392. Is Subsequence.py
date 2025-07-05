class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx, t_idx = 0, 0

        while s_idx < len(s) and t_idx < len(t):
            # if the elements match, increment s_idx
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            #always increment t_idx
            t_idx += 1
        return s_idx == len(s) # check if s_idx == len(s) to see seq s is all matched 
