# Import Python Libraries
from tkinter import *

# Import Custom Classes
from clock import Clock
from gui import GUI


# Create main clock
main_clock = Clock()

# Create Tkinter Window
root = Tk()
app = GUI(root, main_clock)

# Create variable for counting 1 second
diff = main_clock.time_since_start

# Main Loop
while True:
    main_clock.time()
    if main_clock.time_since_start - diff > 1:
        GUI.update_gui(self=app)
        diff = main_clock.time_since_start
    root.update_idletasks()
    root.update()
