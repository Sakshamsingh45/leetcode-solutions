class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans=[]
        for i in queries:
            for j in dictionary:
                dis=0
                for k in range(len(i)):
                    if i[k]!=j[k]:
                        dis+=1
                    if dis>2:
                        break
                if dis<=2:
                    ans.append(i)
                    break
        return ans
