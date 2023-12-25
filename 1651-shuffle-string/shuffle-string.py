class Solution:
    
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list = [0]* len(s)
        for i in range(len(s)):
            new_list[indices[i]] = s[i]
        new_value = ""
        for val in new_list:
            new_value = new_value + val
        return new_value

        