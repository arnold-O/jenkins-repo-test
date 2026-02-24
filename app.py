import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Jenkins Parameterization Practice Script")

    parser.add_argument("--name", type=str, default="User", help="Name of the user")
    parser.add_argument("--environment", type=str, choices=["dev", "test", "prod"], default="dev", help="Environment")
    parser.add_argument("--operation", type=str, choices=["add", "multiply"], help="Math operation")
    parser.add_argument("--num1", type=int, help="First number")
    parser.add_argument("--num2", type=int, help="Second number")

    args = parser.parse_args()

    print(f"\nHello, {args.name}!")
    print(f"Running in {args.environment.upper()} environment")
    print(f"Build time: {datetime.now()}")

    if args.operation and args.num1 is not None and args.num2 is not None:
        if args.operation == "add":
            result = args.num1 + args.num2
        elif args.operation == "multiply":
            result = args.num1 * args.num2

        print(f"Result of {args.operation}: {result}")
    else:
        print("No math operation performed.")

if __name__ == "__main__":
    main()