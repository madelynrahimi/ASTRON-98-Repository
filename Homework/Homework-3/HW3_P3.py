def check_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or (year%4 == 0 and year%100 == 0 and year%400 == 0):
        return True
    else:
        return False

print(check_leap_year(3012))
print(check_leap_year(1600))
print(check_leap_year(2013))