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

        # Initializing empty variables for later use
        self.concert_name = ''
        self.name = ''
        self.seat_numbers_text = ''
        self.seat_details_text = ''
        self.price_text = ''

        # Placing the main design of the catalogue page
        self.ticket_title = tk.PhotoImage(file="Designs/Ticket/Tix_Ticket.png")
        self.ticket_canvas = tk.Canvas(self.root, width=1000, height=700)
        self.ticket_canvas.pack()
        self.ticket_canvas.create_image(0, 0, anchor="nw", image=self.ticket_title)

        # Placing the return button
        self.back = tk.PhotoImage(file="Designs/Ticket/Return_Button.png")
        self.back_button = tk.Button(self.root, image=self.back, relief="raised", command=self.open_title)
        self.back_button.image = self.back
        self.back_button.place(x=830, y=625, anchor="center")
        self.back_hover = tk.PhotoImage(file="Designs/Ticket/Return_Button_Hover.png")
        self.back_button.bind("<Enter>", self.on_hover_back)
        self.back_button.bind("<Leave>", self.on_leave_back)
        self.back_button.image = self.back_hover

        # Loading cart
        self.load_cart()

        # Placing the main concert name above the ticket
        self.queue_message = self.ticket_canvas.create_text(360, 271, text=f"Ticket for {self.concert_name} Concert", font=("Helvetica", 20, "bold"), fill="#151c4c", anchor="center") # anchor center like center alignment in ms word

        # Placing the reference ID
        self.ref_id = self.ticket_canvas.create_text(360, 350, text="Reference ID #", font=("Helvetica", 20, "bold"), fill="#151c4c", anchor="center")

        # Placing the customer name
        self.ticket_holder = self.ticket_canvas.create_text(240, 396, text=f"{self.name}", font=("Helvetica", 18, "bold"), fill="#edebe7", anchor="w") # align left
    
        # Placing seat num
        self.seat_numbers = self.ticket_canvas.create_text(250, 435, text=self.seat_numbers_text, font=("Helvetica", 18, "bold"), fill="#edebe7", anchor="w") # align left

        # Placing seat details
        self.seat_details = self.ticket_canvas.create_text(225, 475, text=self.seat_details_text, font=("Helvetica", 18, "bold"), fill="#edebe7", anchor="w") # align left

        # Placing price
        self.price = self.ticket_canvas.create_text(135, 516, text=self.price_text, font=("Helvetica", 18, "bold"), fill="#edebe7", anchor="w") # align left

        # Placing Glinda's picture
        if self.concert_name == "Glinda - Day 1" or self.concert_name == "Glinda - Day 2":
            self.glinda_image = tk.PhotoImage(file="Designs/Ticket/Glinda_Ticket.png")
            self.glinda_image_label = tk.Label(self.root, image=self.glinda_image, bg="#d9e2f1")
            self.glinda_image_label.image = self.glinda_image
            self.glinda_image_label.place(x=840, y=330, anchor="center")

        # Placing Elphaba's picture
        if self.concert_name == "Elphaba - Day 1" or self.concert_name == "Elphaba - Day 2":
            self.elphaba_image = tk.PhotoImage(file="Designs/Ticket/Elphaba_Ticket.png")
            self.elphaba_image_label = tk.Label(self.root, image=self.elphaba_image, bg="#d9e2f1")
            self.elphaba_image_label.image = self.elphaba_image
            self.elphaba_image_label.place(x=840, y=330, anchor="center")

    # Series of functions for the hover effects of each button
    def on_hover_back(self, event):
        self.back_button.config(image=self.back_hover)

    def on_leave_back(self, event):
        self.back_button.config(image=self.back)

    # Function for restarting (yay!) going back to the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.ticket_canvas.pack_forget()  # Remove the canvas before transitioning
        TixMaster(self.root)
    
    # Function for loading the cart
    def load_cart(self):
        with open("tix_cart.dat", "r") as tixCart:
            load = tixCart.readlines()
            self.concert_name = load[0].strip()
            self.items = []

            for line in load[1:-1]:
                seat_number, rest = line.strip().split(' - ')
                seat_detail, price = rest.split(':')
                if seat_detail == "Lower Box":
                    seat_detail = "LB"
                if seat_detail == "Upper Box":
                    seat_detail == "UB"
                if seat_detail == "Right Balcony":
                    seat_detail = "RB"
                if seat_detail == "Left Balcony":
                    seat_detail = "LB"
                self.items.append({
                    'seat_number': seat_number,
                    'seat_detail': seat_detail,
                    'price': int(price)
                })

            self.name = load[-1].strip() # Get last line (name)

        # Extracting seat numbers, details, and total price
        self.seat_numbers_text = ", ".join([item['seat_number'] for item in self.items])
        self.seat_details_text = ", ".join([item['seat_detail'] for item in self.items])
        self.price_text = "₱" + str(sum(item['price'] for item in self.items))


if __name__ == "__main__":
    root = tk.Tk()
    app = tixTicket(root)
    root.mainloop()