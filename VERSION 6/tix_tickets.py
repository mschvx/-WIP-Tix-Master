# Importing necessary libraries
import tkinter as tk

# Main class for tickets page
class tixTicket:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Ticket Generated!")
        self.root.configure(bg="#d9e2f1")

        # Placing the main design of the catalogue page
        self.ticket_title = tk.PhotoImage(file="Designs/Ticket/Tix_Ticket.png")
        self.ticket_title_label = tk.Label(self.root, image=self.ticket_title)
        self.ticket_title_label.image = self.ticket_title
        self.ticket_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing the return button
        self.back = tk.PhotoImage(file="Designs/Ticket/Return_Button.png")
        self.back_button = tk.Button(self.root, image=self.back, relief="raised", command=self.open_title)
        self.back_button.image = self.back
        self.back_button.place(x=830, y=625, anchor="center")
        self.back_hover = tk.PhotoImage(file="Designs/Ticket/Return_Button_Hover.png")
        self.back_button.bind("<Enter>", self.on_hover_back)
        self.back_button.bind("<Leave>", self.on_leave_back)
        self.back_button.image = self.back_hover

    # Series of functions for the hover effects of each button
    def on_hover_back(self, event):
        self.back_button.config(image=self.back_hover)

    def on_leave_back(self, event):
        self.back_button.config(image=self.back)

    # Function for restarting (yay!) going back to the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.ticket_title_label.place_forget()
        TixMaster(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = tixTicket(root)
    root.mainloop()