
def isSquare(arr):
    return arr.ndim == 2 and np.shape(arr)[0] == np.shape(arr)[1] 

def isUnique(arr):
    return np.size(arr) == np.size(np.unique(arr))

def isMagicSquare(arr):
    if not (isSquare(arr) and isUnique(arr)):
        return False
    
    x = arr.trace()
    m = np.shape(arr)[0]
    n = 0
    
    for i in range(m):
        if(x <> np.sum(arr[i,:]) or x <> np.sum(arr[:,i])):
            return False
        n += arr[i,m-i-1]
    
    return n == x    