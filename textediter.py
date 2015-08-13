import Tkinter

main = Tkinter.Tk()
### Menu section

# Menu commands
def testcommand():
	print "command"

def copy():	
	main.clipboard_clear()
	main.clipboard_append('i can has clipboardz?')

menubar = Tkinter.Menu(main)

#Filemenu code
filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=testcommand)
filemenu.add_command(label="Save", command=testcommand)
filemenu.add_command(label="Save as", command=testcommand)
filemenu.add_command(label="Close", command=testcommand)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

#Editmenu code
editmenu = Tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=testcommand)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=testcommand)
menubar.add_cascade(label="Edit", menu=editmenu)

#Helpmenu code
helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=testcommand)
menubar.add_cascade(label="Help", menu=helpmenu)

main.config(menu=menubar)

### End menu section

### Text section

text = Tkinter.Text(main)
text.pack()


main.mainloop()
