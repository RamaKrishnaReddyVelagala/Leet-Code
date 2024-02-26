class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dic = dict()
        for i in range(len(nums)): # O(n)
            if nums[i] in new_dic:
                    return i, new_dic[nums[i]]
            new_dic[target - nums[i]] = i

# a + b = 9
# a : (9-b) -----> 


# create a dictionary:
#   {
#       7: 2,
#       2: 7,
#       -1: 11,
#       -6: 15
#   }

# loop through nums, check if number is in new_dic. return index, and also index of other.
# if indexes are same, ignore.


# index -method.
