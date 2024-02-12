import time
from threading import Thread
import queue

from hal import hal_rfid_reader as rfid_reader
from hal import hal_lcd as lcd

#   initialisation 
lcd = lcd.lcd()
lcd.lcd_clear()

reader = rfid_reader.init()

id_record = [{"rfid_id": 12345678, "account_balance": 100}]
stock = {"coke": 20, "sprite": 20, "fanta": 20, "green_tea": 20, "milo": 20, "pepsi": 20}

def read_rfid():
    lcd.lcd_display_string("Reading RFID..." , 1)           
    time.sleep(5) 
    id = reader.read_id_no_block()
    id = str(id)
    
    if id != "None":
        print("RFID card ID = " + id)
    lcd.lcd_clear()
    return id  

def check_record(rfid_id):
    for item in id_record:
        if str(rfid_id) == str(item["rfid_id"]) : 
            print ("RFID has already been recorded before.")
            return 1
        
    print("RFID has not been recorded")
    if rfid_id != "None": 
        amount = 50
        new_account = {"rfid_id": str(rfid_id), "account_balance": amount}
        id_record.append(new_account)
        print(id_record)
        return 1
    else: 
        lcd.lcd_display_string("Not detected" , 1) 
        time.sleep(5) 
        return 0   
    
def payment(rfid_id):
    for record in id_record:
        if str(record["rfid_id"]) == str(rfid_id):
            record["account_balance"] -= 1.50
            print(record["account_balance"])
            lcd.lcd_display_string("Your balance is:", 1)      
            lcd.lcd_display_string("$" + str(record["account_balance"]), 2) 
            return 1

def update_stock(): 
    print ("1.Coke \n 2.Sprite \n 3.Fanta \n 4.Green Tea \n 5.Milo \n 6.Pepsi")
    choice = int(input("Enter choice: "))
    if choice == 1: 
        stock["coke"] -= 1
    elif choice == 2:
        stock["sprite"] -= 1
    elif choice == 3:
        stock["fanta"] -= 1
    elif choice == 4:
        stock["green_tea"] -= 1
    elif choice == 5:
        stock["milo"] -= 1
    elif choice == 6:
        stock["pepsi"] -= 1


def main():
    rfid_id = read_rfid()
    check_record(rfid_id)

    while check_record(rfid_id) == 0:
        rfid_id = read_rfid()
        if check_record(rfid_id):
            payment(rfid_id)
        if payment(rfid_id):
            update_stock() 

if __name__ == '__main__':
    main()