# Importing necessary libraries
import tkinter as tk

# Main class for sold out page
class SoldOut:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("690x225")
        self.root.resizable(False, False)
        self.root.title("Sorry!")

        # Placing the main design of the sold out page
        self.sold_out_title = tk.PhotoImage(file="Designs/Misc/Sold_Out_Message.png")
        self.sold_out_title_label = tk.Label(self.root, image=self.sold_out_title)
        self.sold_out_title_label.image = self.sold_out_title
        self.sold_out_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing OK button
        self.ok = tk.PhotoImage(file="Designs/Misc/OK_Button.png")
        self.ok_button = tk.Button(self.root, image=self.ok, relief="raised", command=self.close_window)
        self.ok_button.image = self.ok
        self.ok_button.place(x=600, y=170, anchor="center")
        self.ok_hover = tk.PhotoImage(file="Designs/Misc/OK_Button_Hover.png")
        self.ok_button.bind("<Enter>", self.on_hover_ok)
        self.ok_button.bind("<Leave>", self.on_leave_ok)
        self.ok_button.image = self.ok_hover
    
    # Series of functions for the hover effects for each button
    def on_hover_ok(self, event):
        self.ok_button.config(image=self.ok_hover)

    def on_leave_ok(self, event):
        self.ok_button.config(image=self.ok)

    # Function to close the sold out message window
    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SoldOut(root)
    root.mainloop()