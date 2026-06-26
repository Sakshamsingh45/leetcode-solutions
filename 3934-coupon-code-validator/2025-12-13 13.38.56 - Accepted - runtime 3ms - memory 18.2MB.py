class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        e, g, p, r = [], [], [], []
        category={"electronics", "grocery", "pharmacy", "restaurant"}
        for i in range(len(code)):
            a=1
            if businessLine[i] in category and isActive[i]==True and code[i]!="" :
                for j in code[i]:
                    if j.isalnum() or j=="_":
                        continue
                    else:
                        a=0
                        break
                if a!=0:
                    if businessLine[i] == "grocery": g.append(code[i])
                    if businessLine[i] == "electronics": e.append(code[i])
                    if businessLine[i] == "pharmacy": p.append(code[i])
                    if businessLine[i] == "restaurant": r.append(code[i])
        
        return sorted(e) + sorted(g) + sorted(p) + sorted(r)





        