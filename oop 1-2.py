from tkinter import *

window = Tk()

window.title("Hello Python")
window.geometry("500x400+20+10")

# Insert button widget
lbl = Label(window,text = "Student Semestral Grade",font= ("Verdana",14))
lbl.place(relx=.5,y=100, anchor="center")
btn = Button(window, text = "I am a Button", fg="Orange")
btn.place(x= 50, y=300)

lbl1 = Label(window, text ="Prelim Grade")
lbl2 = Label(window, text = "Midterm Grade")
lbl3 = Label(window, text = "Final Grade")
lbl1.place(x=50,y=150)
lbl2.place(x=50,y=200)
lbl3.place(x=50,y=250)

txtfld = Entry(window, bd =4)
txtfld2 = Entry(window, bd=4)
txtfld3 = Entry(window, bd=4)

txtfld.place(x=150,y=150)
txtfld2.place(x=150, y=200)
txtfld3.place(x=150,y=250)

window.mainloop()