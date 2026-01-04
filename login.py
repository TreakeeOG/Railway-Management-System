# auth/login.py

import sys
sys.path.append("c:/Users/USER/Documents/Pytho/Railway-Management-system")
from db import get_connection
import tkinter as tk
from tkinter import messagebox


def login_user():
    root = tk.Tk()
    root.withdraw()

    try:
        con = get_connection()
        print("Database connection established.")
        cur = con.cursor()

        print("USER LOGIN")

        try:
            user_id = int(input("Enter User ID: "))
            password = input("Enter Password: ")

            cur.execute(
                "SELECT userID FROM User WHERE userID = %s AND password = %s",
                (user_id, password)
            )

            if cur.fetchone():
                print("Login Successful!")
                messagebox.showinfo("Success", "Login Successful!")
                return True
            else:
                print("Invalid User ID or Password")
                messagebox.showerror("Error", "Invalid User ID or Password")
                return False

        except ValueError:
            print("Invalid input! User ID must be numeric.")
            messagebox.showwarning("Warning", "Invalid input! User ID must be numeric.")
            return False

        except Exception as e:
            print(f"An error occurred during login: {e}")
            messagebox.showerror("Error", "An unexpected error occurred.")
            return False

    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        messagebox.showerror("Database Error", "Could not connect to the database.")
        return False

    finally:
        try:
            con.close()
            print("Database connection closed.")
        except:
            pass

# this is to show that i can push change to github
