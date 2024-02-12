import pytest
import Testwebsite as tw

def test_load_sales_data(monkeypatch):
    mock_data = [{'id': 1, 'timestamp': '2022-01-01', 'item': 'coke', 'price': 1.50}]
    monkeypatch.setattr('json.load', lambda _: mock_data)
    result = tw.load_sales_data()
    assert result == mock_data

def test_save_sales_data(monkeypatch):
    sales_data = [{'id': 1, 'timestamp': '2022-01-01', 'item': 'coke', 'price': 1.50}]
    monkeypatch.setattr('json.dump', lambda data, _: data == sales_data)
    tw.save_sales_data(sales_data)

def test_load_stock(monkeypatch):
    mock_data = {"coke": 10, "sprite": 10, "fanta": 10, "green_tea": 10, "milo": 10, "pepsi": 10}
    monkeypatch.setattr('json.load', lambda _: mock_data)
    result = tw.load_stock()
    assert result == mock_data

def test_save_stock(monkeypatch):
    stock = {"coke": 10, "sprite": 10, "fanta": 10, "green_tea": 10, "milo": 10, "pepsi": 10}
    monkeypatch.setattr('json.dump', lambda data, _: data == stock)
    tw.save_stock(stock)

def test_calculate_profits():
    sales_data = [{'id': 1, 'timestamp': '2022-01-01', 'item': 'coke', 'price': 1.50}, {'id': 2, 'timestamp': '2022-01-02', 'item': 'sprite', 'price': 1.50}]
    result = tw.calculate_profits(sales_data)
    assert result == 3.0


def test_update_stock(mocker):
    # Mock the stock data
    mock_stock = {
        "coke": 10,
        "sprite": 10,
        "fanta": 10,
        "green_tea": 10,
        "milo": 10,
        "pepsi": 10
    }

    # Mock the input, load_stock, and save_stock functions
    mocker.patch('builtins.input', return_value='1')
    mocker.patch('Testwebsite.load_stock', return_value=mock_stock)
    mock_save_stock = mocker.patch('Testwebsite.save_stock')

    # Call the function to test
    selected_drink = tw.test_update_stock()

    # Assert the selected drink is 'coke'
    assert selected_drink == 'coke'

    # Assert the 'coke' stock is decreased by 1
    mock_stock['coke'] -= 1
    mock_save_stock.assert_called_once_with(mock_stock)  