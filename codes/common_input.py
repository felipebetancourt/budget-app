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

    date_ok = True

    # date format checks
    if len(date) != 10 or date[2] != "/" or date[5] != "/":
        print('Something wrong with date format')
        date_ok = False

    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])

    # check if year is 2009 or larger
    if year < 2019:
        print('You sure about the year you put?')
        date_ok = False

    # According to leap_year output, set number of days in February
    if leap_year(year=year):
        print('you had a leap-year')
        if month == 2:
            if day > 29:
                print('Wrong day for February. This is a leap year.')
                date_ok = False
    elif month == 2:
        if day > 28:
            print('Wrong number of days for this month')
            date_ok = False

    if month in [int(x) for x in [1, 3, 5, 7, 8, 10, 12]]:
        if day < 1 or day > 31:
            print('Wrong number of days for this month')
            date_ok = False

    elif month in [int(x) for x in [4, 6, 9, 11]]:
        if day < 1 or day > 30:
            print('Wrong number of days for this month')
            date_ok = False

    return date_ok


def check_quantity(quantity):

    """
    Takes the parameter **quantity**, transforms it into float and rounds it to two decimals.
    :param quantity: quantity input
    :return: float with two decimals.
    """

    return round(float(quantity), 2)


def common_input():

    """
    Create function with sequence and checks for common_input
    :return: date, concept and quantity
    """

    date = input("Date [DD/MM/YYYY]: ")
    date_ok = check_date(date=date)

    # check if data format is right. Ask again if not.
    while not date_ok:
        date = input("Date [DD/MM/YYYY]: ")
        date_ok = check_date(date=date)

    concept = input("Concept: ")
    quantity_raw = input("Quantity: ")
    quantity = check_quantity(quantity=quantity_raw)

    return date, concept, quantity
