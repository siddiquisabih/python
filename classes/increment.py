class Increment():
    def __init__(self, value):
        self.value = value


    def inc(self):
        self.value = self.value + 1

        return self.value
