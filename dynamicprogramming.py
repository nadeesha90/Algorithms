#solutions to some dynamic programming problems

#https://leetcode.com/problems/maximum-subarray/description/
def maxsubarray(nums):
    m = [0]*len(nums)
    m[0] = nums[0]
    max_val = m[0]

    for i in range(1,len(nums)):
        m[i] = max(m[i-1]+nums[i], nums[i])
        max_val = max(m[i],max_val)
    return max_val 

#https://leetcode.com/problems/unique-paths/description/
def uniquePaths(m,n):
    arr = [[0 for x in range(m)] for y in range(n)]

    for i in range(m):
        arr[0][i] = 1

    for i in range(n):
        arr[i][0] = 1

    for x in range(1,m):
        for y in range(1,n):
            arr[y][x] = arr[y-1][x] + arr[y][x-1]

    return arr

#https://leetcode.com/problems/knight-probability-in-chessboard/
h = {}
def knightprobability(N,K,x,y):
    def get_moves(x,y):
        offset = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        moves = [(x+o[0],y+o[1]) for o in offset]
        return moves

    def onboard(x,y):
        return False if x >= N or y >= N or x < 0 or y < 0 else True

    key = K,x,y
    if key in h:
        return h[key]

    if onboard(x,y) == False:
        h[key] = 0.0
        return 0.0
    elif K == 0:
        h[key] = 1.0
        return 1.0
    elif K > 0:
        p = 0
        for x_n,y_n in get_moves(x,y):
            p += knightprobability(N,K-1,x_n,y_n)*(0.125)            
        h[key] = p
        return p

#https://leetcode.com/problems/continuous-subarray-sum/description/
def csasum(arr,k):
    for i in range(1,len(arr)):
        a = arr[i]
        rem = (k-1)-(a%k)
        if csasum_help(arr,i,k,rem) == True:
            return True

def csasum_help(arr,n,k,rem):
    if n == 0:
        return True if arr[n]%k == rem else False
    else:
        if arr[n]%k == rem:
            return True
        else:
            new_rem = (k-1) - (rem + arr[n])%k
            return csasum_help(arr,n-1,k,new_rem)

#https://leetcode.com/problems/k-inverse-pairs-array/description/
def kinversepairs(n,k):
    arr = [[None for i in range(k+1)] for j in range(n+1)]
    for x in range(2,n+1):
        arr[x][0] = 1
    arr[1]
    for y in range(n+1):
        arr[0][y] = 0

#https://leetcode.com/problems/perfect-squares/description/
def perfect_squares(n):
    i = 1
    ps = []
    while i*i <= n:
        ps.append(i*i)
        i += 1
    return ps

def numsquares(n):
    if n == int(math.sqrt(n))*int(math.sqrt(n)):
        return 1
    else:
        ps = perfect_squares(n)
        ns = [numsquares(n-p)+1 for p in ps]
        return min(ns)

if __name__ == '__main__':
    print knightprobability(10,100,3,4)
    arr = [23,2,4,6,7]
    print csasum(arr,6)

