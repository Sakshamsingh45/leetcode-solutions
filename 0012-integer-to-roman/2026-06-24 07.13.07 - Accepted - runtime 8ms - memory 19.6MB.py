class Solution:
    def intToRoman(self, num: int) -> str:
        ir = {1: "I",2: "II",3: "III",4: "IV",5: "V",6: "VI",7: "VII",8: "VIII",9: "IX",10: "X",20: "XX",30: "XXX",40: "XL",50: "L",60: "LX",70: "LXX",80: "LXXX",90: "XC",100: "C",200: "CC",300: "CCC",400: "CD",500: "D",600: "DC",700: "DCC",800: "DCCC",900: "CM",1000: "M",2000: "MM",3000: "MMM"}

        po=0
        ans=""
        while num!=0:
            if num%10==0:
                pass
            else:
                ans=ir[(num%10)*(10**po)]+ans
            num//=10
            po+=1
        return ans