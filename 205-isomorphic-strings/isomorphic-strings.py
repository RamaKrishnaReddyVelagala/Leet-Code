class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}
        for s_val, t_val in  zip(s, t):
            if ((s_val in s_dict and s_dict[s_val] != t_val) or
            (t_val in t_dict and t_dict[t_val] != s_val)):
                    return False
            s_dict[s_val] = t_val
            t_dict[t_val] = s_val

        return True


        