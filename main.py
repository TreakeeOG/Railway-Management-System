import tkinter as tk
from auth.register import register_user
from auth.login import login_user
from printer import *
from db import create_RMS
from tables import create_all_tables
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Railway management system")
        self.geometry("390x844")
        self.resizable(False,False)
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for Page in (WelcomePage, RegisterPage, LoginPage, DashboardPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, page):
        self.frames[page].tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        create_all_tables()


        self.canvas = tk.Canvas(self, width=390, height=844)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = tk.PhotoImage(file="assets/Welcome/bg.png")
        self.register_img = tk.PhotoImage(file="assets/Welcome/btn_register.png")
        self.login_img = tk.PhotoImage(file="assets/Welcome/btn_login.png")
        self.hero_img = tk.PhotoImage(file="assets/Welcome/Hero.png")

        self.canvas.create_image(195, 422, image=self.bg_image)
        self.canvas.create_image(205, 535, image=self.hero_img)
        
        # Register button (image only)
        reg_id = self.canvas.create_image(140, 730, image=self.register_img)
        self.canvas.tag_bind(reg_id, "<Button-1>", lambda event: controller.show_frame(RegisterPage))

        # Login button (image only)
        log_id = self.canvas.create_image(320, 730, image=self.login_img)
        self.canvas.tag_bind(log_id, "<Button-1>",  lambda event:  controller.show_frame(LoginPage))

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Store the controller instance

        self.canvas = tk.Canvas(self, width=390, height=844)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = tk.PhotoImage(file="assets/register/bg.png")
        self.register_img = tk.PhotoImage(file="assets/register/register_btn.png")
        self.hero_img = tk.PhotoImage(file="assets/register/Hero.png")
        self.back_img = tk.PhotoImage(file="assets/register/back_btn.png")
        self.ticket_img = tk.PhotoImage(file="assets/register/ticket.png")

        self.canvas.create_image(195, 422, image=self.bg_image)
        self.canvas.create_image(210, 63, image=self.hero_img)
        self.canvas.create_image(195, 500, image=self.ticket_img)

        # Adding input fields
        self.username_entry = tk.Entry(self, font=("Kumbh Sans", 12), fg="black", bg="#CFC5B9", relief="flat")
        self.username_entry.place(x=60, y=335, width=200, height=30)

        self.password_entry = tk.Entry(self, font=("Arial", 12), fg="black", bg="#CFC5B9", relief="flat", show="*")
        self.password_entry.place(x=60, y=415, width=200, height=30)

        self.password_reentry = tk.Entry(self, font=("Arial", 12), fg="black", bg="#CFC5B9", relief="flat")
        self.password_reentry.place(x=60, y=495, width=200, height=30)

        # Register button (image only)
        reg_id = self.canvas.create_image(195, 590, image=self.register_img)
        self.canvas.tag_bind(reg_id, "<Button-1>", self.open_register)

        # Back button (image only)
        back_id = self.canvas.create_image(40, 63, image=self.back_img)
        self.canvas.tag_bind(back_id, "<Button-1>", lambda event: controller.show_frame(WelcomePage))

    def open_register(self, event=None):
        while True:
            user_id = self.username_entry.get()
            password = self.password_entry.get()
            reentered_password = self.password_reentry.get()

            if password != reentered_password:
                tk.messagebox.showwarning("Error", "Passwords do not match!")
                return

            if not user_id.isdigit():
                tk.messagebox.showwarning("Error", "User ID must be a number!")
                return

            try:
                register_user(int(user_id), password)
                tk.messagebox.showinfo("Redirecting", "Registration Successful! Redirecting to Login Page.")
                break
            except Exception as e:
                tk.messagebox.showwarning("Error", f"Registration failed: {e}. Please try again.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.password_reentry.delete(0, tk.END)
        self.controller.show_frame(LoginPage)  # Navigate to LoginPage

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Store the controller instance

        self.canvas = tk.Canvas(self, width=390, height=844)
        self.canvas.pack(fill="both", expand=True)

        # Load images
        self.bg_image = tk.PhotoImage(file="assets/login/bg.png")
        self.login_img = tk.PhotoImage(file="assets/login/login_btn.png")
        self.hero_img = tk.PhotoImage(file="assets/login/Hero.png")
        self.back_img = tk.PhotoImage(file="assets/login/back_btn.png")
        self.ticket_img = tk.PhotoImage(file="assets/login/ticket.png")

        # Add images to canvas
        self.canvas.create_image(195, 422, image=self.bg_image)
        self.canvas.create_image(230, 83, image=self.hero_img)
        self.canvas.create_image(195, 500, image=self.ticket_img)

        # Adding input fields
        self.username_entry = tk.Entry(self, font=("Kumbh Sans", 12), fg="black", bg="#ED683D", relief="flat")
        self.username_entry.place(x=60, y=360, width=200, height=30)

        self.password_entry = tk.Entry(self, font=("Arial", 12), fg="black", bg="#ED683D", relief="flat", show="*")
        self.password_entry.place(x=60, y=445, width=200, height=30)

        # Buttons
        reg_id = self.canvas.create_image(195, 550, image=self.login_img)
        self.canvas.tag_bind(reg_id, "<Button-1>", self.open_login)

        back_id = self.canvas.create_image(40, 70, image=self.back_img)
        self.canvas.tag_bind(back_id, "<Button-1>", self.back)

    def open_login(self, event=None):
        while True:
            user_id = self.username_entry.get()
            password = self.password_entry.get()

            if not user_id.isdigit():
                tk.messagebox.showwarning("Error", "User ID must be a number!")
                return

            if login_user(int(user_id), password):
                tk.messagebox.showinfo("redirecting", "Login Successful! Redirecting to Dashboard.")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.controller.show_frame(DashboardPage)  # Navigate to DashboardPage
                break
            else:
                tk.messagebox.showerror("Error", "Invalid credentials. Please try again.")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)

    def back(self, event=None):
        print("Back to Welcome")
        self.controller.show_frame(WelcomePage)  # Use self.controller to navigate

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, width=390, height=844)
        self.canvas.pack(fill="both", expand=True)

        # Load images
        self.bg_image = tk.PhotoImage(file="assets/dash/bg.png")
        self.access_img = tk.PhotoImage(file="assets/dash/access_btn.png")
        self.hero_img = tk.PhotoImage(file="assets/dash/Hero.png")
        self.button1_img = tk.PhotoImage(file="assets/dash/1_btn.png")
        self.button2_img = tk.PhotoImage(file="assets/dash/2_btn.png")
        self.button3_img = tk.PhotoImage(file="assets/dash/3_btn.png")
        self.cross_img = tk.PhotoImage(file="assets/dash/cross_btn.png")
        self.ticket_img = tk.PhotoImage(file="assets/dash/ticket.png")
        self.acc_img = tk.PhotoImage(file="assets/dash/acc.png")

        # Add images to canvas
        self.canvas.create_image(195, 422, image=self.bg_image)
        self.canvas.create_image(155, 150, image=self.hero_img)
        self.canvas.create_image(195, 450, image=self.ticket_img)
        self.canvas.create_image(100, 60, image=self.acc_img)

        # Buttons
        access_id = self.canvas.create_image(195, 700, image=self.access_img)
        self.canvas.tag_bind(access_id, "<Button-1>", self.open_cli)

        cross_id = self.canvas.create_image(65, 697, image=self.cross_img)
        self.canvas.tag_bind(cross_id, "<Button-1>", lambda event: controller.show_frame(WelcomePage))

        btn1_id = self.canvas.create_image(340, 325, image=self.button1_img)
        self.canvas.tag_bind(btn1_id, "<Button-1>", self.btn1)

        btn2_id = self.canvas.create_image(340, 445, image=self.button2_img)
        self.canvas.tag_bind(btn2_id, "<Button-1>", self.btn2)

        btn3_id = self.canvas.create_image(340, 570, image=self.button3_img)
        self.canvas.tag_bind(btn3_id, "<Button-1>", self.btn3)

    def open_cli(self, event=None):
        print("CLI opens")

    def btn1(self, event=None):
        print("Print Available Trains")
        export_table_to_txt_train()

    def btn2(self, event=None):
        print("Print bookings")
        export_table_to_txt_booking()

    def btn3(self, event=None):
        print("Print passengers")
        export_table_to_txt_passenger()


if __name__ == "__main__":
    app = App()
    app.mainloop()
