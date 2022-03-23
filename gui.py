# Import Python Libraries
from tkinter import *
from tkinter.ttk import *

# Import Custom Classes
from clock import Clock
from counter import Counter
from modifiers import Modifiers
from save_state import SaveState


class GUI:
    click = 1
    tick = 1
    main_clock = Clock()
    counter = Counter()
    modifiers = Modifiers()
    save_state = SaveState()
    clocks = [main_clock]
    counters = [counter]

    def __init__(self, master, clock):
        # Take in main clock and initialize it
        self.main_clock = clock

        # Initialize master
        self.master = master
        self.master.title('Number Simulator')
        self.master.iconbitmap("assets/sqrt2.ico")

        # Create and initialize Menus
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="Load", command=self.load)
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)

        stats_menu = Menu(menu)
        stats_menu.add_command(label="Open Statistics Window", command=self.get_statistics)
        menu.add_cascade(label="Stats", menu=stats_menu)

        # Create Frames
        self.game_frame = Frame(self.master, borderwidth=2, relief=SUNKEN)
        self.button_frame = Frame(self.master, borderwidth=2, relief=SUNKEN)
        # self.modifiers_frame = Frame(self.master, borderwidth=2, relief=SUNKEN)

        # Creating and styling the Label widgets
        self.date_label = Label(self.game_frame, font=('cambria', 40, 'bold'), background='red', foreground='white',
                                justify=CENTER)
        self.time_label = Label(self.game_frame, font=('cambria', 40, 'bold'), background='purple', foreground='white',
                                justify=CENTER)
        self.counter_label = Label(self.game_frame, font=('cambria', 40, 'bold'), background='blue', foreground='white',
                                   justify=CENTER)

        # Creating Buttons
        self.clicker = Button(self.button_frame, text='Click Me', command=self.clicker_callback)
        self.buy_clicker = Button(self.button_frame, text='Buy +1/click [ 0 ] ( 100 )', state="disabled",
                                  command=self.buy_clicker_callback)
        self.buy_ticker = Button(self.button_frame, text='Buy +1/tick [ 0 ] ( 1000 )', state="disabled",
                                 command=self.buy_ticker_callback)
        self.sell_clicker = Button(self.button_frame, text='Sell +1/click ( - )', state="disabled",
                                   command=self.sell_clicker_callback)
        self.sell_ticker = Button(self.button_frame, text='Sell +1/tick ( - )', state="disabled",
                                  command=self.sell_ticker_callback)

        # Placing Frames, Labels, and Buttons at the centre of the tkinter window
        self.game_frame.grid(row=0, column=0, sticky=E + W, padx=5, pady=5)
        self.button_frame.grid(row=1, column=0, sticky=E + W, padx=5, pady=5)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        self.date_label.pack(anchor='center', expand=True, fill='both')
        self.time_label.pack(anchor='center', expand=True, fill='both')
        self.counter_label.pack(anchor='center', expand=True, fill='both')

        self.clicker.grid(row=0, column=0, columnspan=4, sticky=N + E + S + W)
        self.buy_clicker.grid(row=1, column=0, columnspan=2, sticky=N + E + S + W)
        self.buy_ticker.grid(row=2, column=0, columnspan=2, sticky=N + E + S + W)
        self.sell_clicker.grid(row=1, column=2, columnspan=2, sticky=N + E + S + W)
        self.sell_ticker.grid(row=2, column=2, columnspan=2, sticky=N + E + S + W)

        # Initialize the main clock
        self.main_clock.time()
        self.date_label.config(text=self.main_clock.start_date)
        self.time_label.config(text=self.main_clock.current_time)
        self.counter_label.config(text=self.counter.current_count)

    # Function to automatically increment the clock and counter every 1 second
    def update_gui(self):
        self.date_label.config(text=self.main_clock.current_date)
        self.time_label.config(text=self.main_clock.current_time)
        self.counter.increment(self.tick + self.modifiers.tick_counter.current_count)
        self.counter_label.config(text=self.counter.current_count)
        self.buy_clicker["text"] = "Buy +1/click [ " + str(self.modifiers.click_mod) + " ] ( " + \
                                   str(self.modifiers.click_mod_buy) + " )"
        self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.modifiers.tick_mod) + " ] ( " + \
                                  str(self.modifiers.tick_mod_buy) + " )"

        # Toggle the buy buttons based on if you can afford them
        if self.counter.current_count < self.modifiers.click_mod_buy:
            self.buy_clicker["state"] = "disabled"
        else:
            self.buy_clicker["state"] = "normal"

        if self.counter.current_count < self.modifiers.tick_mod_buy:
            self.buy_ticker["state"] = "disabled"
        else:
            self.buy_ticker["state"] = "normal"

        # Toggle the sell buttons based on if you own any
        if self.modifiers.click_mod == 0:
            self.sell_clicker["state"] = "disabled"
            self.sell_clicker["text"] = "Sell +1/click ( - )"
        else:
            self.sell_clicker["state"] = "normal"
            self.sell_clicker["text"] = "Sell +1/click ( " + str(self.modifiers.get_click_mod_sell()) + " )"

        if self.modifiers.tick_mod == 0:
            self.sell_ticker["state"] = "disabled"
            self.sell_ticker["text"] = "Sell +1/tick ( - )"
        else:
            self.sell_ticker["state"] = "normal"
            self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.modifiers.get_tick_mod_sell()) + " )"

    # Button Callbacks
    def clicker_callback(self):
        self.counter.increment(self.click + self.modifiers.click_counter.current_count)
        self.counter_label.config(text=self.counter.current_count)

    def buy_clicker_callback(self):
        if self.counter.current_count >= self.modifiers.click_mod_buy:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.click_mod_buy)
            self.modifiers.increment_click_mod(1)
            self.counter_label.config(text=self.counter.current_count)
            self.buy_clicker["text"] = "Buy +1/click [ " + str(self.modifiers.click_mod) + " ] ( " + \
                                       str(self.modifiers.click_mod_buy) + " )"
            self.sell_clicker["text"] = "Sell +1/click ( " + str(self.modifiers.get_click_mod_sell()) + " )"

            # Toggle on the sell clicker button
            self.sell_clicker["state"] = "normal"

            # Toggle the buy buttons based on if you can afford them
            if self.counter.current_count < self.modifiers.click_mod_buy:
                self.buy_clicker["state"] = "disabled"
            else:
                self.buy_clicker["state"] = "normal"

            if self.counter.current_count < self.modifiers.tick_mod_buy:
                self.buy_ticker["state"] = "disabled"
            else:
                self.buy_ticker["state"] = "normal"

    def buy_ticker_callback(self):
        if self.counter.current_count >= self.modifiers.tick_mod_buy:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.tick_mod_buy)
            self.modifiers.increment_tick_mod(1)
            self.counter_label.config(text=self.counter.current_count)
            self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.modifiers.tick_mod) + " ] ( " + \
                                      str(self.modifiers.tick_mod_buy) + " )"
            self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.modifiers.get_tick_mod_sell()) + " )"

            # Toggle on the sell ticker button
            self.sell_ticker["state"] = "normal"

            # Toggle the buy buttons based on if you can afford them
            if self.counter.current_count < self.modifiers.click_mod_buy:
                self.buy_clicker["state"] = "disabled"
            else:
                self.buy_clicker["state"] = "normal"

            if self.counter.current_count < self.modifiers.tick_mod_buy:
                self.buy_ticker["state"] = "disabled"
            else:
                self.buy_ticker["state"] = "normal"

    def sell_clicker_callback(self):
        if self.modifiers.click_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_click_mod_sell())
            self.counter_label.config(text=self.counter.current_count)
            self.modifiers.decrement_click_mod(1)

            # Toggle the sell button based on if you own any
            if self.modifiers.click_mod == 0:
                self.sell_clicker["state"] = "disabled"
                self.sell_clicker["text"] = "Sell +1/click ( - )"
                self.buy_clicker["text"] = "Buy +1/click [ 0 ] ( 100 )"
            else:
                self.sell_clicker["text"] = "Sell +1/click ( " + str(self.modifiers.get_click_mod_sell()) + " )"
                self.buy_clicker["text"] = "Buy +1/click [ " + str(self.modifiers.click_mod) + " ] ( " + \
                                           str(self.modifiers.click_mod_buy) + " )"

            # Toggle the buy buttons based on if you can afford them
            if self.counter.current_count < self.modifiers.click_mod_buy:
                self.buy_clicker["state"] = "disabled"
            else:
                self.buy_clicker["state"] = "normal"

            if self.counter.current_count < self.modifiers.tick_mod_buy:
                self.buy_ticker["state"] = "disabled"
            else:
                self.buy_ticker["state"] = "normal"

    def sell_ticker_callback(self):
        if self.modifiers.tick_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_tick_mod_sell())
            self.counter_label.config(text=self.counter.current_count)
            self.modifiers.decrement_tick_mod(1)

            # Toggle the sell button based on if you own any
            if self.modifiers.tick_mod == 0:
                self.sell_ticker["state"] = "disabled"
                self.sell_ticker["text"] = "Sell +1/tick ( - )"
                self.buy_ticker["text"] = "Buy +1/tick [ 0 ] ( 1000 )"
            else:
                self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.modifiers.get_click_mod_sell()) + " )"
                self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.modifiers.tick_mod) + " ] ( " + \
                                          str(self.modifiers.tick_mod_buy) + " )"

            # Toggle the buy buttons based on if you can afford them
            if self.counter.current_count < self.modifiers.click_mod_buy:
                self.buy_clicker["state"] = "disabled"
            else:
                self.buy_clicker["state"] = "normal"

            if self.counter.current_count < self.modifiers.tick_mod_buy:
                self.buy_ticker["state"] = "disabled"
            else:
                self.buy_ticker["state"] = "normal"

    # Menu Functions
    def save(self):
        self.save_state.save(self.main_clock, self.counter, self.modifiers)

    def load(self):
        self.save_state.load(self.main_clock, self.counter, self.modifiers)

    def exit_program(self):
        self.master.destroy()
        print("The application has been quit.")

    def get_statistics(self):
        self.window = Toplevel(self.master)
        self.window.title('Statistics')
        self.window.iconbitmap("assets/sqrt2.ico")
        self.window.grab_set()
        Label(self.window, justify=CENTER, text='Statistics: ').grid(row=0, column=0, columnspan=2,
                                                                     sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Start Date: ').grid(row=1, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.main_clock.get_start_date()).grid(row=1, column=1,
                                                                                       sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Start Time: ').grid(row=2, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.main_clock.get_start_time_str()).grid(row=2, column=1,
                                                                                           sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Current Date: ').grid(row=3, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.main_clock.get_current_date()).grid(row=3, column=1,
                                                                                         sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Current Time: ').grid(row=4, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.main_clock.get_current_time()).grid(row=4, column=1,
                                                                                         sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Elapsed Time: ').grid(row=5, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=str(self.main_clock.get_time_since_start())).grid(row=5, column=1,
                                                                                                  sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Current Count: ').grid(row=6, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=str(self.counter.get_current_count())).grid(row=6, column=1,
                                                                                            sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Click Modifier: ').grid(row=7, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.modifiers.get_click_mod()).grid(row=7, column=1,
                                                                                     sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text='Tick Modifier: ').grid(row=8, column=0, sticky=N + E + S + W)
        Label(self.window, justify=CENTER, text=self.modifiers.get_tick_mod()).grid(row=8, column=1,
                                                                                    sticky=N + E + S + W)
        Button(self.window, text='Close Window', command=self.exit_window).grid(row=9, column=0, columnspan=2,
                                                                                sticky=N + E + S + W)

    def exit_window(self):
        self.window.destroy()
        print("The statistics window has been closed.")
