class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict={}
        for i in strs:
            temp=[]
            for j in i:
                temp.append(j)
            temp.sort()
            temp=tuple(temp)
            if temp not in dict:
                dict[temp]=[]
            dict[temp].append(i)
        return list(dict.values())