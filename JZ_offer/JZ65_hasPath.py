"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入
该格子。
"ABCESFCSADEE",3,4,"ABCCED" ==> true
"""


def hasPath(matrix, rows, cols, s):
    if not matrix:
        return False
    base = []
    for i in matrix:
        base.append(i)
    for i in range(rows):
        for j in range(cols):
            if base[i*cols+j] == s[0] and find_path(base, s, rows, cols, i, j):
                return True
    return False


def find_path(matrix, s, rows, cols, i, j):
    if not s:
        return True
    if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i*cols+j] == '0' or matrix[i*cols+j] != s[0]:
        return False

    curr_node_value = matrix[i*cols+j]
    matrix[i*cols+j] = '0'
    if find_path(matrix, s[1:], rows, cols, i, j+1) or find_path(matrix, s[1:], rows, cols, i+1, j) or find_path(matrix, s[1:], rows, cols, i-1, j) or \
            find_path(matrix, s[1:], rows, cols, i, j-1):
        return True
    matrix[i*cols+j] = curr_node_value
    return False


print(hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SGGFIECVAASABCEHJIGQEM"))