import tkinter as tk
import time

# Function to gradually increase the opacity of the modal
def fade_in(modal, alpha=0.0):
    if alpha < 1.0:
        modal.attributes('-alpha', alpha)  # Set the opacity of the modal
        alpha += 0.1  # Increase the opacity
        root.after(10, fade_in, modal, alpha)  # Call fade_in again after 10ms

# Function to gradually decrease the opacity of the modal
def fade_out(modal, alpha=1.0):
    if alpha > 0.0:
        modal.attributes('-alpha', alpha)  # Set the opacity of the modal
        alpha -= 0.1  # Decrease the opacity
        root.after(10, fade_out, modal, alpha)  # Call fade_out again after 10ms
    else:
        modal.attributes('-alpha', 0.0)  # Ensure the modal is fully transparent

# Function to show the modal when the mouse hovers over the button
def show_modal(event):
    # Get the button's position and size
    x = event.widget.winfo_rootx()
    y = event.widget.winfo_rooty()
    width = event.widget.winfo_width()
    height = event.widget.winfo_height()

    # Place the modal beside the button
    modal.geometry(f"+{x + width + 10}+{y}")
    modal.lift()  # Bring the modal to the front
    fade_in(modal)  # Start fading in the modal

# Function to hide the modal when the mouse leaves the modal
def hide_modal(event):
    fade_out(modal)  # Start fading out the modal

# Function to keep the modal visible when the mouse enters the modal
def on_modal_enter(event):
    modal.keep_visible = True

# Function to hide the modal when the mouse leaves the modal
def on_modal_leave(event):
    modal.keep_visible = False
    hide_modal(event)  # Start fading out the modal

# Function to print a message below the main button
def print_message():
    global message_count
    message_count += 1  # Increment the message count
    message_label.config(text=f"Message count: {message_count}")  # Update the label text

# Create the main application window
root = tk.Tk()
root.geometry("300x200")  # Set the window size
root.title("Hover Modal Example")  # Set the window title

# Create a button
button = tk.Button(root, text="Hover over me")
button.pack(pady=50, padx=100)  # Add padding around the button

# Create a label to display messages
message_count = 0
message_label = tk.Label(root, text="Message count: 0")
message_label.pack()  # Pack the label below the button

# Create a small modal (tooltip-like)
modal = tk.Toplevel(root)
modal.geometry("-1000-1000")  # Initialize off-screen
modal.overrideredirect(True)  # Remove window decorations
modal.attributes('-alpha', 0.0)  # Set initial opacity to 0
modal.keep_visible = False  # Initialize keep_visible flag

# Create a frame inside the modal to group elements
modal_frame = tk.Frame(modal, bg="lightyellow", relief="solid", borderwidth=1)
modal_frame.pack()  # Pack the frame inside the modal

# Add a label inside the modal frame
modal_label = tk.Label(modal_frame, text="This is a modal!", bg="lightyellow")
modal_label.pack()  # Pack the label inside the frame

# Add a button inside the modal frame
modal_button = tk.Button(modal_frame, text="Click me", command=print_message)
modal_button.pack(pady=10)  # Add padding around the button

# Bind mouse events to show and hide the modal
button.bind("<Enter>", show_modal)  # Show modal on button hover
modal_frame.bind("<Enter>", on_modal_enter)  # Keep modal visible on modal enter
modal_frame.bind("<Leave>", on_modal_leave)  # Hide modal on modal leave

# Start the main event loop
root.mainloop()
