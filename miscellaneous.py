def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    ret = 0
    while x > 0:
        rem = x%10
        ret = ret*10 + rem
        x = int(x/10)

    ret = sign*ret

    return ret

def ispalindrome(x):
    x = str(x)
    for i in range(len(x)):
        k = len(x)-i-1
        if x[i] != x[k]:
            return False

    return True

def longestcommonprefix(str_arr):
    len = 0
    for i in range(len(str_arr[0])):
        c = str_arr[0][i] 
        for s in str_arr[1:]:
            if s[i] != c:
                return len
        
#https://leetcode.com/problems/array-partition-i/description/
def array_partition1(arr):
    arr.sort()
    print "arr: " + str(arr)
    n = len(arr)/2
    pairs = [(arr[2*i], arr[2*i+1]) for i in range(n)]
    print "pairs: " + str(pairs)
    max_sum = sum([p[0] for p in pairs])
    print "max_sum: " + str(max_sum)
    return max_sum

#https://leetcode.com/problems/can-place-flowers/description/
def canplace_flowers(flowerbed,n):
    nf = len(flowerbed)
    if nf > 2:
        i = 2
        while (i < nf) and (n > 0):
            if (flowerbed[i]==0) and (flowerbed[i-1]==0) and (flowerbed[i-2]==0):
                flowerbed[i-1] = 1
                n -= 1
            i+=1    
        if n == 0:
            return True
        else:
            return False
    elif nf == 2:
        if (n <= 1) and (flowerbed[0] == 0) and (flowerbed[1] == 0):
            return True
        else:
            return False
    else:   #nf == 1
        if (n <= 1) and (flowerbed[0] == 0):
            return True
        else:
            return False

#https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
def kdiff_pairs(arr,k):
    h = {a:ix for ix,a in enumerate(arr)}

    print "h: " + str(h)
    pairs = []
    for ix,a in enumerate(arr):
        if a in h:
            p1 = a - k
            p2 = a + k

            #check pair possibility 1 and 2
            for p in [p1,p2]:
                if p in h:
                    pair = [a,p]
                    pair.sort()
                    pairs.append(pair)

    #remove duplicates
    unique_pairs = []
    for p in pairs:
        if not(p in unique_pairs):
            unique_pairs.append(p)

    print "pairs: " + str(unique_pairs)
    return len(unique_pairs)

#https://leetcode.com/problemset/all/?search=third%20max
def third_max(arr):
    m1 = m2 = m3 = None
    if len(arr) < 3:
        return max(arr)
    else:
        for a in arr:
            if m1 == None:
                m1 = a
            else:
                if a > m1:
                    m3 = m2
                    m2 = m1
                    m1 = a
                elif a > m2 and a < m1:
                    m3 = m2
                    m2 = a
                elif a > m3 and a < m2:
                    m3 = a
        return m3,m2,m1

#https://leetcode.com/problems/heaters/description/
def heaters(houses,heaters):
    closest_heater = []
    for h in houses:
        dist = min([abs(heater - h) for heater in heaters])
        closest_heater.append(dist)

    return max(closest_heater)

#https://leetcode.com/problems/arranging-coins/description/
def arrangecoins(n):
    high = n
    low = 0

    while 1:
        k = int(high + low)/2
        l = (k+1)*k/2 
        h = l+k+1

        if (n >= l) and (n < h):
            break
        elif n >= h:
            low = k
        else:
            high = k

    return k

def firstbadversion(vers):
    print "vers: " + str(vers)
    n = len(vers)
    low = 0
    high = n-1
    while low+1 < high:
        mid = int((low+high)/2)
        print "low: {} mid: {} high: {}".format(low,mid,high) 
        if vers[mid] == 1 and vers[low] == 0:
            high = mid
        elif vers[mid] == 0 and vers[high] == 1:
            low = mid
    return high

def twosum(arr,target):
    p1 = 0
    p2 = len(arr) - 1

    while arr[p1] + arr[p2] != target:
        if arr[p1] + arr[p2] > target:
            p2 -= 1
        elif arr[p1] + arr[p2] < target:
            p1 += 1

    return arr[p1], arr[p2]

#def perfectsquare(num):
#    l = 0
#    h = num
#    while (l+1 < h):
#        mid = 


def haspathsum(root,sum):
    d = {}

if __name__ == '__main__':
    #print "reverse(1234): " + str(reverse(-1234))
    #print "ispalindrome(111): " + str(ispalindrome(1114))

    #print "array_partition1([1,2,3,4]): " + str(array_partition1([4,3,2,1]))
    flowerbed = [1,0]
    n = 1
    #print "canplace_flowers: " + str(canplace_flowers(flowerbed,n))
    #print "kdiff_pairs: " + str(kdiff_pairs([1,3,1,5,4],2))
    #print "third_max: " + str(third_max([3,3,2,1]))

    #print "closest_heater: " + str(heaters([1,2,3,4],[1]))
    #print "arrangecoins: " + str(arrangecoins(50000))
    vers = [0]*5
    vers.extend([1]*10)
    print "firstbadversion: " + str(firstbadversion(vers))

    arr = [1,2,4,7]
    print "twosum: " + str(twosum(arr,11))
