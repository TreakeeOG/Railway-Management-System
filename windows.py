import tkinter as tk
from tkinter import Canvas, PhotoImage

def register():
    root = tk.Tk()
    root.geometry("390x844")
    root.resizable(False, False)

    canvas = Canvas(
        root,
        width=390,
        height=844,
        highlightthickness=0
    )
    canvas.pack()

    bg_image = PhotoImage(file="assets/register/bg.png")
    register_img = PhotoImage(file="assets/register/register_btn.png")
    hero_img = PhotoImage(file="assets/register/Hero.png")
    back_img = PhotoImage(file="assets/register/back_btn.png")
    ticket_img = PhotoImage(file="assets/register/ticket.png")

    canvas.create_image(195, 422, image=bg_image)
    canvas.create_image(210,63, image = hero_img)
    canvas.create_image(195, 500, image = ticket_img)

    # Adding input fields
    username_entry = tk.Entry(root, font=("Kumbh Sans", 12),fg="black", bg = "#CFC5B9", relief="flat")
    username_entry.place(x=60, y=335, width=200, height=30)

    password_entry = tk.Entry(root, font=("Arial", 12),fg="black",bg = "#CFC5B9", relief="flat",show="*")
    password_entry.place(x=60, y=415, width=200, height=30)

    password_reentry = tk.Entry(root, font=("Arial", 12),fg="black",bg = "#CFC5B9", relief="flat")
    password_reentry.place(x=60, y=495, width=200, height=30)


    def open_register(event=None):
        print("Register")
        print("Username:", username_entry.get())
        print("Password:", password_entry.get())
        print("re entered Password:",password_reentry.get())

    def back(event=None):
        print("Back to Welcome")

    # Register button (image only)
    reg_id = canvas.create_image(195, 590, image=register_img)
    canvas.tag_bind(reg_id, "<Button-1>", open_register)
    back_id = canvas.create_image(40, 63,image = back_img)
    canvas.tag_bind(back_id, "<Button-1>",back)

    root.mainloop()

def welcome():

    root = tk.Tk()
    root.geometry("390x844")
    root.resizable(False, False)

    canvas = Canvas(
        root,
        width=390,
        height=844,
        highlightthickness=0
    )
    canvas.pack()

    bg_image = PhotoImage(file="assets/Welcome/bg.png")
    register_img = PhotoImage(file="assets/Welcome/btn_register.png")
    login_img = PhotoImage(file="assets/Welcome/btn_login.png")
    hero_img = PhotoImage(file="assets/Welcome/Hero.png")

    canvas.create_image(195, 422, image=bg_image)
    canvas.create_image(195,535, image = hero_img)

    def open_register(event=None): #call register window
        register()

    def open_login(event=None):
        print("Login")

    # Register button (image only)
    reg_id = canvas.create_image(130, 730, image=register_img)
    canvas.tag_bind(reg_id, "<Button-1>", open_register)

    # Login button (image only)
    log_id = canvas.create_image(310, 730, image=login_img)
    canvas.tag_bind(log_id, "<Button-1>", open_login)




    root.mainloop()

def login():
    root = tk.Tk()
    root.geometry("390x844")
    root.resizable(False, False)

    canvas = Canvas(
        root,
        width=390,
        height=844,
        highlightthickness=0
    )
    canvas.pack()

    bg_image = PhotoImage(file="assets/login/bg.png")
    login_img = PhotoImage(file="assets/login/login_btn.png")
    hero_img = PhotoImage(file="assets/login/Hero.png")
    back_img = PhotoImage(file="assets/login/back_btn.png")
    ticket_img = PhotoImage(file="assets/login/ticket.png")

    canvas.create_image(195, 422, image= bg_image)
    canvas.create_image(230,83, image = hero_img)
    canvas.create_image(195, 500, image = ticket_img)

    # Adding input fields
    username_entry = tk.Entry(root, font=("Kumbh Sans", 12),fg="black", bg = "#ED683D", relief="flat")
    username_entry.place(x=60, y=360, width=200, height=30)

    password_entry = tk.Entry(root, font=("Arial", 12),fg="black",bg = "#ED683D", relief="flat",show="*")
    password_entry.place(x=60, y=445, width=200, height=30)



    def open_login(event=None):
        print("login")
        print("Username:", username_entry.get())# <- USERNAME HERE
        print("Password:", password_entry.get())# <- PASSWORD HERE
        username_entry.delete(0,tk.END) 
        password_entry.delete(0,tk.END) 

    def back(event=None):
        print("Back to Welcome")

    # buttons
    reg_id = canvas.create_image(195, 550, image=login_img)
    canvas.tag_bind(reg_id, "<Button-1>", open_login)
    back_id = canvas.create_image(40, 70,image = back_img)
    canvas.tag_bind(back_id, "<Button-1>",back)

    root.mainloop()

def dash():
    root = tk.Tk()
    root.geometry("390x844")
    root.resizable(False, False)

    canvas = Canvas(
        root,
        width=390,
        height=844,
        highlightthickness=0
    )
    canvas.pack()

    bg_image = PhotoImage(file="assets/dash/bg.png")
    access_img = PhotoImage(file="assets/dash/access_btn.png")
    hero_img = PhotoImage(file="assets/dash/Hero.png")
    button1_img = PhotoImage(file="assets/dash/1_btn.png")
    button2_img = PhotoImage(file="assets/dash/2_btn.png")
    button3_img = PhotoImage(file="assets/dash/3_btn.png")
    cross_img = PhotoImage(file="assets/dash/cross_btn.png")
    ticket_img = PhotoImage(file="assets/dash/ticket.png")
    acc_img = PhotoImage(file="assets/dash/acc.png")

    canvas.create_image(195, 422, image= bg_image)
    canvas.create_image(155,150, image = hero_img)
    canvas.create_image(195, 450, image = ticket_img)
    canvas.create_image(100, 60, image = acc_img)

    def open_cli(event=None): #call register window
        print("CLI opens")
    
    def btn1 (event=None):
        print("Pirint Available Trains")
    
    def btn2 (event=None):
        print("Pirint bookings")

    def btn3 (event=None):
        print("Pirint pasengers")

    def logout(event=None):
        print("Back to welcome page")


    # buttons
    access_id = canvas.create_image(195, 700, image= access_img)
    canvas.tag_bind(access_id, "<Button-1>", open_cli)

    cross_id = canvas.create_image(65, 697, image=cross_img)
    canvas.tag_bind(cross_id,"<Button-1>",logout)

    btn1_id = canvas.create_image(340, 325, image= button1_img)
    canvas.tag_bind(btn1_id, "<Button-1>", btn1)

    btn2_id = canvas.create_image(340, 445, image= button2_img)
    canvas.tag_bind(btn2_id, "<Button-1>", btn2)

    btn3_id = canvas.create_image(340, 570, image= button3_img)
    canvas.tag_bind(btn3_id, "<Button-1>", btn3)    

    root.mainloop()

dash()