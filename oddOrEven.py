def odd_or_even(nb):
    if nb % 2 is 0:
        print("%d is Even" % nb)
    else:
        print("%d is Odd" % nb)

# tests
odd_or_even(2) # even
odd_or_even(3) # odd
odd_or_even(17) # odd
odd_or_even(120) # even