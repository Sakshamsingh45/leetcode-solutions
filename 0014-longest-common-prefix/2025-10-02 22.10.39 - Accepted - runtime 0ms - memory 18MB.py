class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if strs[0]==strs[-1]:
            return strs[0]
        i=0
        maxs=""
        while i<len(strs[0]):
            s1=strs[0]
            s2=strs[-1]
            if s1[i]==s2[i]:
                maxs+=s1[i]
            else:
                break
            i+=1
        return maxs
        

        