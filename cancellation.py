import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def cancel_ticket():
    pnr = input("Enter the PNR number of the ticket to cancel: ")
    con = get_connection()
    cur = con.cursor()

    try:
        # Check if the ticket exists in the booking table
        cur.execute("SELECT * FROM Booking WHERE PNR_No = %s", (pnr,))
        ticket = cur.fetchone()

        if not ticket:
            print("No ticket found with the given PNR.")
            return

        refund_amount = ticket[5] * 0.8 
        print(refund_amount)
        
        cancellation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(cancellation_date)

        # Debugging: Print values before inserting into Cancellation table
        print(f"PNR: {pnr}, Cancellation Date: {cancellation_date}, Refund Amount: {refund_amount}")

        # Add cancellation details to the Cancellation table
        cur.execute(
            "INSERT INTO Cancellation (PNR_No, Cancellation_Date, Refund_Amount) VALUES (%s, %s, %s)",
            (pnr, cancellation_date, refund_amount),
        )

        # Delete the ticket from the Booking table
        cur.execute("DELETE FROM Booking WHERE PNR_No = %s", (pnr,))

        # Commit the changes
        con.commit()
        print("Ticket cancelled successfully.")

    except Exception as e:
        print("An error occurred:", e)
        con.rollback()

    finally:
        con.close()


def view_cancellaition():
    root = tk.Tk()
    root.withdraw()

    con = get_connection()
    cur = con.cursor()

    print("BOOK TICKET")
    cur.execute("SELECT * FROM Cancellation")
    records = cur.fetchall()

    if not records:
        print("No booking records found.")
        messagebox.showerror("Error","No booking records found")
    else:
        print("\nPNR | Cancellation Date | Refund amount")
        print("-" * 70)
        for row in records:
            print(f"{row[0]:4} | {row[1]} | {row[2]}")

    input("\nPress Enter to continue...")
    con.close()
