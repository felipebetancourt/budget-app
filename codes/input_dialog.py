from common_input import common_input as ci


def transaction_type():

    print("Welcome to your input-dialog \n")
    print("----------------------------\n")
    print("What kind of operation do you wan to perform? \n")
    print("[1] Cash out \n")
    print("[2] Cash in \n")
    print("[3] Savings \n")

    answer = int(input("Select 1, 2 or 3 : "))

    print(type(answer))

    while answer not in [int(x) for x in [1, 2, 3]]:
        answer = int(input("Select 1, 2 or 3 : "))

    return answer


def do_savings():

    date, concept, quantity = ci()

    return date, concept, quantity


def do_cash_in():

    date, concept, quantity = ci()

    print("Choose one of the soruces: parents, erasmus, bank, work, others \n")

    source = input("Source: ")

    while source not in ["parents", "erasmus", "bank", "work", "others"]:
        source = input("Source: ")

    return date, concept, quantity, source
