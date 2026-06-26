class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        arr = [[1], [1, 1]]

        for i in range(2, numRows):
            prev = arr[i - 1]
            row = [1]  # First element of each row is always 1
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])  # Middle elements
            row.append(1)  # Last element is always 1
            arr.append(row)

        return arr
