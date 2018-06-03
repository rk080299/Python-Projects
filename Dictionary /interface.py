from tkinter import *
import dict

window = Tk()

window.resizable(False, False)

window.geometry('570x215')
window.title("Dictionary")

data1 =str()

def Meaning():

	t1.delete(1.0,'end')
	data = dict.send(e1.get())
	global data1
	data1 =data
	if type(data)==list:
		for item in data:
			t1.insert(END,item + '\n')
	else:
		t1.insert(END,data)

	e1.delete(0,'end')


def Yes():

	t1.delete(1.0,'end')
	data=data1
	data =data.split(' ')
	try:
		data = dict.send(data[3])
	except:
		t1.delete(1.0,'end')
		t1.insert(END,'Enter the word to find meaning of')
	if type(data)==list:
		for item in data:
			t1.insert(END, item + '\n')
	else:
		t1.insert(END,data)
	e1.delete(0,'end')


def No():
	e1.delete(0,'end')
	t1.delete(1.0,'end')
	t1.insert(END,"Word Doesn't Exit")


lb1 = Label(window, text ='ENTER THE WORD TO FIND MEANING OF')
lb1.grid(row=0, column=0, pady=5, padx=5)



e1 = Entry(window, bg = 'lightblue', bd = 5, width = 30)
e1.grid(row=0, column=1, pady=5)



t1 = Text(window, height = 5, width = 75)
t1.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

scroll = Scrollbar(window, command=t1.yview)
scroll.grid(row=1, column=1, sticky='e')
t1['yscrollcommand'] = scroll.set

b1 = Button(window, text = 'Yes', width = 25, highlightbackground = 'green', command = Yes)
b1.grid(row=2, column=0, pady=5)


b2 = Button(window, text = 'No', width = 25, highlightbackground = 'red',command = No)
b2.grid(row=2, column=1, pady=5)

b3 = Button(window, text = 'Submit', width = 25, highlightbackground = 'green', command = Meaning)
b3.grid(row=3, column=0, pady=5)


b4 = Button(window, text = 'Exit', width = 25, highlightbackground = 'red', command = window.destroy)
b4.grid(row=3, column=1, pady=5)


window.mainloop()
