import time
from threading import Thread
import queue

from hal import hal_lcd as LCD
from hal import hal_servo as servo

#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()

def key_pressed(key):
    shared_keypad_queue.put(key)

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


if __name__ == "__main__":
    dispensing("fanta")