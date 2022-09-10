from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def user_info(new_window2):
    label_info = Label(new_window2,text=f"Account Detail\n"
                            f"Account Holder:{log_name().get().title()}\n"
                            f"Account Number:{log_number().get()}")
    label_info.pack()

def check_balance(new_window2):
    label_balance = Label(new_window2, text= "Available balance: Rm%.2f" %balance)
    label_balance.pack()

def deposit(new_window2):
    label_Deposit= Label(new_window2,text="Enter amount to deposit: Rm")
    label_Deposit.pack()
    entry_Deposit = Entry(new_window2)
    entry_Deposit.pack()
    new_balance = balance + entry_Deposit.get()
    label_Deposit_Viewer = Label(new_window2,text="The total balance is Rm%.2f" %new_balance)
    label_Deposit_Viewer.pack()

def withdraw(new_window2):
    label_Withdraw= Label(new_window2,text="Enter amount to withdraw: Rm")
    label_Withdraw.pack()
    entry_Withdraw = Entry(new_window2)
    entry_Withdraw.pack()
    new_balance = balance - entry_Withdraw.get()
    if entry_Withdraw.get() >= balance:
        messagebox.showwarning(title='Low Balance',message="Insufficient Balance")
        label_Withdraw_Viewer = Label(new_window2, text="The total balance is Rm%.2f" % balance)
        label_Withdraw_Viewer.pack()
    else:
        label_Withdraw_Viewer = Label(new_window2, text="The total balance is Rm%.2f" % new_balance)
        label_Withdraw_Viewer.pack()

def new_window_2():
    new_window2 = Tk()
    new_window2.geometry('300x300')



# radio button for menu
def button_menu(new_window):
    ButtonMenu1 = Button(new_window, text='1.Account Details')
    ButtonMenu1.pack()
    ButtonMenu2 = Button(new_window, text='2.Check Balances')
    ButtonMenu2.pack()
    ButtonMenu3 = Button(new_window, text='3.Deposit')
    ButtonMenu3.pack()
    ButtonMenu4 = Button(new_window, text='4.Withdraw')
    ButtonMenu4.pack()
def Menu(new_window):
    menu_label = Label(new_window, text=f"Menu")
    menu_label.pack()

#open new window
def open_new_window():
    new_window = Tk()
    new_window.geometry('300x150')
    Menu(new_window)
    button_menu(new_window)
    master.destroy()



def log_name():
    account_name = entry_name.get()
    nonspace = account_name.replace(' ', '')
    if nonspace.isalpha() == False:
        messagebox.showwarning(title='Warning', message='Please enter alphabets only in account name section')
    else:
        return account_name

def log_number():
    account_number = entry_number.get()
    if not account_number.isdigit():
        messagebox.showwarning(title='Warning', message='Please enter number only in account number section')
    else:
        return account_number

def get_info():
    while True:
        if  log_number()==None or log_name()==None:
            break
        else:
            open_new_window()


            break

master = Tk()
menus = ['1.Account Details', '2.Check Balances', '3.Deposit', '4.Withdraw']
# menus_function = [user_info(new_window_2()),check_balance(new_window_2()),deposit(new_window_2()),withdraw(new_window_2())]
balance = 0
img = Image.open("bank.png")
bank_logo = img.resize((100,100))
bank_logo1 = ImageTk.PhotoImage(bank_logo)
bank_logo2 = PhotoImage(file ='bank-988164_640.png')

master.geometry("300x300")

master.title("Bank System")

label = Label(master, text="Welcome to the bank", height=3)
account_name_label = Label(master, text="Account Name:")
account_number_label = Label(master, text="Account Number:")
bank_label = Label(image =bank_logo1)

entry_name = Entry(master)
entry_number = Entry(master)

submit_button = Button(text='submit', command=get_info)
exit_button = Button(text='exit', command=quit)

label.pack()
account_name_label.place(x=10, y=180)
account_number_label.place(x=10, y=200)
bank_label.place(x=90,y=57)

entry_name.place(x=120, y=180)
entry_number.place(x=120, y=200)

submit_button.place(x=100, y=250)
exit_button.place(x=160, y=250)
master.iconphoto(True, bank_logo2)
master.mainloop()
