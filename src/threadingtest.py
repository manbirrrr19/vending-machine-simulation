#git submodule update --init
import time
\
import queue
from flask import render_template


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

# Initialize the lcd class
lcd_instance = LCD.lcd()
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


def Burglar_system():
    while True:
        alarm_status = 0
        accelerometer.setTapDetection()
        alarm_status = accelerometer.getTapDetection()
        print(alarm_status)
        if alarm_status == 2:
            alarm()
            alarm_status = 0
        time.sleep(0.5)

def website_run():
    app.run(debug=True,host='0.0.0.0', port=5001, use_reloader=False)
    time.sleep(15)

def alarm():
    for x in range(10):
        buzzer.turn_on()
        time.sleep(0.25)
        buzzer.turn_off()
        time.sleep(0.1)

def main():
    while True:
        alarm_status = 0
        accelerometer.setTapDetection()
        alarm_status = accelerometer.getTapDetection()
        print(alarm_status)
        if alarm_status == 2:
            alarm()
            alarm_status = 0
        time.sleep(0.5)

def display_main_menu():
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

def dispensing(drink):
    servo.init()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    
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

def check_drink():
    keyvalue = shared_keypad_queue.get()
    drink = {1: "coke", 2: "sprite",3:"fanta",4:"greentea",5:"pepsi",6:"milo"}.get(keyvalue)
    if drink:
        return drink      
def servicing():
    while True:
        keyvalue = shared_keypad_queue.get()
        if keyvalue==("#"):
            for x in range(3):
                buzzer.turn_on()
                time.sleep(0.5)
                buzzer.turn_off()
                time.sleep(0.5)
        time.sleep(0.3)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sales')
def sales():
    return render_template("sales.html", profits=profits)

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/order')
def order():
    return render_template("order.html")

profits = 200

if __name__ == '__main__':
    Burglar_system_thread = threading.Thread(target=Burglar_system)
    Website_thread = threading.Thread(target=website_run)
    Main_menu_thread = threading.Thread(target=display_main_menu)
    keypad_thread = Thread(target=keypad.get_key)
    #servicing_thread = Thread(target=servicing)
    """
    try to change to threading check for what button press i.e press 1 = dispense drink press # = servicing
    so rpi doesnt die
    max might be 5 thread but depends on delays
    """
    Burglar_system_thread.start()
    Website_thread.start()
    Main_menu_thread.start()
    keypad_thread.start()   
    #servicing_thread.start()
    while True:
        if check_drink():
            dispensing(check_drink()) 
        
 
    