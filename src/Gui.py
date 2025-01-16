import tkinter as tk

class GUI():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1920x1080')
        self.window.title("Copypasta")
        
        self.copyButton = tk.Button(self.window, text="Copy", font=("Fira Code", 16))
        self.copyButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.copyButton.place(x=950,y=100)
        self.moveButton = tk.Button(self.window, text="Move", font=("Fira Code", 16))
        self.moveButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.moveButton.place(x=850, y=100)
        
        self.startButton = tk.Button(self.window, text="Start", font=("Fira Code", 14))
        self.startButton.pack(padx=2, pady=1, fill=tk.BOTH)
        self.startButton.place(x=1800, y=920)
        self.exitButton = tk.Button(self.window, text="Exit", font=("Fira Code", 14))
        self.exitButton.pack(padx=2, pady=1, expand=True, fill=tk.BOTH)
        self.exitButton.place(x=1700, y=920)
        
        # self.label = tk.Label(self.window, text="Hello, Center!", font=("Arial", 16), bg="lightblue")
        # self.label.update_idletasks()  # Update the widget to get the correct dimensions
        # self.window_width = self.window.winfo_width()
        # self.window_height = self.window.winfo_height()
        # self.widget_width = self.label.winfo_reqwidth()
        # self.widget_height = self.label.winfo_reqheight()
        # self.x = (self.window_width - self.widget_width) // 2
        # self.y = (self.window_height - self.widget_height) // 2
        # print(f"{self.x}, {self.y}")
        
        self.browseDestinationDirButton = tk.Button(self.window, text="BD", font=("Fira Code", 16))
        self.browseDestinationDirButton.pack(padx=1, pady=200)
        self.browseDestinationDirButton.place(x=1100, y=190)
        self.browseSourceDirButton = tk.Button(self.window, text="BS", font=("Fira Code", 16))
        self.browseSourceDirButton.pack(padx=1, pady=200)
        self.browseSourceDirButton.place(x=1300, y=190)
        self.browseDestinationDirButton.place(x=850, y=190)
        
        self.sourceDirectoryTextBox = tk.Text(self.window, height=1, width=30, font=("Arial", 12))
        self.sourceDirectoryTextBox.pack(padx=.05, pady=3, expand=False, fill=tk.X)
        self.sourceDirectoryTextBox.place(x=550, y=200)
        self.destinationDirectoryTextBox = tk.Text(self.window, height=1, width=30, font=("Arial", 12))
        self.destinationDirectoryTextBox.pack(padx=1, pady=3, expand=False, fill=tk.X)
        self.destinationDirectoryTextBox.place(x=1000, y=200)
        
        self.window.mainloop()

GUI()

