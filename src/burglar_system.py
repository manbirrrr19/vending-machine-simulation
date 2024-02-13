import time
from threading import Thread
import queue

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
import requests

accelerometer = accel.init()
buzzer.init()

TELEGRAM_BOT_TOKEN = '6533036701:AAFLGg9h-M3Ba68HY3osZuO-dOV2eoLNuRA'
CHAT_ID = '5271825143'

def alarm():
    for x in range(10):
        buzzer.turn_on()
        time.sleep(0.25)
        buzzer.turn_off()
        time.sleep(0.1)

def Burglar_system():
    while True:
        alarm_status = 0
        accelerometer.setTapDetection()
        alarm_status = accelerometer.getTapDetection()
        #print(alarm_status)
        if alarm_status == 2:
            #alarm()
            alert_message = "Alert! Your vending machine is being burglarized"
            print(requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={alert_message}").json())
            alarm_status = 0
        time.sleep(0.5)



if __name__ == '__main__':
    Burglar_system()