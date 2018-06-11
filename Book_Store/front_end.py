from tkinter import *
from tkinter import messagebox
from back_end import *
window = Tk()

window.resizable(False, False)

window.title("Book Store")


def view_all():

	list1.delete(0,END)
	for row in view():
		list1.insert(END,row)

def search_entry():

	list1.delete(0,END)
	for row in search(e1.get(),e2.get(),e3.get(),e4.get()):
		list1.insert(END,row)

def add_entry():

	insert(e1.get(),e2.get(),e3.get(),e4.get())
	messagebox.showinfo('Message','Record added sucessfully')

def get_selected_row(event):

	global selected_tuple
	try:
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)

		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])

		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])

		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])

		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])

	except IndexError:

		messagebox.showinfo('Message','File is Empty \n Add Record First ...')


def delete_command():

	delete(selected_tuple[0])
	view_all()
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)


def update_command():

	update(selected_tuple[0], e1.get(), e2.get(), e3.get(), e4.get())
	view_all()


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

e1 = Entry(window, bg="lightgray")
e1.grid(row=0,column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

e2 = Entry(window, bg="lightgray")
e2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

e3 = Entry(window , bg="lightgray")
e3.grid(row=1, column=1)

l4 = Label(window, text="ID")
l4.grid(row=1, column=2)

e4 = Entry(window, bg="lightgray")
e4.grid(row=1, column=3)


list1 = Listbox(window, bg="lightblue", height=11, width=40)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)


list1.bind('<<ListboxSelect>>',get_selected_row)


scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)


list1.configure(yscrollcommand = scroll.set)
scroll.configure(command = list1.yview)

b1 = Button(window, text = "View All", background="limegreen",  width=19, command=view_all)
b1.grid(row=2, column=3)


b2 = Button(window, text = "Search Entry", background="limegreen",  width=19, command=search_entry)
b2.grid(row=3, column=3)

b3 = Button(window, text = "Add Entry", background="limegreen",  width=19, command=add_entry)
b3.grid(row=4, column=3)

b4 = Button(window, text = "Update", background="limegreen",  width=19, command=update_command)
b4.grid(row=5, column=3)


b5 = Button(window, text = "Delete", background="limegreen", width=19, command=delete_command)
b5.grid(row=6, column=3)


b6 = Button(window, text = "Close",background="red",  width=19, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
