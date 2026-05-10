import argparse
import math


def incorrect():
    print("Incorrect parameters")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

values = [args.type, args.principal, args.payment, args.periods, args.interest]

if args.type not in ["annuity", "diff"]:
    incorrect()
elif args.interest is None:
    incorrect()
elif len([x for x in values if x is not None]) < 4:
    incorrect()
elif args.type == "diff" and args.payment is not None:
    incorrect()
elif args.principal is not None and args.principal < 0:
    incorrect()
elif args.payment is not None and args.payment < 0:
    incorrect()
elif args.periods is not None and args.periods < 0:
    incorrect()
elif args.interest is not None and args.interest < 0:
    incorrect()
else:
    i = args.interest / (12 * 100)

    if args.type == "diff":
        total_payment = 0

        for month in range(1, args.periods + 1):
            payment = math.ceil(
                args.principal / args.periods
                + i * (args.principal - args.principal * (month - 1) / args.periods)
            )
            total_payment += payment
            print(f"Month {month}: payment is {payment}")

        overpayment = int(total_payment - args.principal)
        print(f"Overpayment = {overpayment}")

    elif args.type == "annuity":
        if args.payment is None:
            payment = math.ceil(
                args.principal
                * (i * math.pow(1 + i, args.periods))
                / (math.pow(1 + i, args.periods) - 1)
            )

            overpayment = int(payment * args.periods - args.principal)

            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {overpayment}")

        elif args.principal is None:
            principal = math.floor(
                args.payment
                / (
                    (i * math.pow(1 + i, args.periods))
                    / (math.pow(1 + i, args.periods) - 1)
                )
            )

            overpayment = int(args.payment * args.periods - principal)

            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {overpayment}")

        elif args.periods is None:
            periods = math.ceil(
                math.log(args.payment / (args.payment - i * args.principal), 1 + i)
            )

            years = periods // 12
            months = periods % 12

            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")

            overpayment = int(args.payment * periods - args.principal)
            print(f"Overpayment = {overpayment}")