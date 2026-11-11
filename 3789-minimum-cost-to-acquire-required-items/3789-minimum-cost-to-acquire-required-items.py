class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost=cost1*need1+cost2*need2
        mn=min(need1,need2)
        n_cost=(need1-mn)*cost1+(need2-mn)*cost2+mn*costBoth
        if n_cost<cost:
            cost=n_cost
        n_cost=costBoth*max(need1,need2)
        if n_cost<cost:
            cost=n_cost
        return cost