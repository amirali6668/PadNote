from tkinter import *
from tkinter import filedialog
import sys

# =====================
# Globals
# =====================
file_pathm2 = ''
is_dark_mode = False

# =====================
# Functions
# =====================

def update_details_bar():
    for widget in frame.winfo_children():
        widget.destroy()
    Label(frame, text=f"File path: {file_pathm2}").pack()

def Open(event=None):
    global file_pathm2
    open_file = filedialog.askopenfilename(
        initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if open_file:
        with open(open_file, "r") as f:
            content = f.read()
        textbox.delete(1.0, END)
        textbox.insert(END, content)
        file_pathm2 = open_file
        update_details_bar()

def Save(event=None):
    global file_pathm2
    if not file_pathm2:
        f = filedialog.asksaveasfile(defaultextension=".txt",
                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                     initialdir="G:\\")
        if not f:
            return
        file_pathm2 = f.name
    else:
        f = open(file_pathm2, "w")
    f.write(textbox.get(1.0, END))
    f.close()
    update_details_bar()

def darkmode():
    global is_dark_mode
    if not is_dark_mode:
        dark_bg = '#222222'
        dark_fg = '#f0f0f0'
        window.config(bg=dark_bg)
        textbox.config(bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
        frame.config(bg=dark_bg)
        menubar.config(bg=dark_bg, fg=dark_fg)
        filemenu.config(bg=dark_bg, fg=dark_fg)
        savemenu.config(bg=dark_bg, fg=dark_fg)
        domenu.config(bg=dark_bg, fg=dark_fg)
        for widget in frame.winfo_children():
            if isinstance(widget, Label):
                widget.config(bg=dark_bg, fg=dark_fg)
        is_dark_mode = True
    else:
        light_bg = '#f0f0f0'
        light_fg = '#222222'
        window.config(bg=light_bg)
        textbox.config(bg=light_bg, fg=light_fg, insertbackground=light_fg)
        frame.config(bg=light_bg)
        menubar.config(bg=light_bg, fg=light_fg)
        filemenu.config(bg=light_bg, fg=light_fg)
        savemenu.config(bg=light_bg, fg=light_fg)
        domenu.config(bg=light_bg, fg=light_fg)
        for widget in frame.winfo_children():
            if isinstance(widget, Label):
                widget.config(bg=light_bg, fg=light_fg)
        is_dark_mode = False

def shortcuts():
    shwin = Tk()
    shwin.title("Shortcuts")
    shwin.resizable(False, False)
    
    keys = ['Copy', 'Paste', 'Cut', 'Save', 'Open']
    shortcuts_keys = ['Ctrl + C', 'Ctrl + V', 'Ctrl + X', 'Ctrl + S', 'Ctrl + O']
    
    frame1 = Frame(shwin)
    frame1.pack(side=LEFT, padx=10, pady=10)
    frame2 = Frame(shwin)
    frame2.pack(side=LEFT, padx=10, pady=10)
    frame3 = Frame(shwin)
    frame3.pack(side=LEFT, padx=10, pady=10)
    
    for i in range(len(keys)):
        Label(frame1, text=keys[i]).pack()
        Label(frame2, text='=>').pack()
        Label(frame3, text=shortcuts_keys[i]).pack()
    
    shwin.geometry("300x180")
    shwin.mainloop()

def submit():
    Save()

def delete():
    textbox.delete(1.0, END)

# =====================
# Main Window
# =====================
window = Tk()
window.title("Simple Notepad")
window.geometry("800x600")

# =====================
# Menu
# =====================
menubar = Menu(window)
window.config(menu=menubar)

# File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=Open)
filemenu.add_command(label='Save', command=Save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=sys.exit)
menubar.add_cascade(label='File', menu=filemenu)

# Settings Menu
savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label='Dark Mode', command=darkmode)
savemenu.add_command(label='Shortcuts', command=shortcuts)
menubar.add_cascade(label='Settings', menu=savemenu)

# Functions Menu
domenu = Menu(menubar, tearoff=0)
domenu.add_command(label='Submit', command=submit)
domenu.add_command(label='Delete', command=delete)
menubar.add_cascade(label='Functions', menu=domenu)

# =====================
# Textbox
# =====================
textbox = Text(window, font=("Arial", 16))
textbox.pack(fill=BOTH, expand=True)

# =====================
# Details Bar
# =====================
frame = Frame(window)
frame.pack(side=BOTTOM, fill=X)

# =====================
# Keyboard Shortcuts
# =====================
window.bind('<Control-s>', Save)
window.bind('<Control-o>', Open)

# =====================
# Start App
# =====================
window.mainloop()
