class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        sol=[]
        category={"electronics", "grocery", "pharmacy", "restaurant"}
        for i in range(len(code)):
            a=1
            if businessLine[i] in category and isActive[i]==True and code[i]!="" :
                for j in code[i]:
                    if 47<ord(j)<58 or 64<ord(j)<91 or 96<ord(j)<123 or j=="_":
                        continue
                    else:
                        a=0
                        break
                if a!=0:
                    sol.append(code[i])
        sol.sort()
        return sol





        