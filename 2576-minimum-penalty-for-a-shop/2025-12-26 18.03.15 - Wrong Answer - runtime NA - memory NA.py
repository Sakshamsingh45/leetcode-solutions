class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty=len(customers)
        min_=0
        ope_n={"Y":0,"N":0}
        clos_e={"Y":0,"N":0}
        for i in customers:
            if i=="Y":
                clos_e["N"]+=1
            else:
                clos_e["Y"]+=1
        for j , k in enumerate(customers):
            min_penalty=ope_n["N"]+clos_e["Y"]
            if k=="N":
                clos_e["N"]-=1
                ope_n["N"]+=1
            else:
                clos_e["Y"]-=1
                ope_n["Y"]+=1
            if min_penalty<penalty:
                penalty=min_penalty
                min_=j
        return min_+1 if min_==len(customers)-1 else min_

