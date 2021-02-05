class Candle: 
        
    def __init__(self, name, id, fragrance, candle_type, burn_time, dimensions, price):
             self.name = name
             self.id = id
             self.fragrance = fragrance
             self.candle_type = candle_type
             self.burn_time = burn_time
             self.dimensions = dimensions
             self.price = price

    def __str__(self):
            return f"Candle name: {self.name}, ID: {self.id}, fragrance: {self.fragrance}, Candle type: {self.candle_type}, Burn time: {self.burn_time}, Dimensions: {self.dimensions}, Price: {self.price}"