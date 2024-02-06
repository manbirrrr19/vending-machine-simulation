import time
from threading import Thread
import queue

from hal import hal_rfid_reader as rfid_reader
from hal import hal_lcd as lcd

def read_rfid(id):
    lcd.lcd_display_string("Reading RFID..." , 1)           
    id = rfid_reader.read_id_no_block()
    id = str(id)
        
    if id != "None":
        print("RFID card ID = " + id)
        # Display RFID card ID on LCD line 2
        lcd.lcd_display_string(id, 2) 

    return id  

def check_record(rfid_id):
    for item in id_record:
        if int(item["rfid_id"]) ==int(rfid_id) :
            print ("RFID has already been recorded before.")



            return 1
        else: 
            print("RFID has not been recorded")
            amount = float(input("Enter the amount you want to top up: $"))
            new_account = {rfid_id, amount}
            id_record.append(new_account)
            return "account created"            


id_record = [{"rfid_id": 12345678, "account_balance": 100}]

def main():
    read_rfid();


if __name__ == '__main__':
    main()

