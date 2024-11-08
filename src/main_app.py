import tkinter as tk
from pages import HomePage, HelpPage  # Ensure this imports from the correct module name

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prepared 4 Eternity")
        self.root.geometry("1024x600")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (HomePage, HelpPage):
            page_name = F.__name__
            frame = F(parent=self.root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
