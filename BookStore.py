"""
A program for bookstore
A book will following information:
Title
Author
Year
ISBN

A user can do following with a record:
Search
Insert
Update
Delete

"""

from tkinter import *
from backendgui import DataBase

database=DataBase()

def get_select_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.insert(END, selected_tuple[2])
        e3.insert(END, selected_tuple[3])
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_all():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_rec():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_rec():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_row():
    database.delete(selected_tuple[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_all()

def update_row():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()
window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_select_row)

b1 = Button(window, text="View All", width=12, command=view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_rec)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_rec)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update_row)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete_row)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
