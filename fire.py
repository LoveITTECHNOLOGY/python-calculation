from tkinter import  *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
def btnEqualsInput():
    global operator
    sumup=eval(str(operator))
    text_input.set(sumup)
cal=Tk()
cal.title("this is my first calc")
global operator
operator=""
text_input=StringVar()


txtDisplay=Entry(cal,font=("arial",20,'bold'),insertwidth=4,bd=40,bg="powder blue",textvariable=text_input,
                 justify='right').grid(columnspan=4) #columnspan express is 4 columns
btn0 = Button(cal, font=("arial", 20, 'bold'), fg="black", bg="powder blue", padx=16, pady=16, bd=4

             ,text="0",command=lambda :btnClick(0)).grid(row=1,column=0)
btn1=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="1",command=lambda :btnClick(1)).grid(row=1,column=1)
btn2=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="2",command=lambda :btnClick(2)).grid(row=1,column=2)
btn3=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="4",command=lambda :btnClick(3)).grid(row=1,column=3)
################################################################################################
btn4 = Button(cal, font=("arial", 20, 'bold'), fg="black", bg="powder blue", padx=16, pady=16, bd=4

             ,text="4",command=lambda :btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="5",command=lambda :btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="6",command=lambda :btnClick(6)).grid(row=2,column=2)
btn7=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="7",command=lambda :btnClick(7)).grid(row=2,column=3)
##############################################################################################
btn8 = Button(cal, font=("arial", 20, 'bold'), fg="black", bg="powder blue", padx=16, pady=16, bd=4

             ,text="8",command=lambda :btnClick(8)).grid(row=3,column=0)
btn9=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="9",command=lambda :btnClick(9)).grid(row=3,column=1)
Addition=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="+",command=lambda :btnClick("+")).grid(row=3,column=2)
Multiply=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="*",command=lambda :btnClick("*")).grid(row=3,column=3)
#######################################################################################
Devision = Button(cal, font=("arial", 20, 'bold'), fg="black", bg="powder blue", padx=16, pady=16, bd=4

             ,text="/",command=lambda :btnClick("/")).grid(row=4,column=0)
Substraction=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="-",command=lambda :btnClick("-")).grid(row=4,column=1)
btnClear=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="C",command=lambda :btnClearDisplay()).grid(row=4,column=2)
btnEquals=Button(cal,font=("arial",20,'bold'),fg="black",bg="powder blue",padx=16,pady=16,bd=4
            ,text="=",command=lambda :btnEqualsInput()).grid(row=4,column=3)






cal.mainloop()