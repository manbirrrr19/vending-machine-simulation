import time
from threading import Thread
import threading
import queue
from flask import render_template
import threading
import payment

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_adc as adc
from hal import hal_buzzer as buzzer
from hal import hal_keypad as keypad
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_input_switch as input_switch
from hal import hal_ir_sensor as ir_sensor
from hal import hal_rfid_reader as rfid_reader
from hal import hal_servo as servo
from hal import hal_accelerometer as accel
from flask import Flask
import burglar_system
import Testwebsite
import dispensing

shared_keypad_queue = queue.Queue()
def key_pressed(key):
    shared_keypad_queue.put(key)
keypad.init(key_pressed)

accelerometer = accel.init()
buzzer.init()

led.init()
adc.init()
buzzer.init()

moisture_sensor.init()
input_switch.init()
ir_sensor.init()
reader = rfid_reader.init()

def key_pressed(key):
    shared_keypad_queue.put(key)
keypad.init(key_pressed)

lcd_instance = LCD.lcd()
menu_status = True

Coke = "1: Coke"
Sprite = "2: Sprite"
Fanta = "3: Fanta"
Green_Tea = "4: Green Tea"
Pepsi = "5: Pepsi"
Milo = "6: Milo"

TELEGRAM_BOT_TOKEN = '6533036701:AAFLGg9h-M3Ba68HY3osZuO-dOV2eoLNuRA'
CHAT_ID = '5271825143'

# Group the drinks into top and bottom lists
drinks_top = [Coke, Fanta, Pepsi]
drinks_bottom = [Sprite, Green_Tea, Milo]


def check_choice():
    keyvalue = shared_keypad_queue.get()
    choice = {1: "coke", 2: "sprite",3:"fanta",4:"greentea",5:"pepsi",6:"milo",}.get(keyvalue)
    if choice:
        return choice   

def display_drinks(drinks_top, drinks_bottom, lcd_instance):
    while True:
        if menu_status == True:
            for i in range(len(drinks_top)):
                if menu_status == False:
                    break
                # Clear the LCD
                lcd_instance.lcd_clear()

                # Display the drink from the top list
                lcd_instance.lcd_display_string(drinks_top[i], 1)

                # Display the drink from the bottom list
                lcd_instance.lcd_display_string(drinks_bottom[i], 2)

                # Wait for 5 seconds
                time.sleep(5)
                print(menu_status)
        else:
            print("work")
            time.sleep(5)


def check_password():
    global stock
    global timer_password
    timer_password = 5
    password = "1234"
    lcd_instance.lcd_display_string("Enter PIN: ",1)
    password_key = ""
    global menu_status
    
    
    for x in range (0,4):
        print(x)
        keyvalue = shared_keypad_queue.get()
        if (keyvalue ==1 or keyvalue ==2 or keyvalue ==3 or keyvalue ==4 or keyvalue ==5 or keyvalue ==6 or keyvalue ==7 or keyvalue ==8 or keyvalue ==9 or keyvalue ==0):
            lcd_instance.lcd_display_string(str(keyvalue),1,10+x)
            password_key += (str(keyvalue))
        elif (keyvalue == '#' or keyvalue == '*'):
            continue
        
    if password_key == password:
        global stock_of_coke
        global stock_of_sprite
        global stock_of_fanta
        global stock_of_greentea
        global stock_of_pepsi
        global stock_of_milo
        stock = Testwebsite.load_stock()
        Testwebsite.save_stock(stock)
        stock_of_coke = stock["Coke"]
        stock_of_sprite = stock["Sprite"]
        stock_of_fanta = stock["Fanta"]
        stock_of_greentea = stock["Green Tea"]
        stock_of_pepsi = stock["Pepsi"]
        stock_of_milo = stock["Milo"]
        restock_choice = None
        restocking_p1()
        menu_status = True
    else:
        print("password wrong")
        lcd_instance.lcd_clear()
        lcd_instance.lcd_display_string("Wrong Pin!", 1)
        lcd_instance.lcd_display_string("Pls Try Again", 2)
        time.sleep(1)
        lcd_instance.lcd_clear
        menu_status = True

    return password_key

