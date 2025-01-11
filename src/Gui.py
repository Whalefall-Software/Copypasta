import tkinter as tk

class GUI():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1920x1080')
        self.window.title("Copypasta")
        
        self.copyButton = tk.Button(self.window, text="Copy", font=("Fira Code", 16))
        self.copyButton.pack(padx=2, pady=1)
        self.copyButton.place(x=10,y=20)
        self.moveButton = tk.Button(self.window, text="Move", font=("Fira Code", 16))
        self.moveButton.pack(padx=2, pady=1)
        self.moveButton.place(x=10, y=60)
        
        self.startButton = tk.Button(self.window, text="Start", font=("Fira Code", 16))
        self.startButton.pack(padx=2, pady=1)
        self.startButton.place()
        self.exitButton = tk.Button(self.window, text="Exit", font=("Fira Code", 16))
        self.exitButton.pack(padx=2, pady=1)
        
        self.browseDestinationDirButton = tk.Button(self.window, text="Browse Destination", font=("Fira Code", 16))
        self.browseDestinationDirButton.pack(padx=1, pady=2)
        self.browseSourceDirButton = tk.Button(self.window, text="Browse Source", font=("Fira Code", 16))
        self.browseSourceDirButton.pack(padx=1, pady=2)
        
        self.sourceDirectoryTextBox = tk.Text(self.window, height=5, font=("Fira Code", 16))
        self.sourceDirectoryTextBox.pack(padx=.05, pady=3)
        self.destinationDirectoryTextBox = tk.Text(self.window, height=5, font=("Fira Code", 16))
        self.destinationDirectoryTextBox.pack(padx=1, pady=3)
        
        self.window.mainloop()

GUI()

