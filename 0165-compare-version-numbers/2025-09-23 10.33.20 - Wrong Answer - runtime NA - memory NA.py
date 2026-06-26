class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        if len(version1)>1:
            v1=int(version1[-1])
        else:
            v1=0
        if len(version2)>1:
            v2=int(version2[-1])
        else:
            v2=0
        if v1<v2:
            return -1
        elif v1>v2:
            return 1
        else:
            return 0
        