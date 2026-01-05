import tkinter as tk

def get_input():
    user_input = input_field.get()
    print("User Input:", user_input)

root = tk.Tk()
root.title("Input Example")
root.geometry("300x200")

# Create an input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=20)

# Create a button to retrieve input
submit_button = tk.Button(root, text="Submit", command=get_input)
submit_button.pack(pady=10)

root.mainloop()