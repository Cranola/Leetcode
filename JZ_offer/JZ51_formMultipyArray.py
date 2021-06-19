def multiply(A):
    # write code here
    C = []
    D = []
    B = []
    for i in range(len(A)):
        if i == 0:
            C.append(1)
            D.append(1)
        else:
            C.append(C[i-1] * A[i-1])
            D.append(D[i-1] * A[len(A)-i])

    for k in range(len(A)):
        B.append(C[k] * D[len(A)-1-k])
    return B


print(multiply([1,2,3,4,5]))