class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return False if len(bits)%2==0  else True
        