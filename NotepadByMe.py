from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.colorchooser import askcolor
from tkinter import ttk
import os
from datetime import datetime

root = Tk()
root.title("Untitled-Notepad")
root.wm_iconbitmap("3.ico")
root.geometry("800x600")

# Initialize notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

# Dictionary to store file paths for each tab to save files independently in each tab
file_paths = {}
tabCount = 1
def newTab():
    global File,tabCount
    # Create a new frame for the tab
    new_frame = Frame(notebook)
    new_frame.pack(fill=BOTH, expand=True)
    # Create a new text area for the tab
    new_text_area = Text(new_frame, font="lucida 13", undo=True, maxundo=-1, bg="white", fg="black")
    new_text_area.pack(fill=BOTH, expand=True)
    # Add the new tab to the notebook
    notebook.add(new_frame, text=f"Tab{tabCount}")
    notebook.select(new_frame)
    tabCount += 1
    # Configure scrollbar for new tab
    scrollBar = Scrollbar(new_text_area)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=new_text_area.yview)
    new_text_area.config(yscrollcommand=scrollBar.set)
    # Set file path for new tab to None, it is because to save file in new tabs independently
    file_paths[new_frame] = None

    # Bind events to update menu state
    new_text_area.bind("<<Selection>>", updateMenuState)
    new_text_area.bind("<KeyRelease>", updateMenuState)
    new_text_area.bind("<ButtonRelease-1>", updateMenuState)

    return new_text_area

def newFile():
    current_tab = notebook.select()
    current_frame = notebook.nametowidget(current_tab)
    TextArea = current_frame.winfo_children()[0]
    TextArea.delete(1.0, END)
    file_paths[current_frame] = None
    notebook.tab(current_tab, text="Untitled")
    root.title("Untitled-Notepad")
    TextArea.config(bg="white", fg="black")
    updateMenuState()

def openFile():
    global File, TextArea
    File = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if File == "":
        File = None
    else:
        TextArea = newTab()
        root.title(os.path.basename(File) + "-Notepad")
        TextArea.delete(1.0, END)
        with open(File, "r") as f:
            TextArea.insert(1.0, f.read())
        # Update the file path for the current tab
        current_tab = notebook.select()
        file_paths[notebook.nametowidget(current_tab)] = File
    TextArea.config(bg="white", fg="black")
    updateMenuState()

def saveFile():
    global File,TextArea
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    File = file_paths[notebook.nametowidget(current_tab)]
    if File is None:
        File = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if File == "":
            File = None
        else:
            with open(File, "w") as f:
                f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(File) + "-Notepad")
            notebook.tab(current_tab, text=os.path.basename(File))
            # Update the file path for the current tab
            file_paths[notebook.nametowidget(current_tab)] = File
            print("File Saved.")
    else:
        with open(File, "w") as f:
            f.write(TextArea.get(1.0, END))
        notebook.tab(current_tab, text=os.path.basename(File))
    updateMenuState()

def quitApp():
    root.destroy()

def undo():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    try:
        TextArea.edit_undo()
    except TclError:
        pass
    updateMenuState()

def redo():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    try:
        TextArea.edit_redo()
    except TclError:
        pass
    updateMenuState()

def cut():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    TextArea.event_generate(("<<Cut>>"))
    updateMenuState()

def copy():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    TextArea.event_generate(("<<Copy>>"))
    updateMenuState()

def paste():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    TextArea.event_generate(("<<Paste>>"))
    updateMenuState()

def selectAll():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    TextArea.tag_add("sel", 1.0, END)
    updateMenuState()

def delete():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    try:
        TextArea.delete("sel.first", "sel.last")
    except:
        print("Nothing is selected to delete. Select first, then delete it using the Delete option.")
    updateMenuState()

def timeDate():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TextArea.insert(INSERT,f"The date and time currently is - {now}\n")
    updateMenuState()

