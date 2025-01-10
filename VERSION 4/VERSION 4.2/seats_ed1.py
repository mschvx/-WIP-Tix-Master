# Importing necessary libraries
import tkinter as tk
from tkinter import Toplevel

# Fade in and fade out effects
def fade_in(tooltip, alpha=0.0):
    if alpha < 1.0:
        alpha += 0.1
        tooltip.attributes("-alpha", alpha)
        tooltip.after(10, fade_in, tooltip, alpha)

def fade_out(tooltip, alpha=1.0):
    if alpha > 0.0:
        alpha -= 0.1
        tooltip.attributes("-alpha", alpha)
        tooltip.after(10, fade_out, tooltip, alpha)
    else:
        tooltip.destroy()

# Main class for Layout - ED1 page
class ED1Layout:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Elphaba Day 1 Seats")

        # Placing the main design of the save page
        self.save_title = tk.PhotoImage(file="Designs/Layout/ED1_Layout.png")
        self.save_title_label = tk.Label(self.root, image=self.save_title)
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
        self.seat_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('1', "#798ec4"))
        self.seat_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S1.png")
        self.seat_one.place(x=293, y=339, width=62., height=62)
        self.seat_one.bind("<Enter>", self.show_seat_details)
        self.seat_one.bind("<Leave>", self.hide_seat_details)
        self.seat_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('2', "#798ec4"))
        self.seat_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S2.png")
        self.seat_two.place(x=363, y=339, width=62., height=62)
        self.seat_two.bind("<Enter>", self.show_seat_details)
        self.seat_two.bind("<Leave>", self.hide_seat_details)
        self.seat_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('3', "#798ec4"))
        self.seat_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S3.png")
        self.seat_three.place(x=433, y=339, width=62., height=62)
        self.seat_three.bind("<Enter>", self.show_seat_details)
        self.seat_three.bind("<Leave>", self.hide_seat_details)
        self.seat_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('4', "#798ec4"))
        self.seat_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S4.png")
        self.seat_four.place(x=503, y=339, width=62., height=62)
        self.seat_four.bind("<Enter>", self.show_seat_details)
        self.seat_four.bind("<Leave>", self.hide_seat_details)
        self.seat_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('5', "#798ec4"))
        self.seat_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S5.png")
        self.seat_five.place(x=573, y=339, width=62., height=62)
        self.seat_five.bind("<Enter>", self.show_seat_details)
        self.seat_five.bind("<Leave>", self.hide_seat_details)
        self.seat_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('6', "#798ec4"))
        self.seat_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S6.png")
        self.seat_six.place(x=643, y=339, width=62., height=62)
        self.seat_six.bind("<Enter>", self.show_seat_details)
        self.seat_six.bind("<Leave>", self.hide_seat_details)

        # SECOND ROW
        self.seat_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('7', "#798ec4"))
        self.seat_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S7.png")
        self.seat_seven.place(x=223, y=411, width=62., height=62)
        self.seat_seven.bind("<Enter>", self.show_seat_details)
        self.seat_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('8', "#798ec4"))
        self.seat_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S8.png")
        self.seat_eight.place(x=293, y=411, width=62., height=62)
        self.seat_eight.bind("<Enter>", self.show_seat_details)
        self.seat_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('9', "#798ec4"))
        self.seat_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S9.png")
        self.seat_nine.place(x=363, y=411, width=62., height=62)
        self.seat_nine.bind("<Enter>", self.show_seat_details)
        self.seat_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_ten = tk.Button(self.root, relief="raised", bg=seat_colors.get('10', "#798ec4"))
        self.seat_ten.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S10.png")
        self.seat_ten.place(x=433, y=411, width=62., height=62)
        self.seat_ten.bind("<Enter>", self.show_seat_details)
        self.seat_ten.bind("<Leave>", self.hide_seat_details)
        self.seat_eleven = tk.Button(self.root, relief="raised", bg=seat_colors.get('11', "#798ec4"))
        self.seat_eleven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S11.png")
        self.seat_eleven.place(x=503, y=411, width=62., height=62)
        self.seat_eleven.bind("<Enter>", self.show_seat_details)
        self.seat_eleven.bind("<Leave>", self.hide_seat_details)
        self.seat_twelve = tk.Button(self.root, relief="raised", bg=seat_colors.get('12', "#798ec4"))
        self.seat_twelve.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S12.png")
        self.seat_twelve.place(x=573, y=411, width=62., height=62)
        self.seat_twelve.bind("<Enter>", self.show_seat_details)
        self.seat_twelve.bind("<Leave>", self.hide_seat_details)
        self.seat_thirteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('13', "#798ec4"))
        self.seat_thirteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S13.png")
        self.seat_thirteen.place(x=643, y=411, width=62., height=62)
        self.seat_thirteen.bind("<Enter>", self.show_seat_details)
        self.seat_thirteen.bind("<Leave>", self.hide_seat_details)
        self.seat_fourteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('14', "#798ec4"))
        self.seat_fourteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S14.png")
        self.seat_fourteen.place(x=713, y=411, width=62., height=62)
        self.seat_fourteen.bind("<Enter>", self.show_seat_details)
        self.seat_fourteen.bind("<Leave>", self.hide_seat_details)

        # THIRD ROW
        self.seat_fifteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('15', "#798ec4"))
        self.seat_fifteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S15.png")
        self.seat_fifteen.place(x=153, y=485, width=62., height=62)
        self.seat_fifteen.bind("<Enter>", self.show_seat_details)
        self.seat_fifteen.bind("<Leave>", self.hide_seat_details)
        self.seat_sixteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('16', "#798ec4"))
        self.seat_sixteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S16.png")
        self.seat_sixteen.place(x=223, y=485, width=62., height=62)
        self.seat_sixteen.bind("<Enter>", self.show_seat_details)
        self.seat_sixteen.bind("<Leave>", self.hide_seat_details)
        self.seat_seventeen = tk.Button(self.root, relief="raised", bg=seat_colors.get('17', "#798ec4"))
        self.seat_seventeen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S17.png")
        self.seat_seventeen.place(x=293, y=485, width=62., height=62)
        self.seat_seventeen.bind("<Enter>", self.show_seat_details)
        self.seat_seventeen.bind("<Leave>", self.hide_seat_details)
        self.seat_eighteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('18', "#798ec4"))
        self.seat_eighteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S18.png")
        self.seat_eighteen.place(x=643, y=485, width=62., height=62)
        self.seat_eighteen.bind("<Enter>", self.show_seat_details)
        self.seat_eighteen.bind("<Leave>", self.hide_seat_details)
        self.seat_nineteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('19', "#798ec4"))
        self.seat_nineteen.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S19.png")
        self.seat_nineteen.place(x=713, y=485, width=62., height=62)
        self.seat_nineteen.bind("<Enter>", self.show_seat_details)
        self.seat_nineteen.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty = tk.Button(self.root, relief="raised", bg=seat_colors.get('20', "#798ec4"))
        self.seat_twenty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S20.png")
        self.seat_twenty.place(x=783, y=485, width=62., height=62)
        self.seat_twenty.bind("<Enter>", self.show_seat_details)
        self.seat_twenty.bind("<Leave>", self.hide_seat_details)

        # LEFT SIDE
        self.seat_twenty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('21', "#798ec4"))
        self.seat_twenty_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S21.png")
        self.seat_twenty_one.place(x=13, y=263, width=62., height=62)
        self.seat_twenty_one.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_one.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('22', "#798ec4"))
        self.seat_twenty_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S22.png")
        self.seat_twenty_two.place(x=83, y=263, width=62., height=62)
        self.seat_twenty_two.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_two.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('23', "#798ec4"))
        self.seat_twenty_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S23.png")
        self.seat_twenty_three.place(x=13, y=337, width=62., height=62)
        self.seat_twenty_three.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_three.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('24', "#798ec4"))
        self.seat_twenty_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S24.png")
        self.seat_twenty_four.place(x=83, y=337, width=62., height=62)
        self.seat_twenty_four.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_four.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('25', "#798ec4"))
        self.seat_twenty_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S25.png")
        self.seat_twenty_five.place(x=13, y=411, width=62., height=62)
        self.seat_twenty_five.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_five.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('26', "#798ec4"))
        self.seat_twenty_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S26.png")
        self.seat_twenty_six.place(x=83, y=411, width=62., height=62)
        self.seat_twenty_six.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_six.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('27', "#798ec4"))
        self.seat_twenty_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S27.png")
        self.seat_twenty_seven.place(x=13, y=485, width=62., height=62)
        self.seat_twenty_seven.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('28', "#798ec4"))
        self.seat_twenty_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S28.png")
        self.seat_twenty_eight.place(x=83, y=485, width=62., height=62)
        self.seat_twenty_eight.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_twenty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('29', "#798ec4"))
        self.seat_twenty_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S29.png")
        self.seat_twenty_nine.place(x=13, y=559, width=62., height=62)
        self.seat_twenty_nine.bind("<Enter>", self.show_seat_details)
        self.seat_twenty_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty = tk.Button(self.root, relief="raised", bg=seat_colors.get('30', "#798ec4"))
        self.seat_thirty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S30.png")
        self.seat_thirty.place(x=83, y=559, width=62., height=62)
        self.seat_thirty.bind("<Enter>", self.show_seat_details)
        self.seat_thirty.bind("<Leave>", self.hide_seat_details)

        # RIGHT SIDE
        self.seat_thirty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('31', "#798ec4"))
        self.seat_thirty_one.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S31.png")
        self.seat_thirty_one.place(x=853, y=263, width=62., height=62)
        self.seat_thirty_one.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_one.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('32', "#798ec4"))
        self.seat_thirty_two.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S32.png")
        self.seat_thirty_two.place(x=923, y=263, width=62., height=62)
        self.seat_thirty_two.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_two.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('33', "#798ec4"))
        self.seat_thirty_three.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S33.png")
        self.seat_thirty_three.place(x=853, y=337, width=62., height=62)
        self.seat_thirty_three.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_three.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('34', "#798ec4"))
        self.seat_thirty_four.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S34.png")
        self.seat_thirty_four.place(x=923, y=337, width=62., height=62)
        self.seat_thirty_four.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_four.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('35', "#798ec4"))
        self.seat_thirty_five.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S35.png")
        self.seat_thirty_five.place(x=853, y=411, width=62., height=62)
        self.seat_thirty_five.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_five.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('36', "#798ec4"))
        self.seat_thirty_six.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S36.png")
        self.seat_thirty_six.place(x=923, y=411, width=62., height=62)
        self.seat_thirty_six.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_six.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('37', "#798ec4"))
        self.seat_thirty_seven.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S37.png")
        self.seat_thirty_seven.place(x=853, y=485, width=62., height=62)
        self.seat_thirty_seven.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_seven.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('38', "#798ec4"))
        self.seat_thirty_eight.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S38.png")
        self.seat_thirty_eight.place(x=923, y=485, width=62., height=62)
        self.seat_thirty_eight.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_eight.bind("<Leave>", self.hide_seat_details)
        self.seat_thirty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('39', "#798ec4"))
        self.seat_thirty_nine.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S39.png")
        self.seat_thirty_nine.place(x=853, y=559, width=62., height=62)
        self.seat_thirty_nine.bind("<Enter>", self.show_seat_details)
        self.seat_thirty_nine.bind("<Leave>", self.hide_seat_details)
        self.seat_forty = tk.Button(self.root, relief="raised", bg=seat_colors.get('40', "#798ec4"))
        self.seat_forty.image = tk.PhotoImage(file="Designs/Layout/Tooltip/S40.png")
        self.seat_forty.place(x=923, y=559, width=62., height=62)
        self.seat_forty.bind("<Enter>", self.show_seat_details)
        self.seat_forty.bind("<Leave>", self.hide_seat_details)

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
        self.exit_button = tk.Button(self.root, image=self.exit, relief="raised")
        self.exit_button.image = self.exit
        self.exit_button.place(x=570, y=640, anchor="center")
        self.exit_hover = tk.PhotoImage(file="Designs/Layout/Exit_Button_Hover.png")
        self.exit_button.bind("<Enter>", self.on_hover_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)
        self.exit_button.image = self.exit_hover

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
            tooltip.geometry(f"+{widget.winfo_rootx()}+{widget.winfo_rooty() - widget.winfo_height() - 80}")
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ED1Layout(root)
    root.mainloop()