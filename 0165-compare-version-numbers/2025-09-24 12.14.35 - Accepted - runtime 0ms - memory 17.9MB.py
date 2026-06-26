class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        i, j = 0, 0
        while i < len(version1) and j < len(version2):
            v1, v2 = int(version1[i]), int(version2[j])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            i += 1
            j += 1
        
        # check leftovers in version1
        while i < len(version1):
            if int(version1[i]) > 0:
                return 1
            i += 1
        
        # check leftovers in version2
        while j < len(version2):
            if int(version2[j]) > 0:
                return -1
            j += 1
        
        return 0
