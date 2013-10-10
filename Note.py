__author__ = 'Drax'

from tkinter import *
class Application():
   def __init__(self):
       self.text1=Text(root,font='Arial 12',wrap=WORD)
       self.listbox1=Listbox(root)
       self.ent=Entry(root)


       m = Menu(root) #создается объект Меню на главном окне
       root.config(menu=m) #окно конфигурируется с указанием меню для него


       fm = Menu(m) #создается пункт меню с размещением на основном меню (m)
       m.add_cascade(label="Файл",menu=fm) #пункту располагается на основном меню (m)

       def dob():
           r=['main']
           for i in r:
               self.listbox1.insert(END,i)
           r.insert(0,"mm")

       fm.add_command(label="Добавить",command=dob) #формируется список команд пункта меню

       def close_win():
           root.destroy()
       fm.add_command(label="Exit",command=close_win)

       hm = Menu(m) #второй пункт меню
       m.add_cascade(label="___",menu=hm)
       hm.add_command(label="Помошь")
       hm.add_command(label="О")

       self.text1.grid(column=2,row=1,sticky="n,s,w,e")
       self.listbox1.grid(row=1,column=1,sticky="n,s,w")
       self.ent.grid(row=3)


root = Tk()
obj = Application()
root.mainloop()
  
