from common_input import common_input as ci


def transaction_type():

    """
    Print instructions for input-dialog and save the input form user.
    :return: 1, 2 or 3 depending on the transaction that the user wants to perform.
    """

    print("Welcome to your input-dialog \n")
    print("----------------------------\n")
    print("What kind of operation do you wan to perform? \n")
    print("[1] Cash out \n")
    print("[2] Cash in \n")
    print("[3] Savings \n")

    answer = int(input("Select 1, 2 or 3 : "))

    while answer not in [int(x) for x in [1, 2, 3]]:
        answer = int(input("Select 1, 2 or 3 : "))

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

        sink = input("Source: ")

    payment_mean = input("Payment mean: ")

    while payment_mean not in ["cash", "debit", "credit"]:

        payment_mean = input("Payment mean: ")

    return date, concept, quantity, sink, payment_mean

