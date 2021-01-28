def dispalyPattern(n):
    for i in range(n):
        for j in range(i+1):
            if j <= i:
                print(j+1,end=" ")
            else:
                print(end=" ")
        print()
dispalyPattern(5)