from common_input import common_input as ci


def transaction_type():

    """
    Print instructions for input-dialog and save the input form user.
    :return: CASH_OUT, CASH_IN or SAVING depending on the transaction that the user wants to perform.
    """

    print("Welcome to your input-dialog \n")
    print("----------------------------\n")
    print("What kind of operation do you wan to perform? \n")
    print("[1] Cash out \n")
    print("[2] Cash in \n")
    print("[3] Savings \n")

    user_input = int(input("Select 1, 2 or 3 : "))

    while user_input not in [int(x) for x in [1, 2, 3]]:

        user_input = int(input("Select 1, 2 or 3 : "))

    if user_input == 1:
        answer = "CASH_OUT"
    elif user_input == 2:
        answer = "CASH_IN"
    elif user_input == 3:
        answer = "SAVING"
    else:
        raise Exception("Error in transaction_type(). Invalid user_input.")

    return answer


def do_savings():

    """
    Dialog for savings. It only contains the common-input.
    :return: date, concept, quantity
    """

    print("Enter some saving statement: \n")

    date, concept, quantity = ci()

    return date, concept, quantity


def do_cash_in():

    """
    Dialog for cash in. Apart from common input it contains another field called "source". Here the source of the money
    is explained"
    :return: date, concept, quantity, source
    """

    print("Enter some cash-in statement: \n")

    date, concept, quantity = ci()

    print("Choose one of the sources: parents, erasmus, bank, work, others \n")

    source = input("Source: ")

    while source not in ["parents",
                         "erasmus",
                         "bank",
                         "work",
                         "others"]:

        source = input("Source: ")

    return date, concept, quantity, source


def do_cash_out():

    """
    Dialog for cash-out. Apart from the common input it contains other two fields: "sink" to specify which kind of
    expense it was and "payment_mean" to specify how the payment was made.
    :return: date, concept, quantity, sink, payment_mean
    """

    print("Enter some cash-out statement: ")

    date, concept, quantity = ci()

    print("Choose one of the sinks: \n")
    print("entertainment, groceries, social, travel, treats, needs, phone, sport, transportation \n")

    sink = input("Sink: ")

    while sink not in ["entertainment",
                       "groceries",
                       "social",
                       "travel",
                       "treats",
                       "needs",
                       "phone",
                       "sport",
                       "transportation"]:

        sink = input("Sink: ")

    payment_mean = input("Payment mean: ")

    while payment_mean not in ["cash", "debit", "credit"]:

        payment_mean = input("Payment mean: ")

    return date, concept, quantity, sink, payment_mean


def input_dialog(input_type):

    """
    According to the transaction type, ask for some inputs and return them.
    Raise an error in case of wrong transaction type.
    """

    if input_type == "CASH_OUT":

        date, concept, quantity, sink, payment_mean = do_cash_out()

        return date, concept, quantity, sink, payment_mean

    elif input_type == "CASH_IN":

        date, concept, quantity, source = do_cash_in()

        return date, concept, quantity, source

    elif input_type == "SAVING":

        date, concept, quantity = do_savings()

        return date, concept, quantity

    else:
        raise Exception("Error in input_dialog(). invalid transaction type.")


input_type = transaction_type()

if input_type == "CASH_OUT":

    date, concept, quantity, sink, payment_mean = input_dialog(input_type=input_type)

elif input_type == "CASH_IN":

    date, concept, quantity, source = input_dialog(input_type=input_type)

elif input_type == "SAVING":

    date, concept, quantity = input_dialog(input_type=input_type)

else:

    raise Exception("Error in transaction type.")