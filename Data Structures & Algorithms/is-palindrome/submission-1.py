import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s== " ":
            return True
        list1=s.split()
        strbuild = ''

        for i in list1:
            strbuild+=(i.lower())
            result = re.sub(r'[^\w\s]','',strbuild)
        
        
        return result == result[::-1]