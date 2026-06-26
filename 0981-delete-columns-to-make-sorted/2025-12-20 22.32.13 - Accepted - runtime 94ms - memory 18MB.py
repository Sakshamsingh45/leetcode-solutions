class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            max1=0
            for j in range(len(strs)):
                if max1>ord(strs[j][i]):
                    count+=1
                    break
                max1=ord(strs[j][i])
        return count




        