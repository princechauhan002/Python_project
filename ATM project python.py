# ATM Project in Python
def read_balance():
    """Read balance from file with exception handling."""
    try:
        with open('balance.txt', 'r') as file:
            balance = float(file.read().strip())
            return balance
    except FileNotFoundError:
        # File doesn't exist, start with zero balance
        return 0.0
    except ValueError:
        # Invalid data in file, reset to zero
        print("Error reading balance file. Resetting to zero.")
        return 0.0
    except Exception as e:
        # General file error
        print(f"File error: {e}")
        return 0.0

def write_balance(amount):
    """Write balance to file with exception handling."""
    try:
        with open('balance.txt', 'w') as file:
            file.write(str(amount))
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def validate_pin():
    """Validate PIN with retry loop."""
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        pin = input("Enter your PIN: ").strip()
        if pin == "1234":  # Hardcoded PIN for simplicity
            print("PIN validated successfully.")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Invalid PIN. {remaining} attempts remaining.")
            else:
                print("Maximum attempts exceeded. Access denied.")
    return False

def check_balance():
    """Display current balance."""
    balance = read_balance()
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    """Handle deposit with exception handling."""
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        current_balance = read_balance()
        new_balance = current_balance + amount
        if write_balance(new_balance):
            print(f"Deposited ${amount:.2f} successfully.")
            print(f"New balance: ${new_balance:.2f}")
        else:
            print("Deposit failed due to file error.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def withdraw():
    """Handle withdrawal with exception handling."""
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        current_balance = read_balance()
        if amount > current_balance:
            print("Insufficient funds.")
            return
        new_balance = current_balance - amount
        if write_balance(new_balance):
            print(f"Withdrew ${amount:.2f} successfully.")
            print(f"New balance: ${new_balance:.2f}")
        else:
            print("Withdrawal failed due to file error.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_menu():
    """Display the ATM menu."""
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def main():
    """Main function to run the ATM system."""
    print("Welcome to the Simple ATM!")
    
    # Initial PIN validation
    if not validate_pin():
        print("Session ended due to invalid PIN.")
        return
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-4.")
        
        input("Press Enter to continue...")  # Pause for user

# Run the program
if __name__ == "__main__":
    main()
