from tkinter import * #Tkinter (GUI) module
from datetime import datetime #date and day module

today=datetime.now() #getting today's date and day details
listofmonths=["January","February","March","April","May","June","July","August","September","October","November","December"]
date_details=today.strftime("%A")+", "+str(today.day)+" "+listofmonths[today.month-1]+" "+str(today.year)

window=Tk()#creating a object of type window
window.title("Event generator")#giving title
window.geometry("669x599")#giving a appropriate size
window.config(bg="skyblue")
#frame(window,)
Scrollbar(window,orient=VERTICAL,activebackground="black",elementborderwidth=1).pack(side=RIGHT,fill=Y)#adding a scrollbar
Label(text="Know The Day",bg="skyblue",font="felixtitling 25 bold",anchor="nw").pack(side=TOP,pady=1)#title of the project
Label(text=date_details,bg="skyblue",font="calibri 13 ").pack(side=TOP)#today's date and day

f1=Frame(window,bg="blue",width=15,height=50)#creating frame for date entry
f1.pack(side=TOP,pady=2)#packing it

datefromentry=StringVar()#variables to store date details entered from entry widget
datefromentry.set(today.day)
monthfromentry=StringVar()
monthfromentry.set(today.month)
yearfromentry=StringVar()
yearfromentry.set(today.year)

date_entry=Entry(f1,textvariable=datefromentry,justify="center",width=3)#packing the entry widgets in the frame f1
date_entry.grid(row=0,column=0,padx=1,pady=1)
month_entry=Entry(f1,textvariable=monthfromentry,justify="center",width=3)
month_entry.grid(row=0,column=1,padx=1,pady=1)
year_entry=Entry(f1,textvariable=yearfromentry,justify="center",width=7)
year_entry.grid(row=0,column=2,padx=1,pady=1)

Button(window,text="Enter",width=13).pack()

eventframe=Frame(window,bg='white',width=900,height=900)
eventframe.pack(fill="both",expand=True)
ef1=Frame(eventframe,bg="black",width=300,height=300,relief=RAISED)
ef1.pack(side=LEFT,fill="both",expand=True,pady=5,padx=3)
Scrollbar(ef1,orient=VERTICAL,activebackground="black",elementborderwidth=1).pack(side=RIGHT,fill=Y)
ef2=Frame(eventframe,bg="red",width=300,height=300,relief=RAISED)
ef2.pack(side=LEFT,fill="both",expand=True,pady=5,padx=3)
Scrollbar(ef2,orient=VERTICAL,activebackground="black",elementborderwidth=1).pack(side=RIGHT,fill=Y)
ef3=Frame(eventframe,bg="blue",width=300,height=300,relief=RAISED)
ef3.pack(side=LEFT,fill="both",expand=True,pady=5,padx=3)
Scrollbar(ef3,orient=VERTICAL,activebackground="black",elementborderwidth=1).pack(side=RIGHT,fill=Y)

wikiframe=Frame(window,bg="yellow",width=1000,height=100,relief=RAISED)
wikiframe.pack(expand=True,fill="both")
Scrollbar(wikiframe,orient=VERTICAL,activebackground="black",elementborderwidth=1).pack(side=RIGHT,fill=Y)

window.mainloop()