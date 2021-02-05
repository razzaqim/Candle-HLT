from catalogue import Catalogue
from candle import Candle 
import pytest

def test_new_catalogue_correct(): 
    cat = Catalogue("2021 catalogue")
    assert cat.cat_name == "2021 catalogue"
    assert cat.candles_list == []

def test_list_all_candles_empty_for_new_cat():
    cat = Catalogue("2021 catalogue")
    list_candles = cat.list_all_candles()
    assert list_candles == []

def test_add_candle_puts_candle_in_list():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    assert cat.candles_list == [candle1]

def test_add_candle_puts_two_candles_in_list():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    candle2 = Candle("Beach", 2, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    cat.add_candle(candle2) 
    assert cat.candles_list == [candle1, candle2]

def test_delete_candle_removes_the_candle_from_list():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    candle2 = Candle("Beach", 2, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    cat.add_candle(candle2) 
    cat.delete_candle(54)
    assert cat.candles_list == [candle2]

def test_delete_both_candles_gives_empty_list():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    candle2 = Candle("Beach", 2, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    cat.add_candle(candle2) 
    cat.delete_candle(54)
    cat.delete_candle(2)
    assert cat.candles_list == []

def test_delete_candle_gives_error_if_candle_not_in_list():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    candle2 = Candle("Beach", 2, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    candle3 = Candle("Beach", 3, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    cat.add_candle(candle2) 
    with pytest.raises(ValueError):
        cat.delete_candle(candle3)
    assert cat.candles_list == [candle1, candle2]
    with pytest.raises(ValueError) as error:
        cat.delete_candle(candle3)
    assert str(error.value) == "Item not found"

def test_update_price_changes_to_new_price():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    cat.update_candle_price(54, "£80")
    assert candle1.price == "£80"

def test_update_price_on_id_not_found_gives_error():
    cat = Catalogue("2021 catalogue")
    candle1 = Candle("Beach", 54, "lavender", "square", "4 hours", "10cm by 10cm", "£100")
    cat.add_candle(candle1)
    with pytest.raises(ValueError) as e:
        cat.update_candle_price(2, "£80")
    assert str(e.value) == "Item not found"
