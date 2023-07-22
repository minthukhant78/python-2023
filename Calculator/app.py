from tkinter import *

top = Tk()

L1 = Label(top , text= "Myanmar Mark ")
L1.place(x=10,y=10)
E1 = Entry (top, bd=5)
E1.place(x=90,y=10)

L2 = Label (top , text= "English Mark ")
L2.place(x=10,y=50)
E2 = Entry (top, bd=5)
E2.place(x=90,y=50)


L3 = Label (top , text= "Maths Mark ")
L3.place(x=10,y=150)
E3 = Entry (top, bd=5)
E3.place(x=90,y=150)


L4 = Label (top , text= "Total Mark  ")
L4.place(x=10,y=200)
E4 = Entry (top, bd=5)
E4.place(x=90,y=200)

B = Button (top , text="Add").place(x=200,y=250)
top.geometry("300x350+10+10")
top.mainloop()