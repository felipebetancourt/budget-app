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

    date, concept, quantity = ci()

    return date, concept, quantity


def do_cash_in():

    """
    Dialog for cash in. Apart from common input it contains another field called "source". Here the source of the money
    is explained"
    :return: date, concept, quantity, source
    """

    date, concept, quantity = ci()

    print("Choose one of the soruces: parents, erasmus, bank, work, others \n")

    source = input("Source: ")

    while source not in ["parents", "erasmus", "bank", "work", "others"]:
        source = input("Source: ")

    return date, concept, quantity, source


def do_cash_out():

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

    return date, concept, quantity, sink


date, concept, quantity, sink = do_cash_out()