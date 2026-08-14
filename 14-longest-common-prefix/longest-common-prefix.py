class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        prefix=v[0]
        for word in v[1:]:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
        return prefix
            
        