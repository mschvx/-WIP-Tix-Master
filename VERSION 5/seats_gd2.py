# Importing necessary libraries
import tkinter as tk
from tkinter import Toplevel

# Fade in and fade out effects
def fade_in(widget, alpha=0.0):
    if alpha < 1.0:
        alpha += 0.1
        widget.attributes("-alpha", alpha)
        widget.after(10, fade_in, widget, alpha)

def fade_out(widget, alpha=1.0):
    if alpha > 0.0:
        alpha -= 0.1
        widget.attributes("-alpha", alpha)
        widget.after(10, fade_out, widget, alpha)
    else:
        widget.destroy()

def fade_in_notif(toplevel, alpha=0):
    if alpha < 1.0:  # Increment alpha until it reaches 1.0
        alpha += 0.05
        toplevel.attributes("-alpha", alpha)
        toplevel.after(10, fade_in_notif, toplevel, alpha)  # Schedule next fade-in step
    else:
        toplevel.after(1000, lambda: fade_out_notif(toplevel))  # Start fading out after 2 seconds

def fade_out_notif(toplevel, alpha=1.0):
    if alpha > 0:  # Decrease alpha until it reaches 0
        alpha -= 0.05
        toplevel.attributes("-alpha", alpha)
        toplevel.after(10, fade_out_notif, toplevel, alpha)  # Schedule next fade-out step
    else:
        toplevel.withdraw()  # Hide the toplevel once fully invisible


