class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs=[]
        potions.sort()
        for i in range (len(spells)):
            j=0
            while j < len(potions):
                if spells[i]*potions[j]>=success:
                    pairs.append(len(potions)-j)
                    break
                elif j==len(potions)-1 :
                    pairs.append(0)
                j+=1
        return pairs