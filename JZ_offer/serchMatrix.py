# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return list()
        else:
            row, col = len(matrix), len(matrix[0])
            i, j = 0, 0
            res = list()
            # 截止条件
            while i*2 <= row and j*2 <= col:
                data = self.run_one_circle(matrix, i, j, row, col)
                res.extend(data)
                i += 1
                j += 1
            return res

    def run_one_circle(self, matrix, start_row, strat_col, row, col):
        if start_row > row-start_row-1 or strat_col > col-strat_col-1:
            return list()
        else:
            res = list()
            for n in range(strat_col, col-strat_col):
                res.append(matrix[start_row][n])
            for m in range(start_row+1, row-start_row):
                res.append(matrix[m][col-strat_col-1])

            if start_row < row-start_row-1:
                for n in range(col-strat_col-2, strat_col-1, -1):
                    res.append(matrix[row-start_row-1][n])
            if strat_col < col-strat_col-1:
                for m in range(row-start_row-2, start_row, -1):
                    res.append(matrix[m][strat_col])
            return res


data1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
data2 = [[1],[2],[3],[4],[5]]
data3 = [[1,2,3,4,5]]
sol = Solution().printMatrix(data3)
print(sol)

