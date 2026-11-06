class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda y: y[1])
        queries = sorted((q, idx) for idx, q in enumerate(queries))
        seen=set()
        for i in logs:
            if i[0] not in seen:
                seen.add(i[0])
        unique_server=len(seen)
        seen={}
        l=0
        r=0
        res=[0]*len(queries)
        for i,idx in queries:
            while r<len(logs) and logs[r][1]<=i:
                seen[logs[r][0]]=seen.get(logs[r][0],0)+1
                r+=1
            while l<len(logs) and logs[l][1]<i-x:
                seen[logs[l][0]]-=1
                if seen[logs[l][0]]==0:
                    del seen[logs[l][0]]
                l+=1
            res[idx]=(n-len(seen))
        return res