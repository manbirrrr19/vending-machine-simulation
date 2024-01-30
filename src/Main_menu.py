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
import time
led.init()
adc.init()
buzzer.init()

moisture_sensor.init()
input_switch.init()
ir_sensor.init()
reader = rfid_reader.init()

# Initialize the lcd class
lcd_instance = LCD()
# Define each drink as a variable
Coke = "1: Coke"
Fanta = "2: Fanta"
Sprite = "3: Sprite"
Milo = "4: Milo"
Green_Tea = "5: Green Tea"
Pepsi = "6: Pepsi"

# Group the drinks into top and bottom lists
drinks_top = [Coke, Sprite, Green_Tea]
drinks_bottom = [Fanta, Milo, Pepsi]

while True:
    for i in range(len(drinks_top)):
        # Clear the LCD
        lcd_instance.lcd_clear()

        # Display the drink from the top list
        lcd_instance.lcd_display_string(drinks_top[i], 1)

        # Display the drink from the bottom list
        lcd_instance.lcd_display_string(drinks_bottom[i], 2)

        # Wait for 5 seconds
        time.sleep(5)

 