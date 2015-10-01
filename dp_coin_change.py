#Solving the coin change problem as described below
#Write a program that, given
# An amount N and types of infinite available coins M
# A list of M coins - C={C1,C2,C3,..,CM}
# Prints out how many different ways you can make
# change from the coins to STDOUT.

N, M = map(int, input().split())
change_vals = list(map(int, input().split()))

#stored subproblems array has 0th row and col at 0
#initial condition
N += 1
M += 1

table =[[0 for x in range(N)] for y in range(M)]

for i in range(1,M):
    for j in range(1,N):
        #previous found solutions
        table[i][j] = table[i-1][j]

        #can new item make change on its own
        if(j%change_vals[i-1]==0):
            table[i][j]+=1

        #check if the residual change is available
        #add the number of ways in which change for
        #T(n-wi) can be got
        remains = j - change_vals[i-1]
        while (remains>0):
            if(table[i-1][remains]):
                table[i][j] += table[i-1][remains]
            remains -= change_vals[i-1]

print (table[M-1][N-1])

