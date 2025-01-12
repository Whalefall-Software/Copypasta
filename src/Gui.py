import tkinter as tk

class GUI():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1920x1080')
        self.window.title("Copypasta")
        
        self.copyButton = tk.Button(self.window, text="Copy", font=("Fira Code", 16))
        self.copyButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.copyButton.place(x=10,y=20)
        self.moveButton = tk.Button(self.window, text="Move", font=("Fira Code", 16))
        self.moveButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.moveButton.place(x=300, y=200)
        
        self.startButton = tk.Button(self.window, text="Start", font=("Fira Code", 16))
        self.startButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.startButton.place(x=1800, y=920)
        self.exitButton = tk.Button(self.window, text="Exit", font=("Fira Code", 16))
        self.exitButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.exitButton.place(x=1700, y=920)
        
        self.browseDestinationDirButton = tk.Button(self.window, text="Browse Destination", font=("Fira Code", 16))
        self.browseDestinationDirButton.pack(padx=1, pady=2)
        self.browseSourceDirButton = tk.Button(self.window, text="Browse Source", font=("Fira Code", 16))
        self.browseSourceDirButton.pack(padx=1, pady=2)
        
        self.sourceDirectoryTextBox = tk.Text(self.window, height=1, width=30, font=("Arial", 12))
        self.sourceDirectoryTextBox.pack(padx=.05, pady=3, expand=False, fill=tk.X)
        self.sourceDirectoryTextBox.place(x=500, y=200)
        self.destinationDirectoryTextBox = tk.Text(self.window, height=1, width=30, font=("Arial", 12))
        self.destinationDirectoryTextBox.pack(padx=1, pady=3, expand=False, fill=tk.X)
        self.destinationDirectoryTextBox.place(x=980, y=200)
        
        self.window.mainloop()

GUI()

