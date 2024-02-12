import time
from threading import Thread
import queue

from hal import hal_lcd as LCD
from hal import hal_keypad as keypad
from hal import hal_servo as servo

stock_of_coke = 1000
stock_of_sprite = 1000
stock_of_fanta = 1000
stock_of_greentea = 1000
stock_of_pepsi = 1000
stock_of_milo = 1000
restock_choice = None



#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()
def key_pressed(key):
    shared_keypad_queue.put(key)
keypad.init(key_pressed)

    
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


    global restock_choice

    while True:
        lcd.lcd_display_string("Restocking...", 1)
        lcd.lcd_display_string("Select 1-6", 2)
        keyvalue = 0
        keyvalue = shared_keypad_queue.get()
        if (keyvalue == 1 or keyvalue == 2 or keyvalue == 3 or keyvalue == 4 or keyvalue == 5 or keyvalue == 6):
            restock_choice = keyvalue
            restock_p2()
            break



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

    added_stock = []

    
    if restock_choice == 1:
        lcd.lcd_display_string("Coke stock: " + str(stock_of_coke), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)
    elif restock_choice == 2:
        lcd.lcd_display_string("Sprite stock: " + str(stock_of_sprite), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)
    elif restock_choice == 3:
        lcd.lcd_display_string("Fanta stock: " + str(stock_of_fanta), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)
    elif restock_choice == 4:
        lcd.lcd_display_string("GT stock: " + str(stock_of_greentea), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)
    elif restock_choice == 5:
        lcd.lcd_display_string("Pepsi stock: " + str(stock_of_pepsi), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)
    elif restock_choice == 6:
        lcd.lcd_display_string("Milo stock: " + str(stock_of_milo), 1)
        for i in range(10):
            lcd.lcd_display_string("Add: ", 2)
            keyvalue= shared_keypad_queue.get()
            if keyvalue == '*':
                break
            else:
                lcd.lcd_display_string(str(keyvalue),2,i+5)
                added_stock.append(keyvalue)

    lcd.lcd_clear()
    restocked_val = ''.join(map(str,added_stock)) if added_stock else 0
    if restock_choice == 1:
        stock_of_coke += int(restocked_val)
        lcd.lcd_display_string("Coke stock: ",1)
        lcd.lcd_display_string(str(stock_of_coke) ,2)
    elif restock_choice == 2:
        stock_of_sprite += int(restocked_val)
        lcd.lcd_display_string("Sprite stock: ",1)
        lcd.lcd_display_string(str(stock_of_sprite) ,2)
    elif restock_choice == 3:
        stock_of_fanta += int(restocked_val)
        lcd.lcd_display_string("Fanta stock: ",1)
        lcd.lcd_display_string(str(stock_of_fanta) ,2)
    elif restock_choice == 4:
        stock_of_greentea += int(restocked_val)
        lcd.lcd_display_string("GT stock: ",1)
        lcd.lcd_display_string(str(stock_of_greentea) ,2)
    elif restock_choice == 5:
        stock_of_pepsi += int(restocked_val)
        lcd.lcd_display_string("Pepsi stock: ",1)
        lcd.lcd_display_string(str(stock_of_pepsi) ,2)
    elif restock_choice == 6:
        stock_of_milo += int(restocked_val)
        lcd.lcd_display_string("Milo stock: ",1)
        lcd.lcd_display_string(str(stock_of_milo) ,2)

    time.sleep(3)
    lcd.lcd_clear()
    lcd.lcd_display_string("Restocking done.",1)
    time.sleep(3)
    lcd.lcd_clear() #go back to main
        


if __name__ == "__main__":
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    stock_of_coke = 100
    stock_of_sprite = 100
    stock_of_fanta = 100
    stock_of_greentea = 100
    stock_of_pepsi = 100
    stock_of_milo = 100
    restock_choice = None
    restocking_p1()
    