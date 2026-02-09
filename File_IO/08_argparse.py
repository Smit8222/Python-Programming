import argparse

parser = argparse.ArgumentParser(description="A simple argument parser example.")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("--operation", choices=["add", "subtract", "multiply", "divide"],
                    help="Operation to perform")


args = parser.parse_args()
print(args)

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Error: Division by zero"
else:
    result = "No operation specified"
print(f"Result: {result}")





                    