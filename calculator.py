from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def get_user_input(message):
    while True:
        try:
            user_input = float(input(message))
            return user_input
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def main():
    print(Fore.GREEN + "Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = get_user_input("Enter first number: ")
            num2 = get_user_input("Enter second number: ")

            if choice == '1':
                print(Fore.BLUE + "Result:", add(num1, num2))
            elif choice == '2':
                print(Fore.BLUE + "Result:", subtract(num1, num2))
            elif choice == '3':
                print(Fore.BLUE + "Result:", multiply(num1, num2))
            elif choice == '4':
                print(Fore.BLUE + "Result:", divide(num1, num2))
        else:
            print(Fore.RED + "Invalid input. Please enter a valid choice (1/2/3/4).")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
