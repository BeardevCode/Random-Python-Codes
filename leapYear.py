def leap_year(year):
    if year % 400 is 0 or year % 4 is 0:
        print("%d is a leap year" % year)
        return True
    else:
        print("%d is not a leap year" % year)
        return False

# tests
leap_year(2000) # yes
leap_year(2001) # no
