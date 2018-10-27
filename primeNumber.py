def prime_number(nb):
    if nb is 1:
        print("%d is not a prime number" % nb)
        return False
    for i in range(2, nb):
        if nb % i is 0:
            print("%d is not a prime number" % nb)
            return False
    print("%d is a prime number" % nb)
    return True

# tests
print(prime_number(1)) # no
print(prime_number(5)) # yes
print(prime_number(6)) # no
print(prime_number(11)) # yes
print(prime_number(888)) # no