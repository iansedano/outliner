class Counter:
    def __init__(
        self,
        start,
        item_count=None,
        increment=1,
        pad=None
    ):
        self.start = start
        self.item_count = item_count
        self.increment = increment
        self.state = start
        self.pad = pad
        
    def i(self):
        self.state += self.increment
        return self.print_pad(self.state)

    def print_pad(self, number):
        s = str(number)
        diff = self.pad - len(s)
        
        if diff < 0:
            raise Exception("number overflow, increase pad")
        
        return (diff * "0") + s + "-"