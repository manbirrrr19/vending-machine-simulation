import time
from threading import Thread
import queue

from hal import hal_lcd as LCD
from hal import hal_keypad as keypad
from hal import hal_servo as servo



#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()
def key_pressed(key):
    shared_keypad_queue.put(key)
keypad.init(key_pressed)

def key_pressed(key):
    shared_keypad_queue.put(key)

def restocking_p1():
    servo.init()
    lcd = LCD.lcd()
    lcd.lcd_clear()

    global stock_of_coke
    global stock_of_sprite
    global stock_of_fanta
    global stock_of_greentea
    global stock_of_pepsi
    global stock_of_milo

    stock_of_coke_str = str(stock_of_coke)
    stock_of_sprite_str = str(stock_of_sprite)
    stock_of_fanta_str = str(stock_of_fanta)
    stock_of_greentea_str = str(stock_of_greentea)
    stock_of_pepsi_str = str(stock_of_pepsi)
    stock_of_milo_str = str(stock_of_milo)

    
    while True:
        keyvalue= shared_keypad_queue.get() 
        if keyvalue == '#':    #For YueHang to add to check for input 
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("1.Coke: ", stock_of_coke_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("2.Sprite: ", stock_of_sprite_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("3.Fanta: ", stock_of_fanta_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("4.Green Tea: ", stock_of_greentea_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("5.Pepsi: ", stock_of_pepsi_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)
                lcd.lcd_display_string("Restocking...", 1)
                lcd.lcd_display_string("6.Milo: ", stock_of_milo_str, 2)
                restock_choice = check_restocking_choice()
                if restock_choice is not None:
                    restock_p2()
                time.sleep(1)

def check_restocking_choice():
    keyvalue = shared_keypad_queue.get()
    choice = {1: "coke", 2: "sprite",3:"fanta",4:"greentea",5:"pepsi",6:"milo",}.get(keyvalue)
    if choice:
        return choice   

def restock_p2():
     
    servo.init()
    lcd = LCD.lcd()
    lcd.lcd_clear()

    global stock_of_coke
    global stock_of_sprite
    global stock_of_fanta
    global stock_of_greentea
    global stock_of_pepsi
    global stock_of_milo
    global restock_choice

    stock_of_coke_str = str(stock_of_coke)
    stock_of_sprite_str = str(stock_of_sprite)
    stock_of_fanta_str = str(stock_of_fanta)
    stock_of_greentea_str = str(stock_of_greentea)
    stock_of_pepsi_str = str(stock_of_pepsi)
    stock_of_milo_str = str(stock_of_milo)

    added_stock = []
    global restock_choice

    
    if restock_choice == 1:
        lcd.lcd_display_string("Coke stock: " + stock_of_coke_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)
    elif restock_choice == 2:
        lcd.lcd_display_string("Sprite stock: " + stock_of_sprite_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)
    elif restock_choice == 3:
        lcd.lcd_display_string("Fanta stock: " + stock_of_fanta_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)
    elif restock_choice == 4:
        lcd.lcd_display_string("GT stock: " + stock_of_greentea_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)
    elif restock_choice == 5:
        lcd.lcd_display_string("Pepsi stock: " + stock_of_pepsi_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)
    elif restock_choice == 6:
        lcd.lcd_display_string("Milo stock: " + stock_of_milo_str, 1)
        prev_keyvalue = keyvalue
        for i in range(10):
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string("Add: " + str(keyvalue), 2, i+5)
                added_stock.append(added_stock)

    lcd.lcd_clear()
    restocked_val = ''.join(map(int, added_stock))
    if prev_keyvalue == 1:
        stock_of_coke += restocked_val
        stock_of_coke_str = str(stock_of_coke)   
        lcd.lcd_display_string("Coke stock: ",1)
        lcd.lcd_display_string(stock_of_coke_str ,2)
    elif prev_keyvalue == 2:
        stock_of_sprite += restocked_val
        stock_of_sprite_str = str(stock_of_sprite)
        lcd.lcd_display_string("Sprite stock: ",1)
        lcd.lcd_display_string(stock_of_sprite_str ,2)
    elif prev_keyvalue == 3:
        stock_of_fanta += restocked_val
        stock_of_fanta_str = str(stock_of_fanta)
        lcd.lcd_display_string("Fanta stock: ",1)
        lcd.lcd_display_string(stock_of_fanta_str ,2)
    elif prev_keyvalue == 4:
        stock_of_greentea += restocked_val
        stock_of_greentea_str = str(stock_of_greentea)
        lcd.lcd_display_string("Green Tea stock: ",1)
        lcd.lcd_display_string(stock_of_greentea_str ,2)
    elif prev_keyvalue == 5:
        stock_of_pepsi += restocked_val
        stock_of_pepsi_str = str(stock_of_pepsi)
        lcd.lcd_display_string("Pepsi stock: ",1)
        lcd.lcd_display_string(stock_of_pepsi_str ,2)
    elif prev_keyvalue == 6:
        stock_of_milo += restocked_val
        stock_of_milo_str = str(stock_of_milo)
        lcd.lcd_display_string("Milo stock: ",1)
        lcd.lcd_display_string(stock_of_milo_str ,2)

        time.sleep(3)
        lcd.lcd_display_string("Restocking done.",1)
        time.sleep(3)
        lcd.lcd_clear()
        


if __name__ == "__main__":
    stock_of_coke = 1000
    stock_of_sprite = 1000
    stock_of_fanta = 1000
    stock_of_greentea = 1000
    stock_of_pepsi = 1000
    stock_of_milo = 1000
    restock_choice = None
    