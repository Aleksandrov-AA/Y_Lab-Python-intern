class CyclicIterator:
    def __init__(self, value_range):
        self.current = value_range[0] - 1
        self.value_range = value_range

        self.stop_value = value_range[-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        else:
            self.current = self.value_range[0] - 1
            self.current += 1
            return self.current