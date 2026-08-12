class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total = []
        while matrix:

            total+=(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    total.append(row.pop())

            if matrix:
                total+=(matrix.pop()[::-1])

            if matrix and matrix[0]:

                for row in matrix[::-1]:
                    total.append(row.pop(0))

        return total