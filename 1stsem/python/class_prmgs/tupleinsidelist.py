n = int(input("How many accounts? "))

if n <= 0:
    print("Error: Number of accounts must be greater than zero")
else:
    account_list = []

    for i in range(n):

        print("\nEnter details of account", i + 1)
        name = input("Enter name: ")
        account_no = input("Enter account number: ")
        pan = input("Enter PAN number: ")
        dob = input("Enter date of birth (dd/mm/yyyy): ")
        email = input("Enter email: ")

        balance = 0.0

        account = (name, account_no, pan, dob, email, balance)
        account_list.append(account)

    choice = ""

    while choice != "4":
        print("\n----- Bank Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1" or choice == "2" or choice == "3":
            account_no = input("Enter account number: ")

            # search for the account
            index = -1
            for i in range(len(account_list)):
                if account_list[i][1] == account_no:
                    index = i

            if index == -1:
                print("Error: Account not found")

            elif choice == "1":
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Error: Deposit amount must be positive")
                    
                else:
                    acc = account_list[index]
                    new_balance = acc[5] + amount

                    # tuples can't be changed, so make a new tuple

                    account_list[index] = (acc[0], acc[1], acc[2], acc[3], acc[4], new_balance)
                    print("Success: Deposited", amount, ". Current balance:", new_balance)

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                acc = account_list[index]
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive")
                elif amount > acc[5]:
                    print("Error: Insufficient balance")
                else:
                    new_balance = acc[5] - amount
                    account_list[index] = (acc[0], acc[1], acc[2], acc[3], acc[4], new_balance)
                    print("Success: Withdrew", amount, ". Current balance:", new_balance)

            else:
                acc = account_list[index]
                print("\n------ Account Details ------")
                print("Name       :", acc[0])
                print("Account No :", acc[1])
                print("PAN        :", acc[2])
                print("DOB        :", acc[3])
                print("Email      :", acc[4])
                print("Balance    :", acc[5])

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
        else:
            print("Error: Invalid choice. Please select 1-4.")