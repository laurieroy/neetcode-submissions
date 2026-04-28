class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        hashmap = {")":"(", "}":"{", "]":"[" }
        stk = []


        for char in s:
            if char not in hashmap:
                # store in stack
                stk.append(char)
            else: 
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[char]:
                        return False
        
        return not stk