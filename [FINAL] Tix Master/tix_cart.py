# Importing necessary libraries
from tkinter import Canvas, Frame, Entry, Label
import tkinter as tk

# Main class for the cart page
class TixCart:
    
    # Setting up basic properties of the window
    def __init__(self, root, load_cart=False):
        self.root = root
        self.root.geometry("360x550")
        self.root.resizable(False, False)
        self.root.title("Tix Cart")

        # Placing the main design of the title page
        self.cart_title = tk.PhotoImage(file="Designs/Cart/Tix_Cart.png")
        self.cart_title_label = tk.Label(self.root, image=self.cart_title, bg="#d9e2f1")
        self.cart_title_label.image = self.cart_title
        self.cart_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Initializing empty variables for later use
        self.concert_name = ''
        self.item_one = ''
        self.item_two = ''
        self.item_three = ''
        self.ticket_holder = ''
        self.price_one = 0
        self.price_two = 0
        self.price_three = 0
        self.total_price = 0

        # Placing the labels that will store the item and price value AND remove button
        # For first item
        self.item_one_label = tk.Label(self.root, text=self.item_one, width=17, height=1, bg="#798ec4", fg="#d9e2f1", font=('Helvetica', 13, 'bold'))
        self.item_one_label.place(x=118, y=130, anchor="center")

        self.price_one_label = tk.Label(self.root, text=self.item_one, width=12, height=1, bg="#d9e2f1", fg="#798ec4", font=('Helvetica', 13, 'bold'))
        self.price_one_label.place(x=270, y=130, anchor="center")

        self.r1 = tk.PhotoImage(file="Designs/Cart/R1.png")
        self.r1_button = tk.Button(self.root, image=self.r1, relief="raised", command=self.remove_item_one)
        self.r1_button.image = self.r1
        self.r1_button.place(x=182, y=167, anchor="center")
        self.r1_hover = tk.PhotoImage(file="Designs/Cart/R1_Hover.png")
        self.r1_button.bind("<Enter>", self.on_hover_r1)
        self.r1_button.bind("<Leave>", self.on_leave_r1)
        self.r1_button.image = self.r1_hover

        # For second item
        self.item_two_label = tk.Label(self.root, text=self.item_one, width=17, height=1, bg="#798ec4", fg="#d9e2f1", font=('Helvetica', 13, 'bold'))
        self.item_two_label.place(x=118, y=210, anchor="center")

        self.price_two_label = tk.Label(self.root, text=self.item_one, width=12, height=1, bg="#d9e2f1", fg="#798ec4", font=('Helvetica', 13, 'bold'))
        self.price_two_label.place(x=270, y=210, anchor="center")

        self.r2 = tk.PhotoImage(file="Designs/Cart/R2.png")
        self.r2_button = tk.Button(self.root, image=self.r2, relief="raised", command=self.remove_item_two)
        self.r2_button.image = self.r1
        self.r2_button.place(x=182, y=247, anchor="center")
        self.r2_hover = tk.PhotoImage(file="Designs/Cart/R2_Hover.png")
        self.r2_button.bind("<Enter>", self.on_hover_r2)
        self.r2_button.bind("<Leave>", self.on_leave_r2)
        self.r2_button.image = self.r1_hover

        # For third item
        self.item_three_label = tk.Label(self.root, text=self.item_one, width=17, height=1, bg="#798ec4", fg="#d9e2f1", font=('Helvetica', 13, 'bold'))
        self.item_three_label.place(x=118, y=290, anchor="center")

        self.price_three_label = tk.Label(self.root, text=self.item_one, width=12, height=1, bg="#d9e2f1", fg="#798ec4", font=('Helvetica', 13, 'bold'))
        self.price_three_label.place(x=270, y=290, anchor="center")

        self.r3 = tk.PhotoImage(file="Designs/Cart/R3.png")
        self.r3_button = tk.Button(self.root, image=self.r2, relief="raised", command=self.remove_item_three)
        self.r3_button.image = self.r3
        self.r3_button.place(x=182, y=327, anchor="center")
        self.r3_hover = tk.PhotoImage(file="Designs/Cart/R3_Hover.png")
        self.r3_button.bind("<Enter>", self.on_hover_r3)
        self.r3_button.bind("<Leave>", self.on_leave_r3)
        self.r3_button.image = self.r3_hover

        # Placing the BUY and GO BACK button
        self.buy = tk.PhotoImage(file="Designs/Cart/Buy_Button.png")
        self.buy_button = tk.Button(self.root, image=self.buy, relief="raised", command=self.open_ticket)
        self.buy_button.image = self.buy
        self.buy_button.place(x=100, y=470, anchor="center")
        self.buy_hover = tk.PhotoImage(file="Designs/Cart/Buy_Button_Hover.png")
        self.buy_button.bind("<Enter>", self.on_hover_buy)
        self.buy_button.bind("<Leave>", self.on_leave_buy)
        self.buy_button.image = self.buy_hover

        self.back = tk.PhotoImage(file="Designs/Cart/Back_Button.png")
        self.back_button = tk.Button(self.root, image=self.back, relief="raised", command=self.open_layout)
        self.back_button.image = self.back
        self.back_button.place(x=260, y=470, anchor="center")
        self.back_hover = tk.PhotoImage(file="Designs/Cart/Back_Button_Hover.png")
        self.back_button.bind("<Enter>", self.on_hover_back)
        self.back_button.bind("<Leave>", self.on_leave_back)
        self.back_button.image = self.back_hover

        # Placing total price computation
        self.price_canvas = Canvas(self.root, width=360, height=50, bg="#d9e2f1", highlightthickness=0)
        self.price_canvas.place(x=0, y=500, anchor="nw")
        self.total = self.price_canvas.create_text(
            180, 25,  # Center of the canvas
            text=f"Total: ₱{self.total_price}", 
            font=("Helvetica", 15, "bold"), 
            fill="#798ec4"
        )

        # Asking for name
        name_label_frame = Frame(self.root, bg='#798ec4')
        name_label = Label(name_label_frame, text="Enter your name:", font=('Helvetica', 12, 'bold'), fg='#edebe7', bg='#798ec4')
        name_label.pack(padx=10, pady=5, side="left")
        self.name_entry = Entry(name_label_frame, font=('Helvetica', 12), fg='#151c4c', width=15)
        self.name_entry.pack(pady=5, padx=10, side="left")
        name_label_frame.place(x=23, y=400, anchor='nw')

        if load_cart:
            self.load_cart() # Loading the values

    # Function for loading the cart
    def load_cart(self):
        with open("tix_cart.dat", "r") as tixCart:
            load = tixCart.readlines()
            concert_name = load[0].strip()
            item_one, price_one = load[1].strip().split(':')
            price_one = int(price_one)
            if len(load) > 2:
                item_two, price_two = load[2].strip().split(':')
                price_two = int(price_two)
            else:
                item_two, price_two = "N/A", 0
            if len(load) > 3:
                item_three, price_three = load[3].strip().split(':')
                price_three = int(price_three)
            else:
                item_three, price_three = "N/A", 0

        # Storing the values into the label message after extracting them
        self.concert_name = concert_name
        self.item_one = item_one
        self.price_one = price_one
        self.item_two = item_two
        self.price_two = price_two
        self.item_three = item_three
        self.price_three = price_three

        # Update total price
        self.total_price = price_one + price_two + price_three
        self.price_canvas.itemconfig(self.total, text=f"Total: ₱{self.total_price}")

        # Call update cart (checks if anything is removed)        
        self.update_cart()

    # Function for saving the current items in the cart
    def save_cart(self):
        with open("tix_cart.dat", "w") as tixCart:
            tixCart.write(f"{self.concert_name}\n")
            if self.item_one != "N/A":
                tixCart.write(f"{self.item_one}:{self.price_one}\n")
            if self.item_two != "N/A":
                tixCart.write(f"{self.item_two}:{self.price_two}\n")
            if self.item_three != "N/A":
                tixCart.write(f"{self.item_three}:{self.price_three}\n")
            
    # Series of functions tied to the remove button
    def remove_item_one(self):
        self.item_one = self.item_two # Basically previous items will go to the higher position
        self.price_one = self.price_two
        self.item_two = self.item_three
        self.price_two = self.price_three
        self.item_three = "N/A"
        self.price_three = 0
        self.update_cart()
        self.save_cart()  # Save the cart after updating

    def remove_item_two(self):
        self.item_two = self.item_three
        self.price_two = self.price_three
        self.item_three = "N/A"
        self.price_three = 0
        self.update_cart()
        self.save_cart()  # Save the cart after updating

    def remove_item_three(self):
        self.item_three = "N/A"
        self.price_three = 0
        self.update_cart()
        self.save_cart()  # Save the cart after updating

    # Function that checks if anything changes
    def update_cart(self):
        self.item_one_label.config(text=self.item_one)
        self.price_one_label.config(text=f"₱{self.price_one}")
        self.item_two_label.config(text=self.item_two)
        self.price_two_label.config(text=f"₱{self.price_two}")
        self.item_three_label.config(text=self.item_three)
        self.price_three_label.config(text=f"₱{self.price_three}")
        # Same logic making the previous functions go one step above if the one former to it is removed
        if self.item_one == "N/A" and self.price_one == 0:
            self.item_one_label.place_forget()
            self.price_one_label.place_forget()
            self.r1_button.place_forget()
        else:
            self.item_one_label.place(x=118, y=130, anchor="center")
            self.price_one_label.place(x=270, y=130, anchor="center")
            self.r1_button.place(x=182, y=167, anchor="center")

        if self.item_two == "N/A" and self.price_two == 0:
            self.item_two_label.place_forget()
            self.price_two_label.place_forget()
            self.r2_button.place_forget()
        else:
            self.item_two_label.place(x=118, y=210, anchor="center")
            self.price_two_label.place(x=270, y=210, anchor="center")
            self.r2_button.place(x=182, y=247, anchor="center")

        if self.item_three == "N/A" and self.price_three == 0:
            self.item_three_label.place_forget()
            self.price_three_label.place_forget()
            self.r3_button.place_forget()
        else:
            self.item_three_label.place(x=118, y=290, anchor="center")
            self.price_three_label.place(x=270, y=290, anchor="center")
            self.r3_button.place(x=182, y=327, anchor="center")

        self.total_price = int(self.price_one) + int(self.price_two) + int(self.price_three)
        self.price_canvas.itemconfig(self.total, text=f"Total: ₱{self.total_price}")

        # Disable buy button if no items in cart
        if self.item_one == "N/A" and self.item_two == "N/A" and self.item_three == "N/A":
            self.buy_button.config(state="disabled")
        else:
            self.buy_button.config(state="normal")

    # Series of functions for the hover effects of each button
    def on_hover_r1(self, event):
        self.r1_button.config(image=self.r1_hover)

    def on_leave_r1(self, event):
        self.r1_button.config(image=self.r1)

    def on_hover_r2(self, event):
        self.r2_button.config(image=self.r2_hover)

    def on_leave_r2(self, event):
        self.r2_button.config(image=self.r2)

    def on_hover_r3(self, event):
        self.r3_button.config(image=self.r3_hover)

    def on_leave_r3(self, event):
        self.r3_button.config(image=self.r3)

    def on_hover_buy(self, event):
        self.buy_button.config(image=self.buy_hover)

    def on_leave_buy(self, event):
        self.buy_button.config(image=self.buy)

    def on_hover_back(self, event):
        self.back_button.config(image=self.back_hover)

    def on_leave_back(self, event):
        self.back_button.config(image=self.back)

    # Function for going back to layout page
    def open_layout(self):
        # Seamless checking for all concert types 
        if self.concert_name == "Elphaba - Day 1":
            from seats_ed1 import ED1Layout
            self.cart_title_label.place_forget()
            ED1Layout(self.root, load_cart=True)

        elif self.concert_name == "Elphaba - Day 2":
            from seats_ed2 import ED2Layout
            self.cart_title_label.place_forget()
            ED2Layout(self.root, load_cart=True)

        elif self.concert_name == "Glinda - Day 1":
            from seats_gd1 import GD1Layout
            self.cart_title_label.place_forget()
            ED1Layout(self.root, load_cart=True)
            
        elif self.concert_name == "Glinda - Day 2":
            from seats_gd2 import GD2Layout
            self.cart_title_label.place_forget()
            ED2Layout(self.root, load_cart=True)

    # Function for opening the ticket interface/finalizing the shopping process
    def open_ticket(self):
        self.ticket_holder = self.name_entry.get().upper()
        if self.ticket_holder == '':
            self.blink_entry(self.name_entry, '#ccd9f3', '#ffffff', 5)
        else:
            with open("tix_cart.dat", "w") as tixCart:
                tixCart.write(f"{self.concert_name}\n")
                if self.item_one != "N/A":
                    tixCart.write(f"{self.item_one}:{self.price_one}\n")
                if self.item_two != "N/A":
                    tixCart.write(f"{self.item_two}:{self.price_two}\n")
                if self.item_three != "N/A":
                    tixCart.write(f"{self.item_three}:{self.price_three}\n")
                tixCart.write(f"{self.ticket_holder}")
            from tix_tickets import tixTicket
            self.cart_title_label.place_forget()
            self.price_canvas.place_forget()  # Remove the canvas before transitioning
            tixTicket(self.root)

    # Blinking effect for name if no name is inputted to signal
    def blink_entry(self, entry, color1, color2, count, interval=100):
        if count > 0:
            current_color = entry.cget("bg")
            if current_color == color2:
                new_color = color1
            else:
                new_color = color2
            entry.config(bg=new_color)
            entry.after(interval, self.blink_entry, entry, color1, color2, count-1, interval)
        else:
            entry.config(bg='#ffffff')

            count += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = TixCart(root)
    root.mainloop()