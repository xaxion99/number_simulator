# Import Python Libraries
from math import *
from tkinter import *
from tkinter.ttk import *

# Import Custom Classes
from clock import Clock
from counter import Counter
from helper import Helper
from modifiers import Modifiers
from save_state import SaveState
from stats_gui import StatsGUI


class GUI:
    base_click = 1
    base_tick = 1
    main_clock = Clock()
    counter = Counter()
    max_counter = Counter()
    click_counter = Counter()
    tick_counter = Counter()
    helper = Helper()
    modifiers = Modifiers()
    save_state = SaveState()
    clocks = [main_clock]
    counters = [counter, max_counter, click_counter, tick_counter]

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
        self.buy_ticker = Button(self.button_frame, text='Buy +1/tick [ 0 ] ( 1,000 )', state="disabled",
                                 command=self.buy_ticker_callback)
        self.sell_clicker = Button(self.button_frame, text='Sell +1/click ( - )', state="disabled",
                                   command=self.sell_clicker_callback)
        self.sell_ticker = Button(self.button_frame, text='Sell +1/tick ( - )', state="disabled",
                                  command=self.sell_ticker_callback)
        self.buy_clicker_multiplier = Button(self.button_frame, text='Buy +10%/click [ 0 ] ( 10,000 )',
                                             state="disabled", command=self.buy_clicker_multiplier_callback)
        self.buy_ticker_multiplier = Button(self.button_frame, text='Buy +10%/tick [ 0 ] ( 100,000 )', state="disabled",
                                            command=self.buy_ticker_multiplier_callback)
        self.sell_clicker_multiplier = Button(self.button_frame, text='Sell +10%/click ( - )', state="disabled",
                                              command=self.sell_clicker_multiplier_callback)
        self.sell_ticker_multiplier = Button(self.button_frame, text='Sell +10%/tick ( - )', state="disabled",
                                             command=self.sell_ticker_multiplier_callback)

        # Placing Frames, Labels, and Buttons at the centre of the tkinter window
        self.game_frame.grid(row=0, column=0, sticky=E + W, padx=5, pady=5)
        self.button_frame.grid(row=1, column=0, sticky=E + W, padx=5, pady=5)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        self.date_label.pack(anchor='center', expand=True, fill='both')
        self.time_label.pack(anchor='center', expand=True, fill='both')
        self.counter_label.pack(anchor='center', expand=True, fill='both')

        self.clicker.grid(row=0, column=0, columnspan=4, sticky=N + E + S + W)

        # Initialize the main clock
        self.main_clock.time()
        self.date_label.config(text=self.main_clock.start_date)
        self.time_label.config(text=self.main_clock.current_time)
        self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))

    # Function to automatically increment the clock and counter every 1 second
    # Function that controls a tick
    def update_gui(self):
        self.date_label.config(text=self.main_clock.current_date)
        self.time_label.config(text=self.main_clock.current_time)

        tick = self.base_tick + self.modifiers.tick_counter.current_count
        tick += ceil(tick * 0.1 * self.modifiers.tick_multiplier_counter.current_count)
        self.counter.increment(tick)
        self.max_counter.increment(tick)
        self.tick_counter.increment(tick)
        self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))

        self.scheduler()
        self.buy_buttons_toggler()
        self.sell_buttons_toggler()

    # Button Callbacks
    # Function that controls a click
    def clicker_callback(self):
        click = self.base_click + self.modifiers.click_counter.current_count
        click += ceil(click * 0.1 * self.modifiers.click_multiplier_counter.current_count)
        self.counter.increment(click)
        self.max_counter.increment(click)
        self.click_counter.increment(click)
        self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))

        self.scheduler()
        self.buy_buttons_toggler()

    # Buy Button Callbacks
    def buy_clicker_callback(self):
        if self.counter.current_count >= self.modifiers.click_mod_buy:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.click_mod_buy)
            self.modifiers.increment_click_mod(1)
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.scheduler()
            self.buy_clicker["text"] = "Buy +1/click [ " + str(self.helper.number_formatter(self.modifiers.click_mod)) \
                                       + " ] ( " + str(self.helper.number_formatter(self.modifiers.click_mod_buy)) + \
                                       " )"
            self.sell_clicker["text"] = "Sell +1/click ( " + str(self.helper.number_formatter(
                self.modifiers.get_click_mod_sell())) + " )"

            # Toggle on the sell clicker button
            self.sell_clicker["state"] = "normal"

            self.buy_buttons_toggler()

    def buy_ticker_callback(self):
        if self.counter.current_count >= self.modifiers.tick_mod_buy:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.tick_mod_buy)
            self.modifiers.increment_tick_mod(1)
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.scheduler()
            self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.helper.number_formatter(self.modifiers.tick_mod)) + \
                                      " ] ( " + str(self.helper.number_formatter(self.modifiers.tick_mod_buy)) + " )"
            self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.helper.number_formatter(
                self.modifiers.get_tick_mod_sell())) + " )"

            # Toggle on the sell ticker button
            self.sell_ticker["state"] = "normal"

            self.buy_buttons_toggler()

    def buy_clicker_multiplier_callback(self):
        if self.counter.current_count >= self.modifiers.click_multi_mod_buy:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.click_multi_mod_buy)
            self.modifiers.increment_click_multi_mod(1)
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.scheduler()
            self.buy_clicker_multiplier["text"] = "Buy +10%/click [ " + str(self.helper.number_formatter(
                self.modifiers.click_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
                self.modifiers.click_multi_mod_buy)) + " )"
            self.sell_clicker_multiplier["text"] = "Sell +10%/click ( " + str(self.helper.number_formatter(
                self.modifiers.get_click_multi_mod_sell())) + " )"

            # Toggle on the sell clicker button
            self.sell_clicker_multiplier["state"] = "normal"

            self.buy_buttons_toggler()

    def buy_ticker_multiplier_callback(self):
        if self.counter.current_count >= self.modifiers.tick_multi_mod_sell:
            self.counter.set_current_count(self.counter.current_count - self.modifiers.tick_multi_mod_buy)
            self.modifiers.increment_tick_multi_mod(1)
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.scheduler()
            self.buy_ticker_multiplier["text"] = "Buy +10%/tick [ " + str(self.helper.number_formatter(
                self.modifiers.tick_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
                self.modifiers.tick_multi_mod_buy)) + " )"
            self.sell_ticker_multiplier["text"] = "Sell +10%/tick ( " + str(self.helper.number_formatter(
                self.modifiers.get_tick_multi_mod_sell())) + " )"

            # Toggle on the sell ticker button
            self.sell_ticker_multiplier["state"] = "normal"

            self.buy_buttons_toggler()

    # Sell Button Callbacks
    def sell_clicker_callback(self):
        if self.modifiers.click_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_click_mod_sell())
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.modifiers.decrement_click_mod(1)
            self.scheduler()

            # Toggle the sell button based on if you own any
            if self.modifiers.click_mod == 0:
                self.sell_clicker["state"] = "disabled"
                self.sell_clicker["text"] = "Sell +1/click ( - )"
                self.buy_clicker["text"] = "Buy +1/click [ 0 ] ( 100 )"
            else:
                self.sell_clicker["text"] = "Sell +1/click ( " + str(self.helper.number_formatter(
                    self.modifiers.get_click_mod_sell())) + " )"
                self.buy_clicker["text"] = "Buy +1/click [ " + str(self.helper.number_formatter(
                    self.modifiers.click_mod)) + " ] ( " + str(self.helper.number_formatter(
                    self.modifiers.click_mod_buy)) + " )"

            self.buy_buttons_toggler()

    def sell_ticker_callback(self):
        if self.modifiers.tick_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_tick_mod_sell())
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.modifiers.decrement_tick_mod(1)
            self.scheduler()

            # Toggle the sell button based on if you own any
            if self.modifiers.tick_mod == 0:
                self.sell_ticker["state"] = "disabled"
                self.sell_ticker["text"] = "Sell +1/tick ( - )"
                self.buy_ticker["text"] = "Buy +1/tick [ 0 ] ( 1,000 )"
            else:
                self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.helper.number_formatter(
                    self.modifiers.get_tick_mod_sell())) + " )"
                self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.helper.number_formatter(
                    self.modifiers.tick_mod)) + " ] ( " + str(self.helper.number_formatter(
                    self.modifiers.tick_mod_buy)) + " )"

            self.buy_buttons_toggler()

    def sell_clicker_multiplier_callback(self):
        if self.modifiers.click_multi_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_click_multi_mod_sell())
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.modifiers.decrement_click_multi_mod(1)
            self.scheduler()

            # Toggle the sell button based on if you own any
            if self.modifiers.click_multi_mod == 0:
                self.sell_clicker_multiplier["state"] = "disabled"
                self.sell_clicker_multiplier["text"] = "Sell +10%/click ( - )"
                self.buy_clicker_multiplier["text"] = "Buy +10%/click [ 0 ] ( 100,000 )"
            else:
                self.sell_clicker_multiplier["text"] = "Sell +10%/click ( " + str(self.helper.number_formatter(
                    self.modifiers.get_click_multi_mod_sell())) + " )"
                self.buy_clicker_multiplier["text"] = "Buy +10%/click [ " + str(self.helper.number_formatter(
                    self.modifiers.click_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
                    self.modifiers.click_multi_mod_buy)) + " )"

            self.buy_buttons_toggler()

    def sell_ticker_multiplier_callback(self):
        if self.modifiers.tick_multi_mod > 0:
            self.counter.set_current_count(self.counter.current_count + self.modifiers.get_tick_multi_mod_sell())
            self.counter_label.config(text=str(self.helper.number_formatter(self.counter.current_count)))
            self.modifiers.decrement_tick_multi_mod(1)
            self.scheduler()

            # Toggle the sell button based on if you own any
            if self.modifiers.tick_multi_mod == 0:
                self.sell_ticker_multiplier["state"] = "disabled"
                self.sell_ticker_multiplier["text"] = "Sell +10%/tick ( - )"
                self.buy_ticker_multiplier["text"] = "Buy +10%/tick [ 0 ] ( 100,000 )"
            else:
                self.sell_ticker_multiplier["text"] = "Sell +10%/tick ( " + str(self.helper.number_formatter(
                    self.modifiers.get_tick_multi_mod_sell())) + " )"
                self.buy_ticker_multiplier["text"] = "Buy +10%/tick [ " + str(self.helper.number_formatter(
                    self.modifiers.tick_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
                    self.modifiers.tick_multi_mod_buy)) + " )"

            self.buy_buttons_toggler()

    # Function for scheduling when modifier buttons appear on the GUI
    def scheduler(self):
        if self.max_counter.current_count >= 100:
            self.buy_clicker.grid(row=1, column=0, columnspan=2, sticky=N + E + S + W)
            self.sell_clicker.grid(row=1, column=2, columnspan=2, sticky=N + E + S + W)

        if self.max_counter.current_count >= 1000:
            self.buy_ticker.grid(row=2, column=0, columnspan=2, sticky=N + E + S + W)
            self.sell_ticker.grid(row=2, column=2, columnspan=2, sticky=N + E + S + W)

        if self.max_counter.current_count >= 10000:
            self.buy_clicker_multiplier.grid(row=3, column=0, columnspan=2, sticky=N + E + S + W)
            self.sell_clicker_multiplier.grid(row=3, column=2, columnspan=2, sticky=N + E + S + W)

        if self.max_counter.current_count >= 100000:
            self.buy_ticker_multiplier.grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)
            self.sell_ticker_multiplier.grid(row=4, column=2, columnspan=2, sticky=N + E + S + W)

    # Function to toggle when the state and text of the buy/sell buttons
    def buy_buttons_toggler(self):
        # Set the proper text for buy buttons whenever called, should be needed for loads
        self.buy_clicker["text"] = "Buy +1/click [ " + str(self.helper.number_formatter(self.modifiers.click_mod)) + \
                                   " ] ( " + str(self.helper.number_formatter(self.modifiers.click_mod_buy)) + " )"
        self.buy_ticker["text"] = "Buy +1/tick [ " + str(self.helper.number_formatter(self.modifiers.tick_mod)) + \
                                  " ] ( " + str(self.helper.number_formatter(self.modifiers.tick_mod_buy)) + " )"
        self.buy_clicker_multiplier["text"] = "Buy +10%/click [ " + str(self.helper.number_formatter(
            self.modifiers.click_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
            self.modifiers.click_multi_mod_buy)) + " )"
        self.buy_ticker_multiplier["text"] = "Buy +10%/tick [ " + str(self.helper.number_formatter(
            self.modifiers.tick_multi_mod)) + " ] ( " + str(self.helper.number_formatter(
            self.modifiers.tick_multi_mod_buy)) + " )"

        # Toggle the buy buttons based on if you can afford them
        if self.counter.current_count < self.modifiers.click_mod_buy:
            self.buy_clicker["state"] = "disabled"
        else:
            self.buy_clicker["state"] = "normal"

        if self.counter.current_count < self.modifiers.tick_mod_buy:
            self.buy_ticker["state"] = "disabled"
        else:
            self.buy_ticker["state"] = "normal"

        if self.counter.current_count < self.modifiers.click_multi_mod_buy:
            self.buy_clicker_multiplier["state"] = "disabled"
        else:
            self.buy_clicker_multiplier["state"] = "normal"

        if self.counter.current_count < self.modifiers.tick_multi_mod_buy:
            self.buy_ticker_multiplier["state"] = "disabled"
        else:
            self.buy_ticker_multiplier["state"] = "normal"

    def sell_buttons_toggler(self):
        # Toggle the sell buttons based on if you own any
        if self.modifiers.click_mod == 0:
            self.sell_clicker["state"] = "disabled"
            self.sell_clicker["text"] = "Sell +1/click ( - )"
        else:
            self.sell_clicker["state"] = "normal"
            self.sell_clicker["text"] = "Sell +1/click ( " + str(self.helper.number_formatter(
                self.modifiers.get_click_mod_sell())) + " )"

        if self.modifiers.tick_mod == 0:
            self.sell_ticker["state"] = "disabled"
            self.sell_ticker["text"] = "Sell +1/tick ( - )"
        else:
            self.sell_ticker["state"] = "normal"
            self.sell_ticker["text"] = "Sell +1/tick ( " + str(self.helper.number_formatter(
                self.modifiers.get_tick_mod_sell())) + " )"

        if self.modifiers.click_multi_mod == 0:
            self.sell_clicker_multiplier["state"] = "disabled"
            self.sell_clicker_multiplier["text"] = "Sell +10%/click ( - )"
        else:
            self.sell_clicker_multiplier["state"] = "normal"
            self.sell_clicker_multiplier["text"] = "Sell +10%/click ( " + str(self.helper.number_formatter(
                self.modifiers.get_click_multi_mod_sell())) + " )"

        if self.modifiers.tick_multi_mod == 0:
            self.sell_ticker_multiplier["state"] = "disabled"
            self.sell_ticker_multiplier["text"] = "Sell +10%/tick ( - )"
        else:
            self.sell_ticker_multiplier["state"] = "normal"
            self.sell_ticker_multiplier["text"] = "Sell +10%/tick ( " + str(self.helper.number_formatter(
                self.modifiers.get_tick_multi_mod_sell())) + " )"

    # Menu Functions
    def save(self):
        self.save_state.save(self.main_clock, self.counters, self.modifiers)

    def load(self):
        self.save_state.load(self.main_clock, self.counters, self.modifiers)

    def exit_program(self):
        self.master.destroy()
        print("The application has been quit.")

    # Statistics pop-out window, provides general statistics on the game thus far
    def get_statistics(self):
        stats_gui = StatsGUI(self.master, self.main_clock, self.counters, self.modifiers, self.base_click,
                             self.base_tick)
