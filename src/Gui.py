import Main
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class App():

    def __init__(self, root):
        self.root = root
        self.root.title("Copypasta")
        self.Ui(root)
        root.minsize(root.winfo_width(), root.winfo_height())
        self.root.mainloop()
    
    def Ui(self, root):
        selected = tk.StringVar()
        radioBtnCopy = tk.Radiobutton(text='Copy', value=1, variable=selected).grid(row=0,column=10, sticky='w')
        radioBtnMove = tk.Radiobutton(text='Move', value=2, variable=selected).grid(row=0,column=10, sticky='e')
        
        srcLabel = tk.Label(root, text="Path to source:", font=("IBM Plex Mono", 12))
        srcLabel.grid(row=1,column=0, sticky='w')
        srcDirTextBox = tk.Text(root, height=1, width=25, font=("Arial", 14))
        srcDirTextBox.grid(row=2,column=0)
        
        btnSrcDir = tk.Button(root, text="SRC", font=("IBM Plex Mono", 8), command=self.BrowseDir)
        btnSrcDir.grid(row=2, column=1)

        dstLabel = tk.Label(root, text="Path to destination:", font=("IBM Plex Mono", 12))
        dstLabel.grid(row=1, column=19, sticky='w')
        dstDirTxtBox = tk.Text(root, height=1, width=25, font=("Arial", 14))
        dstDirTxtBox.grid(row=2,column=19)

        btnDstDir = tk.Button(root, text="DST", font=("IBM Plex Mono", 8), command=self.BrowseDir)
        btnDstDir.grid(row=2, column=20)

        btnExit = tk.Button(root, height=2, width=5, padx=2, text="EXIT", font=("IBM Plex Mono", 8))
        btnExit.grid(row=6, column=0, sticky='w')

        btnStart = tk.Button(root, height=2, width=5, padx=2, text="START", font=("IBM Plex Mono", 8))
        btnStart.grid(row=6, column=20, sticky='w')

        transferMethods = ["Skip", "Overwrite", "Merge", "Ask Each Time"]
        chooseTransferMethod = ttk.Combobox(root, values=transferMethods)
        chooseTransferMethod.set("Select transfer method.")
        chooseTransferMethod.grid(row=7, column=10, padx=0, sticky='nsew')

    # Function for opening file explorer to select folder/drive for file transfer
    def BrowseDir(self):
            try:
                selectedPath: str = filedialog.askdirectory(initialdir='/', title="Select a Directory")
                if (selectedPath):
                    dirPath: str = selectedPath
                else:
                    messagebox.showwarning("Canceled", "No path selected!")
            except Exception as e:
                messagebox.showerror(f"{e} error!")

    def Validation(self, Ui):
        src: str = Ui.srcDirTxtBox.get("1.0",tk.END)
        Main.ValidateDirectory(src)
        
        dst: str = Ui.dstDirTxtBox.get("1.0",tk.END)
        Main.ValidateDirectory(dst)
    
    # Copy/Move operation 
    def OperationToggle(self):
        pass
    
def Launch():
    root = tk.Tk()
    app = App(root)
    app = app.__init__(root)