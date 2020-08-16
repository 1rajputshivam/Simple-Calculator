from tkinter import * 
from tkinter.messagebox import *
font=("Verdana",22,"bold")
def click_btn(event):
    print("btn clicked")
    b=event.widget
    text=b["text"]
    print(text) 
    if text=="=":
        try:
            ex=textfield.get()
            anser=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,anser)
        except Exception as e:
            print("Error..",e)
            showerror("Error",e)
        return
    textfield.insert(END,text)
def all_clear():
    textfield.delete(0,END)
def clear():
    ex=textfield.get()
    ex=ex[0:len(ex)-2]
    textfield.delete(0,END)
    textfield.insert(0,ex)
w=Tk()
w.title("calculator")
w.geometry("480x550")
#picture label
pic=PhotoImage(file="cal_logo.png")
headlabel=Label(w,image=pic)
headlabel.pack(side=TOP,pady=5)
#heading label
heading=Label(w,text="calculator",font=font,fg="red")
heading.pack(side=TOP)
textfield=Entry(w,font=font,justify=RIGHT)
textfield.pack(side=TOP,pady=10,fill=X,padx=10)
bframe=Frame(w)
bframe.pack(side=TOP)
temp=1
for i in range(1,4):
    for j in range(0,3):
        btn=Button(bframe,text=temp,font=font,width=5,activebackground="orange",activeforeground="white")
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp=temp+1
        btn.bind("<Button-1>",click_btn)
clearbtn=Button(bframe,text="C",font=font,width=5,activebackground="orange",activeforeground="white",command=all_clear)
clearbtn.grid(row=0,column=0,padx=5,pady=5)
modbtn=Button(bframe,text="%",font=font,width=5,activebackground="orange",activeforeground="white")
modbtn.grid(row=0,column=2,padx=5,pady=5)
divbtn=Button(bframe,text="/",font=font,width=5,activebackground="orange",activeforeground="white")
divbtn.grid(row=0,column=3,padx=5,pady=5)
plusbtn=Button(bframe,text="+",font=font,width=5,activebackground="orange",activeforeground="white")
plusbtn.grid(row=3,column=3,padx=5,pady=5)
minusbtn=Button(bframe,text="-",font=font,width=5,activebackground="orange",activeforeground="white")
minusbtn.grid(row=2,column=3,padx=5,pady=5)
multibtn=Button(bframe,text="*",font=font,width=5,activebackground="orange",activeforeground="white")
multibtn.grid(row=1,column=3,padx=5,pady=5)
btn0=Button(bframe,text=0,font=font,width=5,activebackground="orange",activeforeground="white")
btn0.grid(row=4,column=1,padx=5,pady=5)
dot=Button(bframe,text=".",font=font,width=5,activebackground="orange",activeforeground="white")
dot.grid(row=4,column=0,padx=5,pady=5)
clrbtn=Button(bframe,text="X",font=font,width=5,activebackground="orange",activeforeground="white",command=clear)
clrbtn.grid(row=0,column=1,padx=5,pady=5)
equalbtn=Button(bframe,text="=",font=font,width=11,bg="orange",activebackground="yellow",activeforeground="white")
equalbtn.grid(row=4,column=2,columnspan=2)
clearbtn.bind("<Button-1>",click_btn)
modbtn.bind("<Button-1>",click_btn)
divbtn.bind("<Button-1>",click_btn)
plusbtn.bind("<Button-1>",click_btn)
minusbtn.bind("<Button-1>",click_btn)
multibtn.bind("<Button-1>",click_btn)
btn0.bind("<Button-1>",click_btn)
dot.bind("<Button-1>",click_btn)
clrbtn.bind("<Button-1>",click_btn)
equalbtn.bind("<Button-1>",click_btn)



w.mainloop()