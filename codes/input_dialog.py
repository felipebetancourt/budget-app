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


def check_date(date):

    """
    Check for date formats and that all days, months and years given are coherent.
    :param date: string of the form "DD/MM/YYYY"
    :return:
    """

    # date format checks
    if len(date) != 10 or date[2] != "/" or date[5] != "/":

        raise Exception('Something wrong with date format')

    day = int(date[0:1])
    month = int(date[3:4])
    year = int(date[6:9])

    # check if months and days are alright





check_date(date="321261")