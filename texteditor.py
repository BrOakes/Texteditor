import Tkinter
import tkMessageBox
from tkFileDialog import *

main = Tkinter.Tk()


### Menu section

filename = None


# Menu commands
def testcommand():
	print "command"
	
def newFile():
	global filename
	promptSave()
	filename = "Untitled"
	text.delete(0.0, Tkinter.END)
	setTitle()
	
def saveFile():
	global filename
	if filename == None or filename == "Untitled":
		saveAs()
	else:
		t = text.get(0.0, Tkinter.END)
		f = open(filename, 'w')
		f.write(t)
		f.close()
	
def saveAs():
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, Tkinter.END)
	try:
		f.write(t.rstrip())
	except:
		tkMessageBox.showerror(title="Oops!!", message="Unable to save file..")
		
def openFile():
	global filename
	promptSave()
	f = askopenfile(mode='r')
	filename = f.name
	t = f.read()
	text.delete(0.0, Tkinter.END)
	text.insert(0.0, t)
	f.close()
	setTitle()
	
def close():
	global filename
	promptSave()
	filename = None
	text.delete(0.0, Tkinter.END)
	setTitle()
	
def setTitle():
	if filename == None:
		main.title("Jondar")
	else:
		main.title("Jondar - " + str(filename))
		
def promptSave():
	if(filename != None):
		result = tkMessageBox.askquestion("Save", "Would you like to save this document before closing it?", icon='warning')
		if(result == 'yes'):
			if(filename != "Untitled"):
				saveFile()
			else:
				saveAs()
	

def selectAll():
	text.tag_add(Tkinter.SEL, "1.0", Tkinter.END)
	text.mark_set(Tkinter.INSERT, "1.0")
	text.see(Tkinter.INSERT)
	
setTitle()

menubar = Tkinter.Menu(main)

#Filemenu code
filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as", command=saveAs)
filemenu.add_command(label="Close", command=close)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

#Editmenu code
editmenu = Tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: main.focus_get().event_generate('<<Cut>>'))
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: main.focus_get().event_generate('<<Copy>>'))
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: main.focus_get().event_generate('<<Paste>>'))
editmenu.add_command(label="Select All", accelerator="Ctrl+A", command=selectAll)
menubar.add_cascade(label="Edit", menu=editmenu)

#Helpmenu code
helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=testcommand)
menubar.add_cascade(label="Help", menu=helpmenu)

main.config(menu=menubar)

### End menu section

### Grid section

#Tkinter.Label(main, text="This is a test").grid(row=0, column=0)

text = Tkinter.Text(main)#.grid(row=0, column=0, sticky="ew")
text.bind("<Control-Key-a>", selectAll())
text.pack()

#mytext2 = Tkinter.Text(main, width=30, height=5)
#mytext2.grid(row=2, column=0, sticky="nsew")

#main.columnconfigure(0, weight=1)
#main.rowconfigure(0, weight=0)
#main.rowconfigure(1, weight=1)
#main.rowconfigure(2, weight=1)


### Text section

##text = Tkinter.Text(main)
##text.pack()


main.mainloop()
