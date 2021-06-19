def movingCount(m: int, n: int, k: int) -> int:
    # 特殊情况讨论
    if m<0 or n<0 or k<0:
        return 0

    # 初始化矩阵并计算位数和
    matrix = [[count_sum(i, j) for j in range(n)] for i in range(m)]

    # dfs查找
    res = dfs(matrix, 0, 0, k, m, n)
    return res

def count_sum(ind1, ind2):
    ind_sum = 0
    while ind1 // 10 > 0:
        ind_sum += ind1 % 10
        ind1 = ind1 // 10
    ind_sum += ind1

    while ind2 // 10 > 0:
        ind_sum += ind2 % 10
        ind2 = ind2 // 10
    ind_sum += ind2
    return ind_sum

def dfs(matrix, row_ind, col_ind, k, rows, cols):
    # 标记已到过
    matrix[row_ind][col_ind] = 'p'
    init = 1
    if col_ind - 1 > 0 and matrix[row_ind][col_ind - 1] != 'p' and matrix[row_ind][col_ind - 1]<k:
        init += dfs(matrix, row_ind, col_ind - 1, k, rows, cols)
    if col_ind + 1 < cols and matrix[row_ind][col_ind + 1] != 'p' and matrix[row_ind][col_ind + 1]<k:
        init += dfs(matrix, row_ind, col_ind + 1, k, rows, cols)
    if row_ind - 1 > 0 and matrix[row_ind-1][col_ind] != 'p' and matrix[row_ind-1][col_ind]<k:
        init += dfs(matrix, row_ind-1, col_ind, k, rows, cols)
    if row_ind + 1 < rows and matrix[row_ind+1][col_ind] != 'p' and matrix[row_ind+1][col_ind]<k:
        init += dfs(matrix, row_ind+1, col_ind, k, rows, cols)
    return init

print(movingCount(1,2,1))