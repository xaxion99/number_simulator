from counter import Counter


class Modifiers:
    click_counter = Counter()
    tick_counter = Counter()

    def __init__(self, click_mod=0, tick_mod=0):
        self.click_mod = click_mod
        self.tick_mod = tick_mod
        self.click_mod_buy = int(100 * (1.1 ** click_mod))
        self.tick_mod_buy = int(1000 * (1.2 ** tick_mod))

        if click_mod == 0:
            self.click_mod_sell = 0
        else:
            self.click_mod_sell = int(100 * (1.1 ** (click_mod - 1)))

        if tick_mod == 0:
            self.tick_mod_sell = 0
        else:
            self.tick_mod_sell = int(1000 * (1.2 ** (tick_mod - 1)))

    # Click modifiers functions
    def increment_click_mod(self, amount):
        self.click_counter.increment(amount)
        self.click_mod = self.click_counter.current_count
        self.click_mod_buy = int(100 * (1.1 ** self.click_mod))
        self.click_mod_sell = int(100 * (1.1 ** (self.click_mod - 1)))

    def decrement_click_mod(self, amount):
        self.click_counter.decrement(amount)
        self.click_mod = self.click_counter.current_count
        self.click_mod_buy = int(100 * (1.1 ** self.click_mod))

        if self.click_mod == 0:
            self.click_mod_sell = 0
        else:
            self.click_mod_sell = int(100 * (1.1 ** (self.click_mod - 1)))

    def total_spent_click_mod(self):
        total_spent_click = 0
        c = 0
        while c < self.click_mod:
            total_spent_click += int(100 * (1.1 ** c))
            c += 1

        return total_spent_click

    # Tick modifiers functions
    def increment_tick_mod(self, amount):
        self.tick_counter.increment(amount)
        self.tick_mod = self.tick_counter.current_count
        self.tick_mod_buy = int(1000 * (1.2 ** self.tick_mod))
        self.tick_mod_sell = int(1000 * (1.2 ** (self.tick_mod - 1)))

    def decrement_tick_mod(self, amount):
        self.tick_counter.decrement(amount)
        self.tick_mod = self.tick_counter.current_count
        self.tick_mod_buy = int(1000 * (1.2 ** self.tick_mod))

        if self.tick_mod == 0:
            self.tick_mod_sell = 0
        else:
            self.tick_mod_sell = int(1000 * (1.2 ** (self.tick_mod - 1)))

    def total_spent_tick_mod(self):
        total_spent_tick = 0
        t = 0
        while t < self.tick_mod:
            total_spent_tick += int(1000 * (1.2 ** t))
            t += 1

        return total_spent_tick

    # Getters
    def get_click_mod(self):
        return self.click_mod

    def get_tick_mod(self):
        return self.tick_mod

    def get_click_mod_buy(self):
        return self.click_mod_buy

    def get_tick_mod_buy(self):
        return self.tick_mod_buy

    def get_click_mod_sell(self):
        return self.click_mod_sell

    def get_tick_mod_sell(self):
        return self.tick_mod_sell

    # Setters
    def set_click_mod(self, cm):
        self.click_mod = cm
        self.click_mod_buy = int(100 * (1.1 ** cm))
        self.click_counter.set_current_count(cm)

        if cm == 0:
            self.click_mod_sell = 0
        else:
            self.click_mod_sell = int(100 * (1.1 ** (cm - 1)))

    def set_tick_mod(self, tm):
        self.tick_mod = tm
        self.tick_mod_buy = int(1000 * (1.2 ** tm))
        self.tick_counter.set_current_count(tm)

        if tm == 0:
            self.tick_mod_sell = 0
        else:
            self.tick_mod_sell = int(1000 * (1.2 ** (tm - 1)))
