# Importing necessary libraries
import tkinter as tk

# Main class for Layout - GD2 page
class GD2Layout:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Glinda Day 2 Seats")

        # Placing the main design of the save page
        self.save_title = tk.PhotoImage(file="Designs/Layout/GD2_Layout.png")
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
        self.seat_one.place(x=293, y=339, width=62., height=62)
        self.seat_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('2', "#798ec4"))
        self.seat_two.place(x=363, y=339, width=62., height=62)
        self.seat_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('3', "#798ec4"))
        self.seat_three.place(x=433, y=339, width=62., height=62)
        self.seat_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('4', "#798ec4"))
        self.seat_four.place(x=503, y=339, width=62., height=62)
        self.seat_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('5', "#798ec4"))
        self.seat_five.place(x=573, y=339, width=62., height=62)
        self.seat_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('6', "#798ec4"))
        self.seat_six.place(x=643, y=339, width=62., height=62)

        # SECOND ROW
        self.seat_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('7', "#798ec4"))
        self.seat_seven.place(x=223, y=411, width=62., height=62)
        self.seat_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('8', "#798ec4"))
        self.seat_eight.place(x=293, y=411, width=62., height=62)
        self.seat_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('9', "#798ec4"))
        self.seat_nine.place(x=363, y=411, width=62., height=62)
        self.seat_ten = tk.Button(self.root, relief="raised", bg=seat_colors.get('10', "#798ec4"))
        self.seat_ten.place(x=433, y=411, width=62., height=62)
        self.seat_eleven = tk.Button(self.root, relief="raised", bg=seat_colors.get('11', "#798ec4"))
        self.seat_eleven.place(x=503, y=411, width=62., height=62)
        self.seat_twelve = tk.Button(self.root, relief="raised", bg=seat_colors.get('12', "#798ec4"))
        self.seat_twelve.place(x=573, y=411, width=62., height=62)
        self.seat_thirteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('13', "#798ec4"))
        self.seat_thirteen.place(x=643, y=411, width=62., height=62)
        self.seat_fourteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('14', "#798ec4"))
        self.seat_fourteen.place(x=713, y=411, width=62., height=62)

        # THIRD ROW
        self.seat_fifteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('15', "#798ec4"))
        self.seat_fifteen.place(x=153, y=485, width=62., height=62)
        self.seat_sixteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('16', "#798ec4"))
        self.seat_sixteen.place(x=223, y=485, width=62., height=62)
        self.seat_seventeen = tk.Button(self.root, relief="raised", bg=seat_colors.get('17', "#798ec4"))
        self.seat_seventeen.place(x=293, y=485, width=62., height=62)
        self.seat_eighteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('18', "#798ec4"))
        self.seat_eighteen.place(x=643, y=485, width=62., height=62)
        self.seat_nineteen = tk.Button(self.root, relief="raised", bg=seat_colors.get('19', "#798ec4"))
        self.seat_nineteen.place(x=713, y=485, width=62., height=62)
        self.seat_twenty = tk.Button(self.root, relief="raised", bg=seat_colors.get('20', "#798ec4"))
        self.seat_twenty.place(x=783, y=485, width=62., height=62)

        # LEFT SIDE
        self.seat_twenty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('21', "#798ec4"))
        self.seat_twenty_one.place(x=13, y=263, width=62., height=62)
        self.seat_twenty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('22', "#798ec4"))
        self.seat_twenty_two.place(x=83, y=263, width=62., height=62)
        self.seat_twenty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('23', "#798ec4"))
        self.seat_twenty_three.place(x=13, y=337, width=62., height=62)
        self.seat_twenty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('24', "#798ec4"))
        self.seat_twenty_four.place(x=83, y=337, width=62., height=62)
        self.seat_twenty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('25', "#798ec4"))
        self.seat_twenty_five.place(x=13, y=411, width=62., height=62)
        self.seat_twenty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('26', "#798ec4"))
        self.seat_twenty_six.place(x=83, y=411, width=62., height=62)
        self.seat_twenty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('27', "#798ec4"))
        self.seat_twenty_seven.place(x=13, y=485, width=62., height=62)
        self.seat_twenty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('28', "#798ec4"))
        self.seat_twenty_eight.place(x=83, y=485, width=62., height=62)
        self.seat_twenty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('29', "#798ec4"))
        self.seat_twenty_nine.place(x=13, y=559, width=62., height=62)
        self.seat_thirty = tk.Button(self.root, relief="raised", bg=seat_colors.get('30', "#798ec4"))
        self.seat_thirty.place(x=83, y=559, width=62., height=62)

        # RIGHT SIDE
        self.seat_thirty_one = tk.Button(self.root, relief="raised", bg=seat_colors.get('31', "#798ec4"))
        self.seat_thirty_one.place(x=853, y=263, width=62., height=62)
        self.seat_thirty_two = tk.Button(self.root, relief="raised", bg=seat_colors.get('32', "#798ec4"))
        self.seat_thirty_two.place(x=923, y=263, width=62., height=62)
        self.seat_thirty_three = tk.Button(self.root, relief="raised", bg=seat_colors.get('33', "#798ec4"))
        self.seat_thirty_three.place(x=853, y=337, width=62., height=62)
        self.seat_thirty_four = tk.Button(self.root, relief="raised", bg=seat_colors.get('34', "#798ec4"))
        self.seat_thirty_four.place(x=923, y=337, width=62., height=62)
        self.seat_thirty_five = tk.Button(self.root, relief="raised", bg=seat_colors.get('35', "#798ec4"))
        self.seat_thirty_five.place(x=853, y=411, width=62., height=62)
        self.seat_thirty_six = tk.Button(self.root, relief="raised", bg=seat_colors.get('36', "#798ec4"))
        self.seat_thirty_six.place(x=923, y=411, width=62., height=62)
        self.seat_thirty_seven = tk.Button(self.root, relief="raised", bg=seat_colors.get('37', "#798ec4"))
        self.seat_thirty_seven.place(x=853, y=485, width=62., height=62)
        self.seat_thirty_eight = tk.Button(self.root, relief="raised", bg=seat_colors.get('38', "#798ec4"))
        self.seat_thirty_eight.place(x=923, y=485, width=62., height=62)
        self.seat_thirty_nine = tk.Button(self.root, relief="raised", bg=seat_colors.get('39', "#798ec4"))
        self.seat_thirty_nine.place(x=853, y=559, width=62., height=62)
        self.seat_forty = tk.Button(self.root, relief="raised", bg=seat_colors.get('40', "#798ec4"))
        self.seat_forty.place(x=923, y=559, width=62., height=62)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = GD2Layout(root)
    root.mainloop()