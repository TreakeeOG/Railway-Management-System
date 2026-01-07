# RAILWAY ADMIN CLI
from train import *
from passengers import *
from bookings import * 
from cancellation import *    
import getpass

print("=" * 40)
print(" RAILWAY MANAGEMENT SYSTEM ")
print("        ADMIN CLI")
print("=" * 40)


# SIMPLE AUTHENTICATION

while True:
    password = getpass.getpass("Enter admin password: ")
    if password == "admin123":
        print("Access granted...")
        break
    else:
        print("Access denied...")


print("Type 'help' to see commands\n")



# CLI LOOP

while True:
    command = input("RMS> ").strip().lower()

    # Accept both numbers and keyword commands at the main prompt
    if command in ("help", "?"):
        print("""
Available Commands:
-------------------
Trains              - 1 or trains
Passengers          - 2 or passengers
Cancellation        - 3 or cancellation
Bookings            - 4 or bookings
Exit                - exit or quit
Clear Screen        - clear or cls
""")

    elif command in ("1", "trains", "train"):
        print("redirecting to train details...")

        print("""
Available Commands:
-------------------
Add trains          - 1 or add
Update trains       - 2 or update
Delete trains       - 3 or delete
View trains         - 4 or view
back                - back
""")
        choice = input("RMS Trains> ").strip().lower()
        if choice in ("1", "add", "add trains"):
            print("Adding train...")
            add_train()
        elif choice in ("2", "update", "update trains"):
            print("Updating train...")
            update_train()
        elif choice in ("3", "delete", "delete trains"):
            print("Deleting train...")
            delete_train()
        elif choice in ("4", "view", "view trains"):
            print("Fetching train details...")
            view_trains()
        elif choice == "back":
            continue
        else:
            print("Unknown command. Type 'back' to return")

        
    elif command in ("2", "passengers", "passenger"):
        print("redirecting to passenger details...")
        print("""
Available Commands:
-------------------
Add passengers      - 1 or add
View passengers     - 2 or view
back                - back
""")
        choice = input("RMS Passengers> ").strip().lower()
        if choice in ("1", "add", "add passengers"):
            print("Adding passenger...")
            add_passenger()
        elif choice in ("2", "view", "view passengers"):
            print("Fetching passenger details...")
            view_passengers()
        elif choice == "back":
            continue
        else:
            print("Unknown command. Type 'back' to return")


    elif command in ("3", "cancellation", "cancel", "cancilation"):
        print("redirecting to cancellation details...")
        print("""
Available Commands:
-------------------
View cancellations  - 1 or view
cancel ticket       - 2 or cancel
back                - back
""")
        choice = input("RMS Cancellation> ").strip().lower()
        if choice in ("1", "view", "view cancellations"):
            print("Fetching cancellation details...")
            view_cancellaition()
        elif choice in ("2", "cancel", "cancel ticket"):
            print("Cancelling ticket...")
            cancel_ticket()
        elif choice == "back":
            continue
        else:
            print("Unknown command. Type 'back' to return")
  
    elif command in ("4", "bookings", "booking", "book", "book ticket"):
        print("redirecting to booking details...")
        print("""
Available Commands:
-------------------
Book ticket         - 1 or book
View bookings       - 2 or view
back                - back
""")
        choice = input("RMS Bookings> ").strip().lower()
        if choice in ("1", "book", "book ticket"):
            print("Adding booking...")
            book_ticket()
        elif choice in ("2", "view", "view bookings"):
            print("Fetching booking details...")
            view_bookings()
        elif choice == "back":
            continue
        else:
            print("Unknown command. Type 'back' to return")

    elif command in ("clear", "cls", "clear screen"):
        import os
        os.system("cls")

    elif command in ("exit", "quit"):
        print("Exiting CLI")
        break

    else:
        print("Unknown command. Type 'help'")
