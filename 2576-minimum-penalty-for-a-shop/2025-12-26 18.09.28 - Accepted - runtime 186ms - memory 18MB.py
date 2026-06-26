class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        min_ = 0

        ope_n = {"Y": 0, "N": 0}
        clos_e = {"Y": 0, "N": 0}

        # initially, everything is closed
        for c in customers:
            if c == "Y":
                clos_e["Y"] += 1
            else:
                clos_e["N"] += 1

        # evaluate closing times 0..n-1
        for j, k in enumerate(customers):
            # penalty for closing at time j
            curr_penalty = ope_n["N"] + clos_e["Y"]

            if curr_penalty < penalty:
                penalty = curr_penalty
                min_ = j

            # now move hour j from closed → open
            if k == "N":
                clos_e["N"] -= 1
                ope_n["N"] += 1
            else:
                clos_e["Y"] -= 1
                ope_n["Y"] += 1

        # check closing at time n
        if ope_n["N"] < penalty:
            min_ = len(customers)

        return min_