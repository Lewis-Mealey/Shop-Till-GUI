from tkinter import * 

picture = Tk()
picture.title("Happy Coffee Help")

def menu():
    picture.destroy()

canvas = Canvas(picture, width = 1450, height = 810)
exitprog=Button(picture,fg="red",font=("Arial Rounded MT Bold", 30),text="QUIT",bg="grey",command=menu).pack(fill=X)

image = PhotoImage(file = "happyhelp.png")

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

picture.mainloop()
