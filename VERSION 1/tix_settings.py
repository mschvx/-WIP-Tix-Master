import tkinter as tk

class TixSettings:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Tix Master - Settings")
        self.root.configure(bg="#d9e2f1")

        self.settings_title = tk.PhotoImage(file="Designs/Tix_Settings.png")
        self.settings_title_label = tk.Label(self.root, image=self.settings_title, bg="#d9e2f1")
        self.settings_title_label.image = self.settings_title
        self.settings_title_label.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = TixSettings(root)
    root.mainloop()