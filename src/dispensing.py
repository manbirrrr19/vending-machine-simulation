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

def dispensing(drink):
    servo.init()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    lcd = LCD.lcd()
    lcd.lcd_clear()

    if drink == "coke":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Coca-Cola...",2)
        servo.set_servo_position(30)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)
    elif drink == "sprite":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Sprite...",2)
        servo.set_servo_position(60)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)
    elif drink == "fanta":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Fanta...",2)
        servo.set_servo_position(90)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)
    elif drink == "greentea":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Green Tea...",2)
        servo.set_servo_position(120)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)
    elif drink == "pepsi":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Pepsi...",2)
        servo.set_servo_position(150)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)
    elif drink == "milo":
        lcd.lcd_display_string("Dispensing",1)
        lcd.lcd_display_string("Milo...",2)
        servo.set_servo_position(180)
        time.sleep(3)
        lcd.lcd_clear
        servo.set_servo_position(0)


if __name__ == "__main__":
    dispensing("fanta")