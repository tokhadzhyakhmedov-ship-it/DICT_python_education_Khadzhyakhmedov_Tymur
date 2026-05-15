import argparse
import math


def incorrect():
    print("Incorrect parameters")


def check_args(args):
    values = [args.type, args.principal, args.payment, args.periods, args.interest]

    if args.type not in ["annuity", "diff"]:
        return False
    if args.interest is None:
        return False
    if len([x for x in values if x is not None]) < 4:
        return False
    if args.type == "diff" and args.payment is not None:
        return False

    numbers = [args.principal, args.payment, args.periods, args.interest]
    for number in numbers:
        if number is not None and number < 0:
            return False

    return True


def calculate_diff(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0

    for month in range(1, periods + 1):
        payment = math.ceil(
            principal / periods
            + i * (principal - principal * (month - 1) / periods)
        )
        total_payment += payment
        print(f"Month {month}: payment is {payment}")

    overpayment = int(total_payment - principal)
    print(f"Overpayment = {overpayment}")


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)

    payment = math.ceil(
        principal
        * (i * math.pow(1 + i, periods))
        / (math.pow(1 + i, periods) - 1)
    )

    overpayment = int(payment * periods - principal)

    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {overpayment}")


def calculate_principal(payment, periods, interest):
    i = interest / (12 * 100)

    principal = math.floor(
        payment
        / (
            (i * math.pow(1 + i, periods))
            / (math.pow(1 + i, periods) - 1)
        )
    )

    overpayment = int(payment * periods - principal)

    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")


def calculate_periods(principal, payment, interest):
    i = interest / (12 * 100)

    periods = math.ceil(
        math.log(payment / (payment - i * principal), 1 + i)
    )

    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = int(payment * periods - principal)
    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if not check_args(args):
    incorrect()
else:
    if args.type == "diff":
        calculate_diff(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        if args.payment is None:
            calculate_annuity_payment(args.principal, args.periods, args.interest)

        elif args.principal is None:
            calculate_principal(args.payment, args.periods, args.interest)

        elif args.periods is None:
            calculate_periods(args.principal, args.payment, args.interest)