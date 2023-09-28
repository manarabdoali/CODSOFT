from tkinter import *

root = Tk()
root.title("Calculator App")
root.geometry("570x620+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")
equation=""

def show(value):
  global equation
  equation+=value
  resultLable.config(text=equation)

def clear():
  global equation
  equation=""
  resultLable.config(text=equation)

def calculate():
  global equation
  result=""
  if equation!="":
    try:
      result=eval(equation)
    except:
      result="error"
      equation=""
      result.config(text=result)
  resultLable.config(text=str(result))
      

  

#to separate white and black
resultLable = Label(root, width=25, height=2, text="", font=("arial", 30))
resultLable.place(x=10, y=10)

#to show c
button = Button(root, text="c", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:clear())
button.place(x=10, y=100)

button = Button(root, text="/", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("/"))
button.place(x=150, y=100)

button = Button(root, text="*", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("*"))
button.place(x=290, y=100,)

button = Button(root, text="%", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("%"))
button.place(x=430, y=100,)

button = Button(root, text="7", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("7"))
button.place(x=10, y=200)

button = Button(root, text="8", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("8"))
button.place(x=150, y=200,)

button = Button(root, text="9", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("9"))
button.place(x=290, y=200,)

button = Button(root, text="-", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("-"))
button.place(x=430, y=200,)

button = Button(root, text="4", width=5, height=2, font=("arial", 30,"bold"), bd=1 ,fg="#fff" ,bg="#2a2d36" ,command=lambda:show("4"))
button.place(x = 10 ,y = 300 )

button = Button(root,text="5" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("5"))
button.place(x =150 ,y =300 )

button = Button(root,text="6" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("6") )
button.place(x =290 ,y =300 )

button = Button(root,text="+" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("+") )
button.place(x =430 ,y =300 )
button = Button(root, text="1", width=5, height=2, font=("arial", 30,"bold"), bd=1 ,fg="#fff" ,bg="#2a2d36",command=lambda:show("1"))
button.place(x = 10 ,y = 400 )

button = Button(root,text="2" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("2") )
button.place(x =150 ,y =400 )

button = Button(root,text="3" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("3"))
button.place(x =290 ,y =400 )

button = Button(root,text="0" ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("0"))
button.place(x =430 ,y =400 )

button = Button(root,text="." ,width = 5 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#2a2d36",command=lambda:show("."))
button.place(x =10 ,y =500 )

button = Button(root,text="=" ,width = 17 ,height = 2 ,font=("arial" ,30 ,"bold") ,bd = 1 ,fg ="#fff" ,bg ="#fe9037",command=lambda:calculate())
button.place(x =150 ,y =500 )

root.mainloop()
