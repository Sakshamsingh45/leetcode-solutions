class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        
        max_reachable=None
        for i in towers:
            if abs(i[0]-center[0])+abs(i[1]-center[1])<=radius:
                reachable=i
            else:
                continue
            if max_reachable is None or reachable[2]>max_reachable[2]:
                max_reachable=reachable
            elif reachable[2]==max_reachable[2]:
                if (reachable[0]<max_reachable[0]) or (reachable[0]==max_reachable[0] and reachable[1]<max_reachable[1]):
                    max_reachable=reachable
        if max_reachable is None:
            return [-1,-1]
        return [max_reachable[0],max_reachable[1]]