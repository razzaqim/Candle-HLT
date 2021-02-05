class Catalogue:

    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.candles_list = []

    def list_all_candles(self):
        return self.candles_list

    def add_candle(self, new_candle):
        self.candles_list.append(new_candle)
        return self.candles_list

    def delete_candle(self, id):
        found = False
        for candle in self.candles_list:
            if id == candle.id:
                self.candles_list.remove(candle)
                found = True
        if not found:
            raise ValueError("Item not found")

    def update_candle_price(self, id, new_price):
        found = False
        for candle in self.candles_list:
             if id == candle.id:
                candle.price = new_price
                found = True
        if not found:
            raise ValueError("Item not found")


