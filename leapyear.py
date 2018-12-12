def main ():

  year = int (input ("please enter a year? "))

  while year >= 0:

    if isLeapYear (year):
      print (year, "is a leap year")
    else:
      print (year, "is not a leap year")

    year = int (input ("please enter a year? "))


def isLeapYear (year):
  return ((year % 400) == 0) or ((year % 4) == 0 and (year % 100) != 0)


if __name__ == "__main__":
    main ()
