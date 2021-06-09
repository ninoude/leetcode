from IPython import embed
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=0
        q=p+1
        if len(s) < 2:
            return len(s)
        
        hash = {s[0]: 1}
        max = len(hash)
        tmp=0
        while p < len(s) and q < len(s):
            if s[q] in hash.keys():
                p = p+1
                q = p+1
                if q > len(s)-1:
                    return max
                else:
                    hash = {s[p]: 1}
            else:
                hash[s[q]]=1
                q = q+1
                tmp = len(hash)
                if  max < tmp:
                    max = tmp
        return max

sample = Solution()
#print(sample.lengthOfLongestSubstring("abcabcbb"))
#print(sample.lengthOfLongestSubstring("bb"))
print(sample.lengthOfLongestSubstring("pwwkew"))
