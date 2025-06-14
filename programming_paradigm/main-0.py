import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance
    
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Avoid issues from space after colon
    if ' ' in sys.argv[1]:
        print("❌ Error: Remove spaces. Use deposit:50 not deposit: 50")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')

    try:
        amount = float(params[0]) if params and params[0] != '' else None
    except ValueError:
        print("Invalid amount. Example: deposit:100")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"✅ Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"✅ Withdrew: ${amount}")
        else:
            print("❌ Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("❌ Invalid command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()

