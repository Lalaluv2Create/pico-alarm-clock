# Don't Be Late to Work! - Alarm Clock

## About
- This is a countdown alarm clock project I made for my CS 390 Embedded Systems class
- It uses a Raspberry Pi Pico and MicroPython to create an interactive alarm clock that can be set using a 3x4 keypad
- When the countdown reaches zero, a buzzer plays a repeating melody and an LED indicates that the alarm is going off

## Features 
- Set a countdown timer using a 3x4 matrix keypad
- Play a repeating melody using a buzzer
- Adjust the buzzer volume using a potentiometer
- Use an LED to indicate the alarm
- Stop the alarm using a physical button
- Set another countdown without restarting the Pico

## Components Used 
- Raspberry Pi Pico
- 3x4 matrix keypad
- Buzzer
- LED
- Potentiometer
- Push button
- Breadboard and jumper wires

## Pin Connections 
- | Component | Pico GPIO Pin |
- | Keypad Column 1 | GP3 |
- | Keypad Column 2 | GP4 |
- | Keypad Column 3 | GP5 |
- | Keypad Row 1 | GP6 |
- | Keypad Row 2 | GP7 |
- | Keypad Row 3 | GP8 |
- | Keypad Row 4 | GP9 |
- | Alarm LED | GP17 |
- | Stop Button | GP15 |
- | Potentiometer | GP27 (ADC) |
- | Buzzer | GP16 |

## How to Use
1. Connect the Raspberry Pi Pico to your computer
2. Open "main.py" in Thonny or another MicroPython-compatible editor
3. Run the program on the Pico
4. Enter a countdown time in seconds using the keypad
5. Press "#" to confirm the time and start the countdown
6. When the countdown reaches zero, the buzzer plays a melody, and the LED indicates the alarm
7. Press the stop button to silence the alarm
8. Enter another time to play again


## Keypad Controls:
- "0-9": Enter the countdown time in seconds
- "#": Confirm the entered time
- "*": Clear the entered time

## FIles
- "main.py" - Main alarm clock program
- "Hardware Setup.pdf" - Hardware Setup and wiring instructions
- "User Guide.pdf" - Instructions for using the alarm clock

## What I Learned
- How to scan a matrix keypad for user input
- How to use GPIO pins for digital input and output
- How to use PWM to control a buzzer
- How to read analog input from a potentiometer
- How to measure elapsed time using milliseconds
- How to organize an embedded systems project using functions

## Future Improvements
- Add a motion sensor so the user can wave a hand to snooze the alarm
- Implement a 15-second snooze feature
- Add multiple alarm melodies
- Add different alarm settings
