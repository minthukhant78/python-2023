from tkinter import *
root = Tk()

frame = Frame(root)

root.geometry("200x150")
root.title("Min Thu Khant Desktop")
frame.pack()

bottonframe = Frame(root)
bottonframe.pack ( side= BOTTOM )
bluebutton = Button(frame,text = 'Blue', fg='blue')
bluebutton.pack( side= TOP )

greenbutton = Button(frame , text = 'Green', fg='green')
greenbutton.pack ( side= LEFT )


skybluenbutton = Button(frame , text = 'Skyblue', fg='skyblue')
skybluenbutton.pack ( side= LEFT )

root.mainloop()