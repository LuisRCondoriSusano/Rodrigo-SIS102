def is_leap(year):
    if year%4==0:
        leap=True
        if year %400==0 and year %100==0:
            leap=True
    else:
        leap=False
    return leap           

year = int(input())
print(is_leap(year))