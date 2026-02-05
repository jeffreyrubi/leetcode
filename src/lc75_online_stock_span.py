class StockSpanner:

    def __init__(self):
        self.last_prices = []
        self.last_span = []
        self.end = -1
    
    def trace(self, price: int, index: int) -> int:
        if self.last_prices[index] > price or index < 0:
            return 0
        else:
            return self.last_span[index] + self.trace(price, index-self.last_span[index])
    
    def next(self, price: int) -> int:
        if self.end < 0:
            self.last_span.append(1)
        else:
            self.last_span.append(1 + self.trace(price, self.end))

        self.end += 1
        self.last_prices.append(price)
        return self.last_span[self.end]