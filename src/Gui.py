import tkinter as tk

class App():
    def __init__(self, root):
        self.root = root
        self.root.title("Copypasta")
        self.root.geometry("800x900")
        self.ui(root)
        self.root.mainloop()

    def ui(self, root):
        label = tk.Label(root, text="Welcome to Copypasta!", font=("IBM Plex Mono", 20))
        label.pack(padx=20, pady=20)
        srcLabel = tk.Label(root, text="Path to source:", font=("IBM Plex Mono", 12))
        srcLabel.pack()
        srcDirTextBox = tk.Text(root, height=1, width=25, font=("Arial", 14))
        srcDirTextBox.pack(padx=5, pady=5)

def launch():
    root = tk.Tk()
    app = App(root)
    app = app.__init__(root)
        
