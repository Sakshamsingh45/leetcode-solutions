class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq={"B":0,"W":0}
        for i in range(k):
            freq[blocks[i]]+=1
        count=freq["W"]
        l=0
        for r in range(k,len(blocks)):
            freq[blocks[l]]-=1
            freq[blocks[r]]+=1
            count=min(count,freq["W"])
            l+=1
        return count

