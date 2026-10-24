from machine import Pin, PWM, ADC #buzzer & potentiometer
from time import sleep_ms, ticks_ms, ticks_diff 

#Setting up the pins for each component

#3x4 keypad pins
c1 = Pin(3, Pin.IN, Pin.PULL_UP)
c2 = Pin(4, Pin.IN, Pin.PULL_UP)
c3 = Pin(5, Pin.IN, Pin.PULL_UP)

r1 = Pin(6, Pin.OUT)
r2 = Pin(7, Pin.OUT)
r3 = Pin(8, Pin.OUT)
r4 = Pin(9, Pin.OUT)

#Alarm LED
alarm_led = Pin(17, Pin.OUT)

#Stop Button
stop_button = Pin(15, Pin.IN, Pin.PULL_DOWN)

#Motion Sensor 
#motion_sensor = Pin(13, Pin.IN)

#Potentiometer
potentiometer = ADC(27)

#Buzzer
buzzer_pin = Pin(16, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

#Setting up the keyboard rows and columns
rows = [r1, r2, r3, r4]
cols = [c1, c2, c3]

#Map of physical keypad
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#'],
    ]

#alarm ringtone
melody = [262, 294, 330, 349, 392]
note_times = [300, 300, 300, 300, 500]

#get_key(): read the keypad
def get_key():
    #inside every row check the column
    for row in rows:
        row.value(1) #output a high signal
        
    #go through rows, and it gives the index and row    
    for row_index, row in enumerate(rows):
        row.value(0)
        #go through columns
        for col_index, col in enumerate(cols):
            if col.value() == 0:
                key = keys[row_index][col_index]
                
                row.value(1)
                sleep_ms(200) #debouncing
                return key
            
        row.value(1)
    #if no key is being pressed   
    return None
    
#get_alarm_time(): gets the countdown time from the keypad
def get_alarm_time():
    entered_time = ""
    while True:
        key = get_key()
        if key is not None:
            print("Key pressed:", key)

            if key == '#':
                if entered_time != "":
                    break
            elif key == '*':
                entered_time = ""
            else:
                entered_time = entered_time + key

            print("Entered time:", entered_time)

    return int(entered_time)
    
#countdown(seconds)
def countdown(seconds):
    start_time = ticks_ms() #current time
    
    while True:
        elapsed_time = ticks_diff(ticks_ms(), start_time) # how many milliseconds have passed since we started
        remaining_time = seconds - (elapsed_time // 1000)
        
        print(remaining_time)
        
        if remaining_time <= 0:
            break
        
        sleep_ms(1000)

#helper func
def check_alarm_controls():
    if stop_button.value() == 1:
        return "stop"
    
   # if motion_sensor.value() == 1:
      #  return "snooze"
    
    return None
    
#creating the alarm
def alarm():
    while True:
        
        #play each note in the melody
        for i in range(len(melody)):
            buzzer_pwm.freq(melody[i])
            set_volume()
            
            alarm_led.value(0)
            
            #keep checking controls while note is playing
            note_start = ticks_ms()
            
            while ticks_diff(ticks_ms(), note_start) < note_times[i]:
                action = check_alarm_controls()
                
                if action == "stop":
                    buzzer_pwm.duty_u16(0)
                    alarm_led.value(1)
                    return
                
               # elif action == "snooze":
                   # snooze()
                   # break
                
                sleep_ms(50)
            
            buzzer_pwm.duty_u16(0)
            alarm_led.value(1)
            sleep_ms(50)
        
        #go back and repeat the melody
        
#Motion sensor snooze the alarm
def snooze():
    buzzer_pwm.duty_u16(0)
    alarm_led.value(1)
    
    sleep_ms(15000)

#set_volume(): control buzzer volume with the potentiometer
def set_volume():
    volume = potentiometer.read_u16()
    buzzer_pwm.duty_u16(volume)

#main program:
while True: #keeps the alarm clock running instead of finishing after one alarm
    alarm_time = get_alarm_time()
    
    print("Alarm set for", alarm_time, "seconds")
    
    countdown(alarm_time)
    
    alarm()
