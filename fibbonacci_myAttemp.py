def fibb(n):
    num = [0,1]
    if n>=2:
        for i in range(2,n):
            number = num[i-1] + num[i-2]
            num.append(number)
        return num[-1]
    else:
        if n==1:
            return 1
        else:
            return 0

print(fibb(9))
    