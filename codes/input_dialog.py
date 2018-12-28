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

    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])

    # check if year is 2009 or larger
    if year < 2019:
        raise Exception('You sure about the year you put?')

    # According to leap_year output, set number of days in February
    if leap_year(year=year):
        print('you had a leap-year')
        if month == 2:
            if day > 28:
                raise Exception('Wrong day for February. This is a leap year.')

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            raise Exception('Wrong number of days for this month')

    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            raise Exception('Wrong number of days for this month')


def check_quantity(quantity):

    """
    Takes the parameter **quantity**, transforms it into float and rounds it to two decimals.
    :param quantity: quantity input
    :return: float with two decimals.
    """

    return round(float(quantity), 2)


# Sequence for common-input
date = input("Date [DD/MM/YYYY]: ")
check_date(date=date)
concept = input("Concept: ")
quantity_raw = input("Quantity: ")
quantity = check_quantity(quantity=quantity_raw)


