class Solution:
    def judgeCircle(self, moves: str) -> bool:
        freq={"R":0,"L":0,"U":0,"D":0}
        for i in moves:
            freq[i]+=1
        return freq["R"]==freq["L"] and freq["U"]==freq["D"]