def rename():
    current_tab = notebook.select()
    current_frame = notebook.nametowidget(current_tab)
    TextArea = current_frame.winfo_children()[0]
    old_file = file_paths[current_frame]

    if old_file is None:
        showinfo("Rename Error", "No file to rename. Please save the file first.")
        return

    new_file = asksaveasfilename(initialfile=os.path.basename(old_file), defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if new_file:
        try:
            os.rename(old_file, new_file)
            file_paths[current_frame] = new_file
            notebook.tab(current_tab, text=os.path.basename(new_file))
            root.title(os.path.basename(new_file) + "-Notepad")
            showinfo("Rename", "File renamed successfully.")
        except Exception as e:
            showinfo("Rename Error", f"Error renaming file: {e}")
    updateMenuState()

def fontSize():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]

    def applyFontSize():
        selected_size = font_size_var.get()
        if selected_size.isdigit():
            TextArea.config(font=("lucida", int(selected_size)))
        font_size_window.destroy()

    font_size_window = Toplevel(root)
    font_size_window.title("Select Font Size")
    font_size_window.geometry("200x100")

    Label(font_size_window, text="Enter Font Size:").pack(pady=10)

    font_size_var = StringVar()
    font_size_var.set("13")
    font_size_entry = Entry(font_size_window, textvariable=font_size_var)
    font_size_entry.pack(pady=5)

    apply_button = Button(font_size_window, text="Apply", command=applyFontSize)
    apply_button.pack(pady=5)

def about():
    showinfo("NotePad", "Notepad by Biswajit Mishra, a BTech Cse student.")

def changeColourBackground():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    colour = askcolor(title="Choose Background Colour")[1]
    if colour:
        TextArea.config(bg=colour,insertbackground="white")
    updateMenuState()

def changeColourLetter():
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    colour = askcolor(title="Choose Text Colour")[1]
    if colour:
        TextArea.config(fg=colour)
    updateMenuState()

def updateMenuState(event=None): #If a text is not selected then the below actions cannot be performed
    current_tab = notebook.select()
    TextArea = notebook.nametowidget(current_tab).winfo_children()[0]
    
    # Cut, Copy, Delete
    if TextArea.tag_ranges(SEL):
        EditMenu.entryconfig("Cut                 Ctrl+X", state=NORMAL)
        EditMenu.entryconfig("Copy              Ctrl+C", state=NORMAL)
        EditMenu.entryconfig("Delete                   Del", state=NORMAL)
    else:
        EditMenu.entryconfig("Cut                 Ctrl+X", state=DISABLED)
        EditMenu.entryconfig("Copy              Ctrl+C", state=DISABLED)
        EditMenu.entryconfig("Delete                   Del",state=DISABLED)

TextArea = newTab()  # Initialize the first tab
File = None

MenuBar = Menu(root)

FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New Tab", command=newTab)
FileMenu.add_command(label="New File...", command=newFile)
FileMenu.add_command(label="Open File", command=openFile)
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quitApp)
MenuBar.add_cascade(label="File", menu=FileMenu)

EditMenu = Menu(root, tearoff=0)
EditMenu.add_command(label="Undo             Ctrl+Z", command=undo)
EditMenu.add_command(label="Redo              Ctrl+Y", command=redo)
EditMenu.add_separator()
EditMenu.add_command(label="Cut                 Ctrl+X", command=cut)
EditMenu.add_command(label="Copy              Ctrl+C", command=copy)
EditMenu.add_command(label="Paste              Ctrl+V", command=paste)
EditMenu.add_separator()
EditMenu.add_command(label="Select All        Ctrl+A", command=selectAll)
EditMenu.add_command(label="Delete                   Del", command=delete)
EditMenu.add_command(label="Time/Date             F5",command=timeDate)
EditMenu.add_separator()
EditMenu.add_command(label="Rename                 F2",command=rename)
EditMenu.add_command(label="Font Size", command=fontSize)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

ColourMenu = Menu(root, tearoff=0)
ColourMenu.add_command(label="Background", command=changeColourBackground)
ColourMenu.add_command(label="Text", command=changeColourLetter)
MenuBar.add_cascade(label="Change Colour", menu=ColourMenu)

HelpMenu = Menu(root, tearoff=0)
HelpMenu.add_command(label="About Us", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)

root.configure(menu=MenuBar)

root.bind_all("<<Selection>>", updateMenuState)
root.bind_all("<KeyRelease>", updateMenuState)
root.bind_all("<ButtonRelease-1>", updateMenuState)

root.mainloop()
