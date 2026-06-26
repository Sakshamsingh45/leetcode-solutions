class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
     
        if len(version1) < len(version2):
            version1.extend(["0"] * (len(version2) - len(version1)))
        elif len(version1) > len(version2):
            version2.extend(["0"] * (len(version1) - len(version2)))
        
        v1, v2 = "", ""
        for i in range(len(version1)):
            v1 += str(int(version1[i]))
        for i in range(len(version2)):
            v2 += str(int(version2[i]))
        
        v1, v2 = int(v1), int(v2)
        
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0
