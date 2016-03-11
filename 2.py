
def problem(N,M):
    
    s = []  
    if N%M == 0:
        k = N/M
        i = 1
        while i*k<= N:
            s.append([(i-1)*k+1, i*k])
            i+=1
    else:

        d = N%M
        
        k = (N-d)/M
        i = 1
        while i*k<= N-d:
            s.append([(i-1)*k+1, i*k])
            i+=1
        
    print s


N = input("Please input length of array: ")
M = input("Please input amount of parts: ")
problem(N, M)

"""
for i in range(M+1,20):
    problem(i,M)

"""
