import sys
import stdio

year = int (sys.argv [1])

isLeapYear = ((year % 400) == 0) or ((year % 4) == 0 and (year % 100) != 0)

print (year, " is ", isLeapYear)

help (sys)