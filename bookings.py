import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection

import tkinter as tk
from tkinter import messagebox


def book_ticket():
    root = tk.Tk()
    root.withdraw()

    con = get_connection()
    cur = con.cursor()

    print("BOOK TICKET")

    try:
        pnr = int(input("Enter PNR Number: "))
        train_id = input("Enter Train ID (leave blank if not available): ")
        passenger_id = input("Enter Passenger ID (leave blank if not available): ")
        booking_date = input("Enter Booking Date (YYYY-MM-DD): ")
        departure_date = input("Enter Departure Date (YYYY-MM-DD): ")
        fare = input("Enter Fare (leave blank if not available): ")

        train_id = int(train_id) if train_id else None
        passenger_id = int(passenger_id) if passenger_id else None
        fare = int(fare) if fare else None

        cur.execute(
            """
            INSERT INTO Booking
            (PNR_No, TrainID, PassengerID, Booking_Date, Departure_Date, Fare)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (pnr, train_id, passenger_id, booking_date, departure_date, fare)
        )

        con.commit()
        print("Ticket Booked Successfully")

    except Exception as e:
        print(f"Error {e}")

    finally:
        input("Press Enter to continue...")
        con.close()

def view_bookings():
    root = tk.Tk()
    root.withdraw()

    con = get_connection()
    cur = con.cursor()

    print("BOOKING DETAILS")

    cur.execute("SELECT * FROM Booking")
    records = cur.fetchall()

    if not records:
        print("No booking records found.")
        messagebox.showerror("Error","No booking records found")
    else:
        print("\nPNR | TrainID | PassengerID | Book Date | Depart Date | Fare")
        print("-" * 70)
        for row in records:
            print(f"{row[0]:4} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")

    input("\nPress Enter to continue...")
    con.close()

def cancel_ticket():
    con = get_connection()
    cur = con.cursor()

    print("CANCEL TICKET")

    try:
        pnr = int(input("Enter PNR Number: "))
        cancel_date = input("Enter Cancellation Date (YYYY-MM-DD): ")
        refund = input("Enter Refund Amount (leave blank if none): ")

        refund = int(refund) if refund else None

        # Check if booking exists
        cur.execute(
            "SELECT Fare FROM Booking WHERE PNR_No = %s",
            (pnr,)
        )
        record = cur.fetchone()

        if not record:
            print("Booking Not Found")
            messagebox.showerror("Error", "Booking Not Found")
            input("Press Enter to continue...")
            return

        # Insert into Cancellation table
        cur.execute(
            """
            INSERT INTO Cancellation
            (PNR_No, Cancellation_Date, Refund_Amount)
            VALUES (%s, %s, %s)
            """,
            (pnr, cancel_date, refund)
        )

        # Delete from Booking table
        cur.execute(
            "DELETE FROM Booking WHERE PNR_No = %s",
            (pnr,)
        )

        con.commit()
        print("Ticket Cancelled Successfully")
        messagebox.showinfo("Success", "Ticket Cancelled Successfully")

    except Exception as e:
        print("Error during cancellation")
        messagebox.showerror("Error", f"Error during cancellation: {e}")

    finally:
        input("Press Enter to continue...")
        con.close()

book_ticket()