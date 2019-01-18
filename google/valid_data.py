# google interview from 1o24
# given a list of three int, decide if they can form a valid data in year, month, day
import sys
def valid_date(nums):
    # three intervals, year: 0-any, date: 1-31, month: 1-12
    y,d,m = 0,0,0

    for num in nums:
        if num>=32 or num == 0:
            y += 1
        elif 13<=num:
            d += 1
        elif 1<=num<=12:
            m += 1
    if y>1 or d>2:
       return False
    return True

nums = map(int,sys.argv[1:])
print valid_date(nums)
