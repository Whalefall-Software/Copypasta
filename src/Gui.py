import Main
import tkinter as tk
from tkinter import filedialog

class App():

    def __init__(self, root):
        self.root = root
        self.root.title("Copypasta")
        # self.root.geometry("800x900")
        self.Ui(root)
        root.minsize(root.winfo_width(), root.winfo_height())
        self.root.mainloop()
    
    # Function for opening file explorer to select folder/drive for file transfer
    def BrowseDir(self):
        dirName = filedialog.askdirectory(initialdir='/', title="Select a Directory")
        
    def Ui(self, root):
        selected = tk.StringVar()
        radioBtnCopy = tk.Radiobutton(text='Copy', value=1, variable=selected).grid(row=0,column=10)
        radioBtnMove = tk.Radiobutton(text='Move', value=2, variable=selected).grid(row=0,column=11)
        
        srcLabel = tk.Label(root, text="Path to source:", font=("IBM Plex Mono", 12))
        srcLabel.grid(row=1,column=1)
        srcDirTextBox = tk.Text(root, height=1, width=25, font=("Arial", 14))
        srcDirTextBox.grid(row=2,column=1)
        
        btnSrcDir = tk.Button(root, text="SRC", font=("IBM Plex Mono", 8), command=self.BrowseDir)
        btnSrcDir.grid(row=2, column=9)

        # Arrow design from SRC to DIST 
        # canvas = tk.Canvas(root)
        # canvas.grid(row=1, column=11)
        # canvas.create_line(15, 25, 50, 25, arrow=tk.LAST)

        distLabel = tk.Label(root, text="Path to destination:", font=("IBM Plex Mono", 12))
        distLabel.grid(row=1, column=14)
        distDirTxtBox = tk.Text(root, height=1, width=25, font=("Arial", 14))
        distDirTxtBox.grid(row=2,column=14)

        btnDistDir = tk.Button(root, text="DIST", font=("IBM Plex Mono", 8), command=self.BrowseDir)
        btnDistDir.grid(row=2, column= 15)

    def Validation(self, Ui):
        src: str = Ui.srcDirTextBox.get("1.0",tk.END)
        Main.ValidateDirectory(src)
        
        dist: str = Ui.distDirTxtBox.get("1.0",tk.END)
        Main.ValidateDirectory(dist)

def Launch():
    root = tk.Tk()
    app = App(root)
    app = app.__init__(root)
        