# Main class for Layout - GD2 page
class GD2Layout:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#d9e2f1")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Glinda Day 2 Seats")

        # Placing the main design of the save page
        self.save_title = tk.PhotoImage(file="Designs/Layout/GD2_Layout.png")
        self.save_title_label = tk.Label(self.root, image=self.save_title, bg="#d9e2f1")
        self.save_title_label.image = self.save_title
        self.save_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Loading the value of each assigned seat from the database
        with open("assigned_seats.dat", "r") as assignedSeats:
            seats_dictionary = assignedSeats.read()
            seats = seats_dictionary.strip('{}')
            assigned_seats = seats.split(",")

            seat_colors = {}
            for i in assigned_seats:
                seat_number, value = i.split(':')
                seat_number = seat_number.strip()
                value = value.strip()
                if value == 'True':
                    seat_colors[seat_number] = "#edebe7"

        # Placing the 40 seats/buttons !!! (warning: a lot)
        # FIRST ROW
        self.seat_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('1', "#798ec4"), activebackground="#edebe7")
        self.seat_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S1.png")
        self.seat_one.place(x=293, y=339, width=62., height=62)
        self.seat_one_color = self.seat_one.cget("bg")
        self.seat_one.bind("<Enter>", self.show_seat_details)
        self.seat_one.bind("<Leave>", self.hide_seat_details)
        self.seat_one.config(command=lambda: self.check_to_cart(self.seat_one))
        self.seat_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('2', "#798ec4"), activebackground="#edebe7")
        self.seat_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S2.png")
        self.seat_two.place(x=363, y=339, width=62., height=62)
        self.seat_two_color = self.seat_two.cget("bg")
        self.seat_two.bind("<Enter>", self.show_seat_details)
        self.seat_two.bind("<Leave>", self.hide_seat_details)
        self.seat_two.config(command=lambda: self.check_to_cart(self.seat_two))
        self.seat_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('3', "#798ec4"), activebackground="#edebe7")
        self.seat_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S3.png")
        self.seat_three.place(x=433, y=339, width=62., height=62)
        self.seat_three_color = self.seat_three.cget("bg")
        self.seat_three.bind("<Enter>", self.show_seat_details)
        self.seat_three.bind("<Leave>", self.hide_seat_details)
        self.seat_three.config(command=lambda: self.check_to_cart(self.seat_three))
        self.seat_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('4', "#798ec4"), activebackground="#edebe7")
        self.seat_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S4.png")
        self.seat_four.place(x=503, y=339, width=62., height=62)
        self.seat_four_color = self.seat_four.cget("bg")
        self.seat_four.bind("<Enter>", self.show_seat_details)
        self.seat_four.bind("<Leave>", self.hide_seat_details)
        self.seat_four.config(command=lambda: self.check_to_cart(self.seat_four))
        self.seat_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('5', "#798ec4"), activebackground="#edebe7")
        self.seat_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S5.png")
        self.seat_five.place(x=573, y=339, width=62., height=62)
        self.seat_five_color = self.seat_five.cget("bg")
        self.seat_five.bind("<Enter>", self.show_seat_details)
        self.seat_five.bind("<Leave>", self.hide_seat_details)
        self.seat_five.config(command=lambda: self.check_to_cart(self.seat_five))
        self.seat_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('6', "#798ec4"), activebackground="#edebe7")
        self.seat_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S6.png")
        self.seat_six.place(x=643, y=339, width=62., height=62)
        self.seat_six_color = self.seat_six.cget("bg")
        self.seat_six.bind("<Enter>", self.show_seat_details)
        self.seat_six.bind("<Leave>", self.hide_seat_details)
        self.seat_six.config(command=lambda: self.check_to_cart(self.seat_six))

        # SECOND ROW
        self.seat_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('7', "#798ec4"), activebackground="#edebe7")
        self.seat_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S7.png")
        self.seat_seven.place(x=223, y=411, width=62., height=62)
        self.seat_seven_color = self.seat_seven.cget("bg")
        self.seat_seven.bind("<Enter>", self.show_seat_details)
        self.seat_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_seven.config(command=lambda: self.check_to_cart(self.seat_seven))
        self.seat_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('8', "#798ec4"), activebackground="#edebe7")
        self.seat_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S8.png")
        self.seat_eight.place(x=293, y=411, width=62., height=62)
        self.seat_eight_color = self.seat_eight.cget("bg")
        self.seat_eight.bind("<Enter>", self.show_seat_details)
        self.seat_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_eight.config(command=lambda: self.check_to_cart(self.seat_eight))
        self.seat_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('9', "#798ec4"), activebackground="#edebe7")
        self.seat_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S9.png")
        self.seat_nine.place(x=363, y=411, width=62., height=62)
        self.seat_nine_color = self.seat_nine.cget("bg")
        self.seat_nine.bind("<Enter>", self.show_seat_details)
        self.seat_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_nine.config(command=lambda: self.check_to_cart(self.seat_nine))
        self.seat_ten = tk.Button(self.root, relief="raised", bg=seat_colors.get('10', "#798ec4"), activebackground="#edebe7")
        self.seat_ten.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S10.png")
        self.seat_ten.place(x=433, y=411, width=62., height=62)
        self.seat_ten_color = self.seat_ten.cget("bg")
        self.seat_ten.bind("<Enter>", self.show_seat_details)
        self.seat_ten.bind("<Leave>", self.hide_seat_details)
        self.seat_ten.config(command=lambda: self.check_to_cart(self.seat_ten))
        self.seat_eleven = tk.Button(self.root, relief="raised", bg=seat_colors.get('11', "#798ec4"), activebackground="#edebe7")
        self.seat_eleven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S11.png")
        self.seat_eleven.place(x=503, y=411, width=62., height=62)
        self.seat_eleven_color = self.seat_eleven.cget("bg")
        self.seat_eleven.bind("<Enter>", self.show_seat_details)
        self.seat_eleven.bind("<Leave>", self.hide_seat_details)
        self.seat_eleven.config(command=lambda: self.check_to_cart(self.seat_eleven))
        self.seat_twelve = tk.Button(self.root, relief="raised", bg=seat_colors.get('12', "#798ec4"), activebackground="#edebe7")
        self.seat_twelve.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S12.png")
        self.seat_twelve.place(x=573, y=411, width=62., height=62)
        self.seat_twelve_color = self.seat_twelve.cget("bg")
        self.seat_twelve.bind("<Enter>", self.show_seat_details)
        self.seat_twelve.bind("<Leave>", self.hide_seat_details)
        self.seat_twelve.config(command=lambda: self.check_to_cart(self.seat_twelve))
        self.seat_thirteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('13', "#798ec4"), activebackground="#edebe7")
        self.seat_thirteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S13.png")
        self.seat_thirteen.place(x=643, y=411, width=62., height=62)
        self.seat_thirteen_color = self.seat_thirteen.cget("bg")
        self.seat_thirteen.bind("<Enter>", self.show_seat_details)
        self.seat_thirteen.bind("<Leave>", self.hide_seat_details)
        self.seat_thirteen.config(command=lambda: self.check_to_cart(self.seat_thirteen))
        self.seat_fourteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('14', "#798ec4"), activebackground="#edebe7")
        self.seat_fourteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S14.png")
        self.seat_fourteen.place(x=713, y=411, width=62., height=62)
        self.seat_fourteen_color = self.seat_fourteen.cget("bg")
        self.seat_fourteen.bind("<Enter>", self.show_seat_details)
        self.seat_fourteen.bind("<Leave>", self.hide_seat_details)
        self.seat_fourteen.config(command=lambda: self.check_to_cart(self.seat_fourteen))

        # THIRD ROW
        self.seat_fifteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('15', "#798ec4"), activebackground="#edebe7")
        self.seat_fifteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S15.png")
        self.seat_fifteen.place(x=153, y=485, width=62., height=62)
        self.seat_fifteen_color = self.seat_fifteen.cget("bg")
        self.seat_fifteen.bind("<Enter>", self.show_seat_details)
        self.seat_fifteen.bind("<Leave>", self.hide_seat_details)
        self.seat_fifteen.config(command=lambda: self.check_to_cart(self.seat_fifteen))
        self.seat_sixteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('16', "#798ec4"), activebackground="#edebe7")
        self.seat_sixteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S16.png")
        self.seat_sixteen.place(x=223, y=485, width=62., height=62)
        self.seat_sixteen_color = self.seat_sixteen.cget("bg")
        self.seat_sixteen.bind("<Enter>", self.show_seat_details)
        self.seat_sixteen.bind("<Leave>", self.hide_seat_details)
        self.seat_sixteen.config(command=lambda: self.check_to_cart(self.seat_sixteen))
        self.seat_seventeen = tk.Button(self.root, relief="raised", bg=seat_colors.get('17', "#798ec4"), activebackground="#edebe7")
        self.seat_seventeen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S17.png")
        self.seat_seventeen.place(x=293, y=485, width=62., height=62)
        self.seat_seventeen_color = self.seat_seventeen.cget("bg")
        self.seat_seventeen.bind("<Enter>", self.show_seat_details)
        self.seat_seventeen.bind("<Leave>", self.hide_seat_details)
        self.seat_seventeen.config(command=lambda: self.check_to_cart(self.seat_seventeen))
        self.seat_eighteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('18', "#798ec4"), activebackground="#edebe7")
        self.seat_eighteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S18.png")
        self.seat_eighteen.place(x=643, y=485, width=62., height=62)
        self.seat_eighteen_color = self.seat_eighteen.cget("bg")
        self.seat_eighteen.bind("<Enter>", self.show_seat_details)
        self.seat_eighteen.bind("<Leave>", self.hide_seat_details)
        self.seat_eighteen.config(command=lambda: self.check_to_cart(self.seat_eighteen))
        self.seat_nineteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('19', "#798ec4"), activebackground="#edebe7")
        self.seat_nineteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S19.png")
        self.seat_nineteen.place(x=713, y=485, width=62., height=62)
        self.seat_nineteen_color = self.seat_nineteen.cget("bg")
        self.seat_nineteen.bind("<Enter>", self.show_seat_details)
        self.seat_nineteen.bind("<Leave>", self.hide_seat_details)
        self.seat_nineteen.config(command=lambda: self.check_to_cart(self.seat_nineteen))
        self.seat_twenty = tk.Button(self.root, relief="raised", bg=seat_colors.get('20', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S20.png")
        self.seat_twenty.place(x=783, y=485, width=62., height=62)
        self.seat_twenty_color = self.seat_twenty.cget("bg")
        self.seat_twenty.bind("<Enter>", self.show_seat_details)
        self.seat_twenty.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty.config(command=lambda: self.check_to_cart(self.seat_twenty))

        # LEFT SIDE
        self.seat_twenty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('21', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S21.png")
        self.seat_twenty_one.place(x=13, y=263, width=62., height=62)
        self.seat_twenty_one_color = self.seat_twenty_one.cget("bg")
        self.seat_twenty_one.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_one.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_one.config(command=lambda: self.check_to_cart(self.seat_twenty_one))
        self.seat_twenty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('22', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S22.png")
        self.seat_twenty_two.place(x=83, y=263, width=62., height=62)
        self.seat_twenty_two_color = self.seat_twenty_two.cget("bg")
        self.seat_twenty_two.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_two.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_two.config(command=lambda: self.check_to_cart(self.seat_twenty_two))
        self.seat_twenty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('23', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S23.png")
        self.seat_twenty_three.place(x=13, y=337, width=62., height=62)
        self.seat_twenty_three_color = self.seat_twenty_three.cget("bg")
        self.seat_twenty_three.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_three.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_three.config(command=lambda: self.check_to_cart(self.seat_twenty_three))
        self.seat_twenty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('24', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S24.png")
        self.seat_twenty_four.place(x=83, y=337, width=62., height=62)
        self.seat_twenty_four_color = self.seat_twenty_four.cget("bg")
        self.seat_twenty_four.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_four.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_four.config(command=lambda: self.check_to_cart(self.seat_twenty_four))
        self.seat_twenty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('25', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S25.png")
        self.seat_twenty_five.place(x=13, y=411, width=62., height=62)
        self.seat_twenty_five_color = self.seat_twenty_five.cget("bg")
        self.seat_twenty_five.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_five.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_five.config(command=lambda: self.check_to_cart(self.seat_twenty_five))
        self.seat_twenty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('26', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S26.png")
        self.seat_twenty_six.place(x=83, y=411, width=62., height=62)
        self.seat_twenty_six_color = self.seat_twenty_six.cget("bg")
        self.seat_twenty_six.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_six.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_six.config(command=lambda: self.check_to_cart(self.seat_twenty_six))
        self.seat_twenty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('27', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S27.png")
        self.seat_twenty_seven.place(x=13, y=485, width=62., height=62)
        self.seat_twenty_seven_color = self.seat_twenty_seven.cget("bg")
        self.seat_twenty_seven.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_seven.config(command=lambda: self.check_to_cart(self.seat_twenty_seven))
        self.seat_twenty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('28', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S28.png")
        self.seat_twenty_eight.place(x=83, y=485, width=62., height=62)
        self.seat_twenty_eight_color = self.seat_twenty_eight.cget("bg")
        self.seat_twenty_eight.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_eight.config(command=lambda: self.check_to_cart(self.seat_twenty_eight))
        self.seat_twenty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('29', "#798ec4"), activebackground="#edebe7")
        self.seat_twenty_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S29.png")
        self.seat_twenty_nine.place(x=13, y=559, width=62., height=62)
        self.seat_twenty_nine_color = self.seat_twenty_nine.cget("bg")
        self.seat_twenty_nine.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_nine.config(command=lambda: self.check_to_cart(self.seat_twenty_nine))
        self.seat_thirty = tk.Button(self.root, relief="raised", bg=seat_colors.get('30', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S30.png")
        self.seat_thirty.place(x=83, y=559, width=62., height=62)
        self.seat_thirty_color = self.seat_thirty.cget("bg")
        self.seat_thirty.bind("<Enter>", self.show_seat_details)
        self.seat_thirty.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty.config(command=lambda: self.check_to_cart(self.seat_thirty))

        # RIGHT SIDE
        self.seat_thirty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('31', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S31.png")
        self.seat_thirty_one.place(x=853, y=263, width=62., height=62)
        self.seat_thirty_one_color = self.seat_thirty_one.cget("bg")
        self.seat_thirty_one.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_one.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_one.config(command=lambda: self.check_to_cart(self.seat_thirty_one))
        self.seat_thirty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('32', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S32.png")
        self.seat_thirty_two.place(x=923, y=263, width=62., height=62)
        self.seat_thirty_two_color = self.seat_thirty_two.cget("bg")
        self.seat_thirty_two.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_two.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_two.config(command=lambda: self.check_to_cart(self.seat_thirty_two))
        self.seat_thirty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('33', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S33.png")
        self.seat_thirty_three.place(x=853, y=337, width=62., height=62)
        self.seat_thirty_three_color = self.seat_thirty_three.cget("bg")
        self.seat_thirty_three.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_three.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_three.config(command=lambda: self.check_to_cart(self.seat_thirty_three))
        self.seat_thirty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('34', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S34.png")
        self.seat_thirty_four.place(x=923, y=337, width=62., height=62)
        self.seat_thirty_four_color = self.seat_thirty_four.cget("bg")
        self.seat_thirty_four.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_four.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_four.config(command=lambda: self.check_to_cart(self.seat_thirty_four))
        self.seat_thirty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('35', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S35.png")
        self.seat_thirty_five.place(x=853, y=411, width=62., height=62)
        self.seat_thirty_five_color = self.seat_thirty_five.cget("bg")
        self.seat_thirty_five.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_five.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_five.config(command=lambda: self.check_to_cart(self.seat_thirty_five))
        self.seat_thirty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('36', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S36.png")
        self.seat_thirty_six.place(x=923, y=411, width=62., height=62)
        self.seat_thirty_six_color = self.seat_thirty_six.cget("bg")
        self.seat_thirty_six.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_six.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_six.config(command=lambda: self.check_to_cart(self.seat_thirty_six))
        self.seat_thirty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('37', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S37.png")
        self.seat_thirty_seven.place(x=853, y=485, width=62., height=62)
        self.seat_thirty_seven_color = self.seat_thirty_seven.cget("bg")
        self.seat_thirty_seven.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_seven.config(command=lambda: self.check_to_cart(self.seat_thirty_seven))
        self.seat_thirty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('38', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S38.png")
        self.seat_thirty_eight.place(x=923, y=485, width=62., height=62)
        self.seat_thirty_eight_color = self.seat_thirty_eight.cget("bg")
        self.seat_thirty_eight.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_eight.config(command=lambda: self.check_to_cart(self.seat_thirty_eight))
        self.seat_thirty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('39', "#798ec4"), activebackground="#edebe7")
        self.seat_thirty_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S39.png")
        self.seat_thirty_nine.place(x=853, y=559, width=62., height=62)
        self.seat_thirty_nine_color = self.seat_thirty_nine.cget("bg")
        self.seat_thirty_nine.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_nine.config(command=lambda: self.check_to_cart(self.seat_thirty_nine))
        self.seat_forty = tk.Button(self.root, relief="raised", bg=seat_colors.get('40', "#798ec4"), activebackground="#edebe7")
        self.seat_forty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S40.png")
        self.seat_forty.place(x=923, y=559, width=62., height=62)
        self.seat_forty_color = self.seat_forty.cget("bg")
        self.seat_forty.bind("<Enter>", self.show_seat_details)
        self.seat_forty.bind("<Leave>", self.hide_seat_details)
        self.seat_forty.config(command=lambda: self.check_to_cart(self.seat_forty))

        # Placing the finalize button
        self.finalize = tk.PhotoImage(file="Designs/Layout/Finalize_Button.png")
        self.finalize_button = tk.Button(self.root, image=self.finalize, relief="raised")
        self.finalize_button.image = self.finalize
        self.finalize_button.place(x=420, y=640, anchor="center")
        self.finalize_hover = tk.PhotoImage(file="Designs/Layout/Finalize_Button_Hover.png")
        self.finalize_button.bind("<Enter>", self.on_hover_finalize)
        self.finalize_button.bind("<Leave>", self.on_leave_finalize)
        self.finalize_button.image = self.finalize_hover

        # Placing the exit button
        self.exit = tk.PhotoImage(file="Designs/Layout/Exit_Button.png")
        self.exit_button = tk.Button(self.root, image=self.exit, relief="raised", command=self.open_title)
        self.exit_button.image = self.exit
        self.exit_button.place(x=570, y=640, anchor="center")
        self.exit_hover = tk.PhotoImage(file="Designs/Layout/Exit_Button_Hover.png")
        self.exit_button.bind("<Enter>", self.on_hover_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)
        self.exit_button.image = self.exit_hover

        # Placing the notification messages
        self.seat_added = tk.PhotoImage(file="Designs/Layout/Seat_Added_Message.png")
        self.seat_added_label = tk.Label(self.root, image=self.seat_added)
        self.seat_added_label.image = self.seat_added
        self.seat_added_label.place_forget() # Hide the label at start

        self.seat_error = tk.PhotoImage(file="Designs/Layout/Seat_Error_Message.png")
        self.seat_error_toplevel = Toplevel(self.root)
        self.seat_error_toplevel.wm_overrideredirect(True)
        self.seat_error_toplevel.geometry("+730+635")
        self.seat_error_toplevel.attributes("-alpha", 0.0)
        self.seat_error_label = tk.Label(self.seat_error_toplevel, image=self.seat_error)
        self.seat_error_label.pack()

    # Series of functions for the hover effects of each button
    def on_hover_finalize(self, event):
        self.finalize_button.config(image=self.finalize_hover)
    
    def on_leave_finalize(self, event):
        self.finalize_button.config(image=self.finalize)

    def on_hover_exit(self, event):
        self.exit_button.config(image=self.exit_hover)

    def on_leave_exit(self, event):
        self.exit_button.config(image=self.exit)

    # Series of functions for the tooltip effect appearing/disappearing
    def show_seat_details(self, event):
        widget = event.widget
        tooltip = Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        
        # Determine tooltip position based on seat location
        # ROWS
        if widget in [self.seat_one, self.seat_two, self.seat_three, self.seat_four, self.seat_five, self.seat_six,
                    self.seat_seven, self.seat_eight, self.seat_nine, self.seat_ten, self.seat_eleven, self.seat_twelve,
                    self.seat_thirteen, self.seat_fourteen, self.seat_fifteen, self.seat_sixteen, self.seat_seventeen,
                    self.seat_eighteen, self.seat_nineteen, self.seat_twenty]:
            tooltip.geometry(f"+{widget.winfo_rootx() - 80}+{widget.winfo_rooty() - widget.winfo_height() - 80}")
        # RIGHT
        elif widget in [self.seat_thirty_one, self.seat_thirty_two, self.seat_thirty_three, self.seat_thirty_four,
                        self.seat_thirty_five, self.seat_thirty_six, self.seat_thirty_seven, self.seat_thirty_eight,
                        self.seat_thirty_nine, self.seat_forty]:
            tooltip.geometry(f"+{widget.winfo_rootx() - widget.winfo_width() - 180}+{widget.winfo_rooty()}")
        # LEFT
        else:
            tooltip.geometry(f"+{widget.winfo_rootx() + widget.winfo_width() + 10}+{widget.winfo_rooty()}")
                
        tooltip.attributes("-alpha", 0.0)
        tk.Label(tooltip, image=widget.image, bg="#798ec4", fg="black", padx=5, pady=3).pack()
        fade_in(tooltip)
        widget.tooltip = tooltip

    def hide_seat_details(self, event):
        widget = event.widget
        if hasattr(widget, "tooltip"):
            tooltip = widget.tooltip
            fade_out(tooltip)
            del widget.tooltip

    # Series of functions for the notification messages
    def show_added_message(self):
        self.seat_added_toplevel = Toplevel(self.root)
        self.seat_added_toplevel.wm_overrideredirect(True)
        x = self.root.winfo_rootx() + self.root.winfo_width() // 2 - 125 + 360
        y = self.root.winfo_rooty() + self.root.winfo_height() // 2 - 22 + 310
        self.seat_added_toplevel.geometry(f"250x45+{x}+{y}")  # Set size and position
        self.seat_added_toplevel.attributes("-alpha", 0.0)
        self.seat_added_toplevel.config(highlightthickness=2, highlightbackground="#ccd9f3") 
        tk.Label(self.seat_added_toplevel, image=self.seat_added).pack()
        fade_in_notif(self.seat_added_toplevel)

    def show_error_message(self):
        self.seat_error_toplevel = Toplevel(self.root)
        self.seat_error_toplevel.wm_overrideredirect(True)
        x = self.root.winfo_rootx() + self.root.winfo_width() // 2 - 125 + 360 # x axis
        y = self.root.winfo_rooty() + self.root.winfo_height() // 2 - 22 + 310 # y axis
        self.seat_error_toplevel.geometry(f"250x45+{x}+{y}")  # Set size and position
        self.seat_error_toplevel.attributes("-alpha", 0.0)
        self.seat_error_toplevel.config(highlightthickness=2, highlightbackground="#ccd9f3") 
        tk.Label(self.seat_error_toplevel, image=self.seat_error).pack()
        fade_in_notif(self.seat_error_toplevel)

    # Function of the logic of adding a seat to a cart
    def check_to_cart(self, seat):
        if seat.cget("bg") == "#798ec4":
            self.show_added_message()
            print('added')
        else:
            self.show_error_message()
            print('this seat already taken')

    # Function for opening the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.save_title_label.place_forget()
        TixMaster(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = GD2Layout(root)
    root.mainloop()