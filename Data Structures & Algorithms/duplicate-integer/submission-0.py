class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check if has dups
        if len(set(nums)) != len(nums):
            return True
        else: 
            return False