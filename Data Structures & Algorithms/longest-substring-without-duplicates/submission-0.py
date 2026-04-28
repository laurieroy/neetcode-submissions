class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        longest = 0
        n = len(s)

        for r in range(n):
            while(s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            window_width = (r-l) + 1 
            longest = max(longest, window_width)
            charSet.add(s[r])
        
        return longest