
from tkinter import *
from PIL import Image, ImageTk

def get_info():
    x = entry_name.get()
    print(x)


window = Tk()
img = Image.open("bank.png")
# bank_logo1 = PhotoImage(file="C:\\Users\\user\Downloads\\bank.png")
bank_logo = img.resize((100,100))
bank_logo1 = ImageTk.PhotoImage(bank_logo)
bank_logo2 = PhotoImage(file ='bank-988164_640.png')


window.geometry("300x300")
window.title("Bank System")
label = Label(window, text="Welcome to the bank", height=3)
account_name_label = Label(window, text="Account Name:")
account_number_label = Label(window, text="Account Number:")
bank_label = Label(image =bank_logo1)
entry_name = Entry(window)
entry_number = Entry(window)
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
window.iconphoto(True, bank_logo2)
window.mainloop()
