# Import Python Libraries
from math import *
from tkinter import *
from tkinter.ttk import *

# Import Custom Classes
from helper import Helper


class StatsGUI:

    def __init__(self, master, main_clock, counters, modifiers, base_click, base_tick):
        self.master = master
        self.main_clock = main_clock
        self.counter = counters[0]
        self.max_counter = counters[1]
        self.click_counter = counters[2]
        self.tick_counter = counters[3]
        self.modifiers = modifiers
        self.base_click = base_click
        self.base_tick = base_tick
        self.helper = Helper()

        # Setup pop-out window
        self.window = Toplevel(self.master)
        self.window.title('Statistics')
        self.window.iconbitmap("assets/sqrt2.ico")
        self.window.grab_set()

        # Header Frame
        self.header_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        self.header_frame.grid(row=0, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Label(self.header_frame, font='bold', text='Statistics: ').grid(row=0, column=0, columnspan=2,
                                                                        sticky=N + E + S + W)
        # Clock Frame
        elapsed_time = str(self.main_clock.get_time_since_start())
        self.clock_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        self.clock_frame.grid(row=1, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Label(self.clock_frame, text='Clock Stats').grid(row=0, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.clock_frame, text='Start Date: ').grid(row=1, column=0, sticky=N + E + S + W)
        Label(self.clock_frame, text=self.main_clock.get_start_date()).grid(row=1, column=1, sticky=N + E + S + W)
        Label(self.clock_frame, text='Start Time: ').grid(row=2, column=0, sticky=N + E + S + W)
        Label(self.clock_frame, text=self.main_clock.get_start_time_str()).grid(row=2, column=1, sticky=N + E + S + W)
        Label(self.clock_frame, text='Current Date: ').grid(row=3, column=0, sticky=N + E + S + W)
        Label(self.clock_frame, text=self.main_clock.get_current_date()).grid(row=3, column=1, sticky=N + E + S + W)
        Label(self.clock_frame, text='Current Time: ').grid(row=4, column=0, sticky=N + E + S + W)
        Label(self.clock_frame, text=self.main_clock.get_current_time()).grid(row=4, column=1, sticky=N + E + S + W)
        Label(self.clock_frame, text='Elapsed Time: ').grid(row=5, column=0, sticky=N + E + S + W)
        Label(self.clock_frame, text=elapsed_time).grid(row=5, column=1, sticky=N + E + S + W)

        # Counts_Frame
        current_count = str(self.helper.number_formatter(self.counter.get_current_count()))
        max_count = str(self.helper.number_formatter(self.max_counter.current_count))
        self.counts_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        self.counts_frame.grid(row=2, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Label(self.counts_frame, text='Counts').grid(row=0, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.counts_frame, text='Current Count: ').grid(row=1, column=0, sticky=N + E + S + W)
        Label(self.counts_frame, text=current_count).grid(row=1, column=1, sticky=N + E + S + W)
        Label(self.counts_frame, text='Max Count: ').grid(row=2, column=0, sticky=N + E + S + W)
        Label(self.counts_frame, text=max_count).grid(row=2, column=1, sticky=N + E + S + W)

        # Click Frame
        bc = str(self.helper.number_formatter(self.base_click))
        cmod = str(self.helper.number_formatter(self.modifiers.get_click_mod()))
        cmulti = str(self.helper.number_formatter(10 * self.modifiers.get_click_multi_mod())) + '%'
        temp = self.modifiers.get_click_mod() + self.base_click
        temp += ceil(temp * 0.1 * self.modifiers.get_click_multi_mod())
        amount = '+' + str(self.helper.number_formatter(temp))
        click_amount = amount
        click_count = str(self.helper.number_formatter(self.click_counter.current_count))
        self.click_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        self.click_frame.grid(row=3, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Label(self.click_frame, text='Click Stats').grid(row=0, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.click_frame, text='Base Click: ').grid(row=1, column=0, sticky=N + E + S + W)
        Label(self.click_frame, text=bc).grid(row=1, column=1, sticky=N + E + S + W)
        Label(self.click_frame, text='Click Modifier: ').grid(row=2, column=0, sticky=N + E + S + W)
        Label(self.click_frame, text=cmod).grid(row=2, column=1, sticky=N + E + S + W)
        Label(self.click_frame, text='Click Multiplier: ').grid(row=3, column=0, sticky=N + E + S + W)
        Label(self.click_frame, text=cmulti).grid(row=3, column=1, sticky=N + E + S + W)
        Label(self.click_frame, text='Amount/Click: ').grid(row=4, column=0, sticky=N + E + S + W)
        Label(self.click_frame, text=click_amount).grid(row=4, column=1, sticky=N + E + S + W)
        Label(self.click_frame, text='Click Count: ').grid(row=5, column=0, sticky=N + E + S + W)
        Label(self.click_frame, text=click_count).grid(row=5, column=1, sticky=N + E + S + W)

        # Tick Frame
        bt = str(self.helper.number_formatter(self.base_tick))
        tmod = str(self.helper.number_formatter(self.modifiers.get_tick_mod()))
        tmulti = str(self.helper.number_formatter(10 * self.modifiers.get_tick_multi_mod())) + '%'
        temp = self.modifiers.get_tick_mod() + self.base_tick
        temp += ceil(temp * 0.1 * self.modifiers.get_tick_multi_mod())
        amount = '+' + str(self.helper.number_formatter(temp))
        tick_amount = amount
        tick_count = str(self.helper.number_formatter(self.tick_counter.current_count))
        self.tick_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        self.tick_frame.grid(row=4, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Label(self.tick_frame, text='Tick Stats').grid(row=0, column=0, columnspan=2, sticky=N + E + S + W)
        Label(self.tick_frame, text='Base Tick: ').grid(row=1, column=0, sticky=N + E + S + W)
        Label(self.tick_frame, text=bt).grid(row=1, column=1, sticky=N + E + S + W)
        Label(self.tick_frame, text='Tick Modifier: ').grid(row=2, column=0, sticky=N + E + S + W)
        Label(self.tick_frame, text=tmod).grid(row=2, column=1, sticky=N + E + S + W)
        Label(self.tick_frame, text='Tick Multiplier: ').grid(row=3, column=0, sticky=N + E + S + W)
        Label(self.tick_frame, text=tmulti).grid(row=3, column=1, sticky=N + E + S + W)
        Label(self.tick_frame, text='Amount/Tick: ').grid(row=4, column=0, sticky=N + E + S + W)
        Label(self.tick_frame, text=tick_amount).grid(row=4, column=1, sticky=N + E + S + W)
        Label(self.tick_frame, text='Tick Count: ').grid(row=5, column=0, sticky=N + E + S + W)
        Label(self.tick_frame, text=tick_count).grid(row=5, column=1, sticky=N + E + S + W)

        # Footer Frame
        # self.footer_frame = Frame(self.window, borderwidth=2, relief=SUNKEN)
        # self.footer_frame.grid(row=5, column=0, sticky=N + E + S + W, padx=5, pady=5)
        Button(self.window, text='Close Window', command=self.exit_window).grid(row=5, column=0, columnspan=2,
                                                                                sticky=N + E + S + W)

    # Closes the statistics pop-out window
    def exit_window(self):
        self.window.destroy()
        print("The statistics window has been closed.")