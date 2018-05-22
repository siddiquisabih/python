class Decrement():
    def __init__(self, value):
        self.value = value

    def dec(self):
        self.value = self.value - 1
        return self.value