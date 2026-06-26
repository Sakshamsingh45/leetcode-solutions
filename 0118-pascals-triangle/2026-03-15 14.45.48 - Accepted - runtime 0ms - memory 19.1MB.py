class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        ans=[[1],[1,1]]
        for i in range(2,numRows):
            row=[1]
            prev=ans[i-1]
            for j in range(1,len(prev)):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            ans.append(row)
        return ans

