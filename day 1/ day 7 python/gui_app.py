#GUI - Graphical user interface

# Libraries
#1. Tkinter
#2. Pyqt
#3. Turtle

import tkinter as ttk

app=ttk.Tk()
app.title('my app')
app.geometry('600x400')
# msg=ttk.Variable(app)
# msg.set('empty')
# print(msg.get())
# ttk.Label(app,text='A simple text Label').place(x=50,y=50)
# ttk.Label(app,textvariable=msg,font=('Arial',25)).place(x=100,y=170)

# def abc():
#     print('dhakan sunta ni he')
#     msg.set('jo tera man kare')
# ttk.Button(app, text='isko click mt krna',command=abc).place(x=100,y=100)
# ttk.Button(app, text='ye wala to bilkul bhini',command=lambda:print('ghda hena tu mna kra tha')).place(x=100,y=130)



f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)
ttk.Entry(app,textvariable=f1,font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app,textvariable=f2,font=('Arial',22)).place(x=150,y=200)
ttk.Label(app,text='result').place(x=100,y=300)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=100,y=330)
def calci(op):
    print('i will caculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=240)    
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=240)    
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=240)    
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=240)    

box = ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1,'sample1')
box.insert(2,'sample2')
box.insert(3,'sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))
ttk.Button(app,text='show',command=show).place(x=350,y=250)
#a function can be taken as input argument in another function
#a funcin can be assigned to an identifier
#  
# 
app.mainloop()



import tkinter as ttk
app=ttk.rt()
app.title('yn')
app.mainloop()
