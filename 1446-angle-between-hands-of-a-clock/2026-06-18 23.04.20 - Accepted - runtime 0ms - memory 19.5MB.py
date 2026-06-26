class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if minutes:
            h=(((hour%12)*5)+(5/(60/minutes)))
        else:
            h=((hour%12)*5)
        angle=abs((minutes-h)*6)
        return min(angle,360-angle)