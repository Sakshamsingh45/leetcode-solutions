class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        # Pad with "0" so lengths match
        while len(version1) < len(version2):
            version1.append("0")
        while len(version2) < len(version1):
            version2.append("0")

        v1, v2 = "", ""
        for i in range(len(version1)):
            # zero-fill to width 5 (enough for typical version numbers)
            v1 += str(int(version1[i])).zfill(5)
        for i in range(len(version2)):
            v2 += str(int(version2[i])).zfill(5)

        v1, v2 = int(v1), int(v2)

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0
