import sys
 # for i = 1..n
def MatrixChainOrder(p, i, j):
    if i == j:
        return 0
    _min = sys.maxsize
    for k in range(i, j):
        count = (MatrixChainOrder(p, i, k)
                 + MatrixChainOrder(p, k + 1, j)
                 + p[i-1] * p[k] * p[j])
        if count < _min:
            _min = count
    # Return minimum count
    return _min
# Driver code
arr = [1, 2, 3, 4, 3]
n = len(arr)
print("Minimum number of multiplications is " , MatrixChainOrder(arr, 1, n-1))
 
