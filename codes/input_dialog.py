def leap_year(year):

    """
    Function to see if a year is a leap year or not.

    :param year: year to be tested
    :return: boolean True if year is leap year / False if year is not a leap year.
    """

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        answer = True
    else:
        answer = False

    return answer



