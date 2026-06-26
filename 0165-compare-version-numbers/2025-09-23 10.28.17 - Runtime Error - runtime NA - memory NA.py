class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        v1=int(version1[1])
        v2=int(version2[1])
        if v1<v2:
            return -1
        elif v1>v2:
            return 1
        else:
            return 0
        