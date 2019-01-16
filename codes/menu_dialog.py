from input_dialog import *
from time import time, gmtime, strftime


# TODO: write this function
def see_summary():

    """
    See current balances
    """

    print("Your balances")


# TODO : write this function
def see_operations_month():

    """
    See operations of the month...
    :return:
    """

    print("Operations of month...")


def goto_input_dialog(input_type):

    """

    :param input_type: type of input. "CASH_OUT", "CASH_IN" or "SAVING".
    :return: Will depend on the type of input.
    """

    if input_type == "CASH_OUT":

        date, concept, quantity, sink, payment_mean = input_dialog(input_type=input_type)

        return date, concept, quantity, sink, payment_mean

    elif input_type == "CASH_IN":

        date, concept, quantity, source = input_dialog(input_type=input_type)

        return date, concept, quantity, source

    elif input_type == "SAVING":

        date, concept, quantity = input_dialog(input_type=input_type)

        return date, concept, quantity

    else:

        raise Exception("Error in transaction type.")


def menu_dialog():

    """
    Display menu-dialog.
    :return:
    """

    print("Welcome to your Budge-App. \n")
    print("---------------------------- \n")

    print("What do you want to do? \n")
    print("[1] See summary \n")
    print("[2] See operations month \n")
    print("[3] Go to input-dialog \n")

    menu_choice = int(input("Select 1, 2 or 3 : "))

    while menu_choice not in [int(x) for x in [1, 2, 3]]:

        menu_choice = int(input("Select 1, 2 or 3 : "))

    if menu_choice == 1:

        see_summary()

    elif menu_choice == 2:

        see_operations_month()

    elif menu_choice == 3:

        goto_input_dialog(input_type=transaction_type())

    else:

        raise Exception("Error in menu_dialog(). Invalid menu choice. ")


def generate_id(old_id):

    """
    Takes the last recognized ID and generates a new one by checking at three things:
    - If the month is the same, just add one more value
    - If the month has changed, set counter to zero and add one month.
    - If year has changed, set month to 01, counter to 0 and add one more year.
    :param old_id: las ID item
    :return: new generated ID
    """

    year = old_id[0:2]
    month = old_id[2:4]
    counter = int(old_id[-2:])

    # Current date and time
    now = gmtime()

    if not (year == strftime("%y", now)):

        year_new = strftime("%y", now)
        month_new = "01"
        counter_new = "00"

    if not (month == strftime("%m", now)):

        year_new = year
        month_new = strftime("%m", now)
        counter_new = "00"

    if month == strftime("%m", now):

        year_new = year
        month_new = month

        # Make sure that the number of digits is conserved
        if (counter + 1) < 10:
            counter_new = "0" + str(counter+1)
        else:
            counter_new = str(counter+1)

    return year_new + month_new + counter_new

