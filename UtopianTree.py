#Solving by DP
#T(0) = 1
#T(n) = T(n-1)+1 if n is even (summer)
#T(n) = 2*T(n-1) if n is odd (spring)
def utopianTree(n):
    treeSize = []
    treeSize.append(1)

    if (n==0):
        return treeSize[0]

    for x in range(1,n+1):
        if ((x%2) == 1):
            treeSize.append(2*treeSize[x-1])
        else:
            treeSize.append(treeSize[x-1]+1)

    return treeSize[n]

num_test_cases = int(input())
results=[]
for test in range(num_test_cases):
    inputDuration = int(input())
    results.append(utopianTree(inputDuration))

for ans in range(num_test_cases):
    print(results[ans])