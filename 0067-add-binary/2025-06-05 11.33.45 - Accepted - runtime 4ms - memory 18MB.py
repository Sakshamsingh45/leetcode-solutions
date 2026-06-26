class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d = max(len(a), len(b))
        bo = 0
        e =1
        f =1
        result = ""

        while d > 0:
            if e<len(a)+1:
                g = int(a[-e])
            else:
                g=0
            if f<len(b)+1:
                h = int(b[-f])
            else:
                h=0

            total = g + h + bo
            if total == 0:
                result = "0"+ result
                bo = 0
            elif total == 1:
                result ="1"+ result
                bo = 0
            elif total == 2:
                result = "0"+ result
                bo = 1
            elif total == 3:
                result = "1"+result
                bo = 1

            e += 1
            f += 1
            d -= 1

        if bo == 1:
            result ="1"+ result
            bo=0

        return result
