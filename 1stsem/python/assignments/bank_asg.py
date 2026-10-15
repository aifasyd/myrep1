balance = 0
choice = ""

while choice != "4":
    print("\n----- Bank Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Error: Deposit amount must be positive")
        else:
            balance = balance + amount
            print("Success: Deposited", amount, ". New balance:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
        elif amount > balance:
            print("Error: Insufficient balance")
        else:
            balance = balance - amount
            print("Success: Withdrew", amount, ". New balance:", balance)
    elif choice == "3":
        print("Current Balance:", balance)
    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
    else:
        print("Error: Invalid choice. Please select 1-4.")