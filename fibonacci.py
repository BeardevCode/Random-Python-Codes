def fibonacci(nb):
    n1 = 0
    n2 = 1
    print(n1)
    while n2 < nb:
        print(n2)
        tmp = n2
        n2 += n1
        n1 = tmp

fibonacci(10000)