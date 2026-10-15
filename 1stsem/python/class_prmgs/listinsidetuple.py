n = int(input("How many accounts? "))

if n <= 0:
    print("Error: Number of accounts must be greater than zero")
else:
    all_accounts = []

    for i in range(n):
        print("\nEnter details of account", i + 1)
        account_no = input("Enter account number: ")
        name = input("Enter name: ")
        pan_no = input("Enter PAN number: ")
        dob = input("Enter date of birth (dd/mm/yyyy): ")
        email = input("Enter email: ")
        contact_no = input("Enter contact number: ")
        city = input("Enter city: ")
        current_balance = float(input("Enter current balance: "))

        bank_details = (account_no, name, pan_no, dob, [email, contact_no, city, current_balance])
        all_accounts.append(bank_details)

    choice = ""

    while choice != "5":
        print("\n----- Bank Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Show Accounts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1" or choice == "2" or choice == "3":
            account_no = input("Enter account number: ")

            index = -1
            for i in range(len(all_accounts)):
                if all_accounts[i][0] == account_no:
                    index = i

            if index == -1:
                print("Error: Account not found")

            elif choice == "1":
                print("Current balance:", all_accounts[index][4][3])
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Error: Deposit amount must be positive")
                else:
                    all_accounts[index][4][3] = all_accounts[index][4][3] + amount
                    print("Success: Deposited", amount, ". Current balance:", all_accounts[index][4][3])
                    print("Updated account:", all_accounts[index])

            elif choice == "2":
                print("Current balance:", all_accounts[index][4][3])
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive")
                elif amount > all_accounts[index][4][3]:
                    print("Error: Insufficient balance")
                else:
                    all_accounts[index][4][3] = all_accounts[index][4][3] - amount
                    print("Success: Withdrew", amount, ". Current balance:", all_accounts[index][4][3])
                    print("Updated account:", all_accounts[index])

            else:
                print("\n------ Account Details ------")
                print("Account No :", all_accounts[index][0])
                print("Name       :", all_accounts[index][1])
                print("PAN No     :", all_accounts[index][2])
                print("DOB        :", all_accounts[index][3])
                print("Email      :", all_accounts[index][4][0])
                print("Contact No :", all_accounts[index][4][1])
                print("City       :", all_accounts[index][4][2])
                print("Balance    :", all_accounts[index][4][3])

        elif choice == "4":
            print("\n===== All Accounts =====")
            print(all_accounts)

        elif choice == "5":
            print("Thank you for banking with us. Goodbye!")
        else:
            print("Error: Invalid choice. Please select 1-5.")
