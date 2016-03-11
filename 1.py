N = input("Please input a number: ")
s = []
s.append([])
s.append([2])
print s
for k in range(3, N+1):
    for i in range(2, k):
        if k%i == 0:
            s.append([])
            for item in s[i-1]:
                s[k-1].append(item)
            for item in s[k/i - 1]:
                s[k-1].append(item)
            break
    else:
        s.append([k])
for i in range(1,len(s)):
    print i+1, s[i]
