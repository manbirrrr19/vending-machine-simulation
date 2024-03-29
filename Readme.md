# Smart Vending Machine
Our Smart Vending Machine which allows customers to purchase a drink physically as the machine and pay using an RFID Tag and Scanner. It includes an anti-burglary system which detects whether the machine is being forcefully opened. A valid user code can be used to open the vending machine without triggering the alarm in order to service or restock. Project is done using Python

# Project Developers
- Drew ~ 2110123
- Manbir ~ 2224107
- Yue Hang ~ 2204554
- Zi Qiong ~ 2223924

# Components Used

| Component Name       | Usage                                                                                  | Requirements                                                                                                                                                                                                                                                                                 |
|----------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RFID Scanner         | Simulate payment for the drinks                                                        | - The drinks vending machine shall allow customers to purchase drinks physically at the vending machine or remotely via their smartphones or an external website                                                                                                                             |
| LCD                  | Display information to the customers                                                   | - At the vending machine the customers can select their drink/s using the numeric keypad and the LCD screen                                                                                                                                                                                  |
| Keypad               | Input for drink selection and password input for servicing                             | - At the vending machine the customers can select their drink/s using the numeric keypad and the LCD screen - For service technicians and drinks suppliers, they need to enter a valid user code on the keypad in order to open the vending machine door without triggering the buzzer alarm |
| LED                  | Indicates whether the vending machine is opened for servicing                          | - For service technicians and drinks suppliers, they need to enter a valid user code on the keypad in order to open the vending machine door without triggering the buzzer alarm                                                                                                             |
| Buzzer               | Used as an alarm when burglary is detected (attempt in forcefully opening the machine) | - If the vending machine detects that there has been an attempt to forcefully open it then the buzzer shall be activated                                                                                                                                                                     |                                                                                                           
| Servo Motor          | Use to dispense drinks                                                                 | - The drinks vending machine shall allow customers to purchase drinks physically at the vending machine or remotely via their smartphones or an external website                                                                                                                             |
| 3-Axis Accelerometer | Detects whether the machine is being forcefully opened                                 | - To avoid any theft of the drinks, the vending machine shall implement a burglar detection system to detect if the door of the vending machine has been forcefully pried open                                                                                                               |

# How to set up
Run the commands <br>
`
docker pull druuuw/devopsgrp4:latest 
` <br>
followed by <br>
`
docker container run --privileged -dp 5001:5001 devopsgrp4
`
# Video Demo
[Link Here](https://youtu.be/IlhguRAQusw)
