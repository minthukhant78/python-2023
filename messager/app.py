import tkinter as tk

from tkinter import messagebox as me

def answer ():
    me.showerror("အမှားဖြစ်ပါတယ်", "ကျေးဇူးတင်ပါတယ်။")

def callback () :
    if me.askyesno('Verify',"တွက်ရန်သေချောပြီးလား😊😊"):
        me.showwarning("Bye", )
    else :
        me.showinfo ('No been Quit ')

tk.Button(text="တွက်",command= callback) .pack(fill=tk.X)
tk.Button(text="အမှား",command= answer ) .pack(fill=tk.X)

tk.mainloop()
    