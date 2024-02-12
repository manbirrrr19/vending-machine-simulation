import time
from threading import Thread
import threading
import queue
from flask import render_template

import Main_menu as main_menu 
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
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_usonic as usonic
from hal import hal_dc_motor as dc_motor
from hal import hal_accelerometer as accel
from flask import Flask
import threadingtest
import burglar_system
import Testwebsite

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

lcd_instance = LCD.lcd()
menu_status = True

Coke = "1: Coke"
Fanta = "2: Fanta"
Sprite = "3: Sprite"
Milo = "4: Milo"
Green_Tea = "5: Green Tea"
Pepsi = "6: Pepsi"

TELEGRAM_BOT_TOKEN = '6533036701:AAFLGg9h-M3Ba68HY3osZuO-dOV2eoLNuRA'
CHAT_ID = '5271825143'

# Group the drinks into top and bottom lists
drinks_top = [Coke, Sprite, Green_Tea]
drinks_bottom = [Fanta, Milo, Pepsi]

def check_choice():
    keyvalue = shared_keypad_queue.get()
    choice = {1: "coke", 2: "sprite",3:"fanta",4:"greentea",5:"pepsi",6:"milo",}.get(keyvalue)
    if choice:
        return choice   

def dispensing(drink):
    servo.init()
    
    lcd = LCD.lcd()
    lcd.lcd_clear()

    drink_positions = {
        "coke": 30,
        "sprite": 60,
        "fanta": 90,
        "greentea": 120,
        "pepsi": 150,
        "milo": 180
    }

    position = drink_positions.get(drink)
    if position is not None:
        lcd.lcd_display_string("Dispensing", 1)
        lcd.lcd_display_string(f"{drink.capitalize()}...", 2)
        servo.set_servo_position(position)
        time.sleep(3)
        lcd.lcd_clear()
        servo.set_servo_position(0)
    else:
        lcd.lcd_display_string("Invalid drink", 1)

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
    global timer_password
    timer_password = 5
    password = "1234"
    lcd_instance.lcd_display_string("Enter PIN: ",1)
    password_key = ""
    global menu_status
    
    
    for x in range (0,4):
        print(x)
        keyvalue = shared_keypad_queue.get()
        if keyvalue:
            lcd_instance.lcd_display_string(str(keyvalue),1,10+x)
            password_key += (str(keyvalue))
        
    if password_key == password:
        print("password works")
        
        menu_status = True
    else:
        print("password wrong")
        menu_status = True
        

def main():
    global menu_status
    burglar_alarm_thread = threading.Thread(target=burglar_system.Burglar_system)
    main_menu_thread = threading.Thread(target=display_drinks, args=(drinks_top,drinks_bottom,lcd_instance))
    website_thread = threading.Thread(target=Testwebsite.website_run)
    keypad_thread = threading.Thread(target=threadingtest.keypad.get_key)
    timer_thread = threading.Thread(target=timer)

    timer_thread.start()
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
            dispensing(drinks)
            menu_status = True

        elif keyvalue == "#":
            print("hello")
            menu_status = False
            lcd_instance.lcd_clear()
            check_password()


            

if __name__ == '__main__':
    main()
