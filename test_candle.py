from candle import Candle 

def test_str_returns_all_details():
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    result = candle1.__str__()
    assert result == "Candle name: Beach, ID: 54, fragrance: lavender, Candle type: square, Burn time: 4 hours, Dimensions: 10cm by 10cm, Price: £100" 
    
def test_new_candle_correct(): 
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    assert candle1.name == "Beach"
    assert candle1.id == 54
    assert candle1.fragrance == "lavender"
    assert candle1.candle_type == "square"
    assert candle1.burn_time == "4 hours"
    assert candle1.dimensions == "10cm by 10cm"
    assert candle1.price == "£100"