def main():
    global menu_status
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    burglar_alarm_thread = threading.Thread(target=burglar_system.Burglar_system)
    main_menu_thread = threading.Thread(target=display_drinks, args=(drinks_top,drinks_bottom,lcd_instance))
    website_thread = threading.Thread(target=Testwebsite.website_run)
    
    burglar_alarm_thread.start()
    keypad_thread.start()
    main_menu_thread.start()
    website_thread.start()
    while True:
        keyvalue = shared_keypad_queue.get()

        drink = {1: "coke", 2: "sprite",3:"fanta",4:"greentea",5:"pepsi",6:"milo",} 

        if keyvalue in drink:
            payment_success = 0
            lcd_instance.lcd_clear()
            menu_status = False
            print(keyvalue)
            drinks = drink[keyvalue] 
            rfid_id = payment.read_rfid()
            payment.check_record(rfid_id)
            while payment.check_record(rfid_id) == 0:
                rfid_id = payment.read_rfid()
                if payment.check_record(rfid_id):
                    payment_success = payment.payment(rfid_id)
                if payment_success == 1:
                    Testwebsite.load_sales_data()
                    Testwebsite.load_stock()
                    selected_drink = Testwebsite.update_stock(keyvalue)
                    Testwebsite.update_sales_data(selected_drink)
                    break
            dispensing.dispensing(drinks)
            menu_status = True

        elif keyvalue == "#":
            print("hello")
            menu_status = False
            lcd_instance.lcd_clear()
            check_password()

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
    global menu_status

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
        elif (keyvalue == "*"):
            restock_choice = 0
            lcd_instance.lcd_display_string("Abort Restock")
            lcd_instance.lcd_clear()
            menu_status = True
            break
    return restock_choice


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
    global stock
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
        update_stock_2(restock_choice, stock_of_coke)
    elif restock_choice == 2:
        stock_of_sprite += int(restocked_val)
        lcd.lcd_display_string("Sprite stock: ",1)
        lcd.lcd_display_string(str(stock_of_sprite) ,2)
        update_stock_2(restock_choice, stock_of_sprite)
    elif restock_choice == 3:
        stock_of_fanta += int(restocked_val)
        lcd.lcd_display_string("Fanta stock: ",1)
        lcd.lcd_display_string(str(stock_of_fanta) ,2)
        update_stock_2(restock_choice, stock_of_fanta)
    elif restock_choice == 4:
        stock_of_greentea += int(restocked_val)
        lcd.lcd_display_string("GT stock: ",1)
        lcd.lcd_display_string(str(stock_of_greentea) ,2)
        update_stock_2(restock_choice, stock_of_greentea)
    elif restock_choice == 5:
        stock_of_pepsi += int(restocked_val)
        lcd.lcd_display_string("Pepsi stock: ",1)
        lcd.lcd_display_string(str(stock_of_pepsi) ,2)
        update_stock_2(restock_choice, stock_of_pepsi)
    elif restock_choice == 6:
        stock_of_milo += int(restocked_val)
        lcd.lcd_display_string("Milo stock: ",1)
        lcd.lcd_display_string(str(stock_of_milo) ,2)
        update_stock_2(restock_choice, stock_of_milo)
    
    time.sleep(3)
    lcd.lcd_clear()
    lcd.lcd_display_string("Restocking done.",1)
    time.sleep(3)
    lcd.lcd_clear() #go back to main
        
def update_stock_2(choice,new_stock):
    global stock
    choice -= 1
    drinks = ["Coke", "Sprite", "Fanta", "Green Tea", "Pepsi", "Milo"]
    selected_drink = drinks[choice]
    stock[selected_drink] = new_stock
    Testwebsite.save_stock(stock)
            

if __name__ == '__main__':
    main()