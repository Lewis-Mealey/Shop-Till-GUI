import datetime
import tkinter as tk
from tkinter import *

calc = tk.Tk()
calc.title("Mortgage calculator")

calc.attributes('-fullscreen', True)

window = tk.Canvas(calc, width=1920, height=1080, relief='raised')
window.pack()

totalamount = 0.00


def menu():
    calc.destroy()


def helpo():
    from subprocess import Popen
    Popen('python happy_help.py')


img0 = PhotoImage(file="logo.png")
logo = Label(calc, bg="white", borderwidth=2, relief="groove", image=img0)
logo.place(x=160, y=100, width=350, height=115)

now = datetime.datetime.now()
date = (now.strftime("%B %d, %Y"))

tablee = StringVar(calc)
tablee.set("1")
tables = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

customerinfo = Listbox(calc)


def addtoo():
    name = namer.get()
    tablenum = tablee.get()
    orderinfo = (name + "," + tablenum + "," + "£" + str(totalamount))
    print(orderinfo)
    customerinfo.insert(END, orderinfo)


totalcount = Label(calc, text="0")
totalcount.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), bg="light blue")
window.create_window(840, 900, window=totalcount)

#########################################################################

runningtotal = tk.Label(calc, text='Running Total')
runningtotal.config(font=('helvetica', 30))
window.create_window(840, 840, window=runningtotal)


#########################################################################

def breakfasttea():
    global totalamount
    totalamount += 1.8
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=breakfasttea)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Breakfast tea £1.80", bg="light blue")
window.create_window(1500, 150, window=label2)


def sandwich():
    global totalamount
    totalamount += 4.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=sandwich)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Sandwich £4.50",
              bg="light blue")
window.create_window(1200, 150, window=label2)


def soup():
    global totalamount
    totalamount += 3.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=soup)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Soup £3.50",
              bg="light blue")
window.create_window(1500, 230, window=label2)


def americano():
    global totalamount
    totalamount += 3.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=americano)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Americano £1.50",
              bg="light blue")
window.create_window(1200, 230, window=label2)


def latte():
    global totalamount
    totalamount += 1.9
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=latte)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Latte £1.90",
              bg="light blue")
window.create_window(1500, 310, window=label2)


def combo():
    global totalamount
    totalamount += 6
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=combo)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="S & S Combo £6.00", bg="light blue")
window.create_window(1200, 310, window=label2)


def cappuccino():
    global totalamount
    totalamount += 2
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=cappuccino)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Cappuccino £2.00",
              bg="light blue")
window.create_window(1500, 390, window=label2)


def breakfast():
    global totalamount
    totalamount += 6.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=breakfast)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Full breakfast £6.50", bg="light blue")
window.create_window(1200, 390, window=label2)


def espresso():
    global totalamount
    totalamount += 1.8
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=espresso)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Espresso £1.80",
              bg="light blue")
window.create_window(1500, 470, window=label2)


def goats():
    global totalamount
    totalamount += 7
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=goats)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Goats tart salad £7.00", bg="light blue")
window.create_window(1200, 470, window=label2)


def macchiato():
    global totalamount
    totalamount += 2.2
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=macchiato)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Macchiato £2.20",
              bg="light blue")
window.create_window(1500, 550, window=label2)


def special():
    global totalamount
    totalamount += 5.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=special)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Daily special £5.50", bg="light blue")
window.create_window(1200, 550, window=label2)


def chocolate():
    global totalamount
    totalamount += 2.2
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=chocolate)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Hot Chocolate £2.20", bg="light blue")
window.create_window(1500, 630, window=label2)


def children():
    global totalamount
    totalamount += 1.8
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=children)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16),
              text="Childrens meal £1.80", bg="light blue")
window.create_window(1200, 630, window=label2)


def cake():
    global totalamount
    totalamount += 3
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=cake)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Cake £3.00",
              bg="light blue")
window.create_window(1500, 710, window=label2)


def chino():
    global totalamount
    totalamount += 0.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=chino)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Baby chino £0.50",
              bg="light blue")
window.create_window(1200, 710, window=label2)


def traybake():
    global totalamount
    totalamount += 2.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=traybake)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Tray bake £2.50",
              bg="light blue")
window.create_window(1500, 790, window=label2)


def biscotti():
    global totalamount
    totalamount += 1
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=biscotti)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Biscotti £1.00",
              bg="light blue")
window.create_window(1200, 790, window=label2)


def scone():
    global totalamount
    totalamount += 2.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=scone)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Scone £2.50",
              bg="light blue")
window.create_window(1500, 870, window=label2)


def zerotill():
    global totalamount
    totalamount -= totalamount
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


label2 = tk.Button(calc, text='Help', command=zerotill)
label2.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Zero till £0.00",
              bg="yellow")
window.create_window(1200, 870, window=label2)

help = tk.Button(calc, text='Help', command=helpo)
help.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Help",
            bg="light blue")
window.create_window(840, 150, window=help)

quit = tk.Button(calc, text='Exit', command=menu)
quit.config(width=10, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Exit",
            bg="light blue")
window.create_window(1800, 150, window=quit)


#########################################################################

def twenty():
    global totalamount
    totalamount *= 0.8
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


labeloff = tk.Button(calc, text='Help', command=twenty)
labeloff.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="20% off",
                bg="yellow")
window.create_window(840, 390, window=labeloff)


def thirty():
    global totalamount
    totalamount *= 0.7
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


labeloff = tk.Button(calc, text='Help', command=thirty)
labeloff.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="30% off",
                bg="yellow")
window.create_window(840, 550, window=labeloff)


def fifty():
    global totalamount
    totalamount *= 0.5
    totalamount = round(totalamount, 2)
    totalcount.config(text=totalamount)


labeloff = tk.Button(calc, text='Help', command=fifty)
labeloff.config(width=20, height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="50% off",
                bg="yellow")
window.create_window(840, 710, window=labeloff)

#########################################################################

saveorder = tk.Button(calc, text='Save order', command=addtoo)
saveorder.config(height=13, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Save Order",
                 bg="yellow")
window.create_window(550, 900, window=saveorder)

#########################################################################

label1 = tk.Label(calc, text=date)
label1.config(font=('helvetica', 20))
window.create_window(320, 280, window=label1)

label3 = tk.Label(calc, text='Name')
label3.config(font=('helvetica', 20))
window.create_window(320, 435, window=label3)

label1 = tk.Label(calc, text='Table number')
label1.config(font=('helvetica', 20))
window.create_window(320, 595, window=label1)

customerinfo = tk.Listbox(calc, )
customerinfo.config(font=('helvetica', 20))
window.create_window(320, 900, window=customerinfo)

#########################################################################

namer = tk.Entry(calc)
namer.config(font=('helvetica', 20))
window.create_window(320, 470, window=namer)

tablenum = OptionMenu(calc, tablee, *tables)
tablenum.config(font=('helvetica', 20))
tablenum.place(x=270, y=620, width=100, height=100)


#########################################################################

def savefile():
    file = open(date + ".csv", "a")
    customerlist = customerinfo.get(0, END)
    num = 0
    for x in customerlist:
        newrecord = customerlist[num] + "\n"
        file.write(str(newrecord))
        num = num + 1
    file.close()


safetofile = tk.Button(calc, text='Save order', command=savefile)
safetofile.config(height=2, bd=4, padx=8, fg="black", font=("Arial Rounded MT Bold", 16), text="Save To File",
                  bg="yellow")
window.create_window(840, 1000, window=safetofile)

calc.mainloop()
