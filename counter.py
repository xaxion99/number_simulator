class Counter:

    # Constructor
    def __init__(self, current_count=0):
        self.current_count = current_count

    # Functions to increment or decrement counter
    def increment(self, amount):
        self.current_count += amount

    def decrement(self, amount):
        if self.current_count - amount <= 0:
            self.current_count = 0
        else:
            self.current_count -= amount

    # Getter
    def get_current_count(self):
        return self.current_count

    # Setter
    def set_current_count(self, cc):
        self.current_count = cc
