# Importing necessary libraries
import tkinter as tk

# Main class for Layout - GD1 page
class GD1Layout:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Glinda Day 1 Seats")

        # Placing the main design of the save page
        self.save_title = tk.PhotoImage(file="Designs/Layout/GD1_Layout.png")
        self.save_title_label = tk.Label(self.root, image=self.save_title)
        self.save_title_label.image = self.save_title
        self.save_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing the 40 seats/buttons !!! (warning: a lot)

        # FIRST ROW
        self.seat_one = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_one.place(x=293, y=339, width=62., height=62)
        self.seat_two = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_two.place(x=363, y=339, width=62., height=62)
        self.seat_three = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_three.place(x=433, y=339, width=62., height=62)
        self.seat_four = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_four.place(x=503, y=339, width=62., height=62)
        self.seat_five = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_five.place(x=573, y=339, width=62., height=62)
        self.seat_six = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_six.place(x=643, y=339, width=62., height=62)

        # SECOND ROW
        self.seat_seven = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_seven.place(x=223, y=411, width=62., height=62)
        self.seat_eight = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_eight.place(x=293, y=411, width=62., height=62)
        self.seat_nine = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_nine.place(x=363, y=411, width=62., height=62)
        self.seat_ten = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_ten.place(x=433, y=411, width=62., height=62)
        self.seat_eleven = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_eleven.place(x=503, y=411, width=62., height=62)
        self.seat_twelve = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twelve.place(x=573, y=411, width=62., height=62)
        self.seat_thirteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirteen.place(x=643, y=411, width=62., height=62)
        self.seat_fourteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_fourteen.place(x=713, y=411, width=62., height=62)

        # THIRD ROW
        self.seat_fifteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_fifteen.place(x=153, y=485, width=62., height=62)
        self.seat_sixteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_sixteen.place(x=223, y=485, width=62., height=62)
        self.seat_seventeen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_seventeen.place(x=293, y=485, width=62., height=62)
        self.seat_eighteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_eighteen.place(x=643, y=485, width=62., height=62)
        self.seat_nineteen = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_nineteen.place(x=713, y=485, width=62., height=62)
        self.seat_twenty = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty.place(x=783, y=485, width=62., height=62)

        # LEFT SIDE
        self.seat_twenty_one = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_one.place(x=13, y=263, width=62., height=62)
        self.seat_twenty_two = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_two.place(x=83, y=263, width=62., height=62)
        self.seat_twenty_three = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_three.place(x=13, y=337, width=62., height=62)
        self.seat_twenty_four = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_four.place(x=83, y=337, width=62., height=62)
        self.seat_twenty_five = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_five.place(x=13, y=411, width=62., height=62)
        self.seat_twenty_six = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_six.place(x=83, y=411, width=62., height=62)
        self.seat_twenty_seven = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_seven.place(x=13, y=485, width=62., height=62)
        self.seat_twenty_eight = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_eight.place(x=83, y=485, width=62., height=62)
        self.seat_twenty_nine = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_twenty_nine.place(x=13, y=559, width=62., height=62)
        self.seat_thirty = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty.place(x=83, y=559, width=62., height=62)

        # RIGHT SIDE
        self.seat_thirty_one = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_one.place(x=853, y=263, width=62., height=62)
        self.seat_thirty_two = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_two.place(x=923, y=263, width=62., height=62)
        self.seat_thirty_three = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_three.place(x=853, y=337, width=62., height=62)
        self.seat_thirty_four = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_four.place(x=923, y=337, width=62., height=62)
        self.seat_thirty_five = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_five.place(x=853, y=411, width=62., height=62)
        self.seat_thirty_six = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_six.place(x=923, y=411, width=62., height=62)
        self.seat_thirty_seven = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_seven.place(x=853, y=485, width=62., height=62)
        self.seat_thirty_eight = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_eight.place(x=923, y=485, width=62., height=62)
        self.seat_thirty_nine = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_thirty_nine.place(x=853, y=559, width=62., height=62)
        self.seat_forty = tk.Button(self.root, relief="ridge", bg="#798ec4")
        self.seat_forty.place(x=923, y=559, width=62., height=62)

if __name__ == "__main__":
    root = tk.Tk()
    app = GD1Layout(root)
    root.mainloop()