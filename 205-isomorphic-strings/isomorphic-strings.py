class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        new_dict = {}
        for i in range(len(s)):
            if s[i] in new_dict:
                if new_dict[s[i]] != t[i]:
                    return False
            else:
                new_dict[s[i]] = t[i]
        
        old_dict = {}
        for i in range(len(t)):
            if t[i] in old_dict:
                if old_dict[t[i]] != s[i]:
                    return False
            else:
                old_dict[t[i]] = s[i]
        return True


        