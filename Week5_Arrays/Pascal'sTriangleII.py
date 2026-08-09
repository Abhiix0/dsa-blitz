class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res[rowIndex]

    #this problem can be solved in O(n^2) time complexity, where n is the rowIndex. We start with the first row of Pascal's Triangle and iteratively build each subsequent row by adding the two numbers above it. We use a temporary list to handle the edge cases by padding with zeros on both ends. Finally, we return the specific row at the given rowIndex.