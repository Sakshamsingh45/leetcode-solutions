class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a=0
        for i in operations:
            if i[0]=="-" or i[-1]=="-":
                a-=1
            else:
                a+=1
        return a
