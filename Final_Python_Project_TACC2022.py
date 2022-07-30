########### Start of Header #############
import RPi.GPIO as GPIO
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

red_1_pin = 18
red_2_pin = 19
red_3_pin = 20
red_4_pin = 21
sun_1_pin = 12
sun_2_pin = 25

########## End of Header #############

datafile = 'site-1_FishPond.csv'
style.use('fivethirtyeight')
sensor_data = pd.read_csv(datafile)
sensor_data.head()

for pin in range(18,22):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.LOW)

max_temp = sensor_data["temperature"].max()
print("The maximum temperature in the data is: ", max_temp)
int(np.interp(max_temp, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,22]))

## Cycle through all the values in the data set under Humidity

GPIO.setmode(GPIO.BCM)   ## Allows the use of the GPIO pin numbers instead of the physical pin numbers
GPIO.setup(sun_1_pin,GPIO.OUT)  ## Sets GPIO pin 21 into ouput mode (goes-ousta)
GPIO.setwarnings(False)  ## Removes any warnings if any arose from changing GPIO pin 21's mode
GPIO.output(sun_1_pin,GPIO.HIGH) ## Sets GPIO pin 21 output voltage low/off

for sensorvalue in sensor_data["temperature"]:
    #Interpolate the current value
    pin = int(np.interp(sensorvalue, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,21]))
    #Turn on the number of pins up to the interpolated value
    #print(pin)
    for pins in range(18, pin+1):
        GPIO.output(pins,GPIO.HIGH)
#        print(pin)
    time.sleep(.7)
    #Turn all the pins off before checking the next value
    for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)
    time.sleep(.7)
# Turn all pins off
for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)

time.sleep(4)

datafile = 'site-2_Waterfall.csv'
style.use('fivethirtyeight')
sensor_data = pd.read_csv(datafile)
sensor_data.head()

for pin in range(18,22):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.LOW)

max_temp = sensor_data["temperature"].max()
print("The maximum temperature in the data is: ", max_temp)
int(np.interp(max_temp, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,22]))

## Cycle through all the values in the data set under Humidity
for sensorvalue in sensor_data["temperature"]:
    #Interpolate the current value
    pin = int(np.interp(sensorvalue, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,21]))
    #Turn on the number of pins up to the interpolated value
    #print(pin)
    for pins in range(18, pin+1):
        GPIO.output(pins,GPIO.HIGH)
#        print(pin)
    time.sleep(.7)
    #Turn all the pins off before checking the next value
    for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)
    time.sleep(.7)
# Turn all pins off
for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)

time.sleep(4)

GPIO.output(sun_1_pin,GPIO.LOW) ## Sets GPIO pin 21 output voltage low/off

time.sleep(4)

GPIO.setmode(GPIO.BCM)   ## Allows the use of the GPIO pin numbers instead of the physical pin numbers
GPIO.setup(sun_2_pin,GPIO.OUT)  ## Sets GPIO pin 21 into ouput mode (goes-ousta)
GPIO.output(sun_2_pin,GPIO.HIGH) ## Sets GPIO pin 21 output voltage low/off

datafile = 'site-3_GreatPlains.csv'
style.use('fivethirtyeight')
sensor_data = pd.read_csv(datafile)
sensor_data.head()

for pin in range(18,22):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.LOW)

max_temp = sensor_data["temperature"].max()
print("The maximum temperature in the data is: ", max_temp)
int(np.interp(max_temp, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,22]))

## Cycle through all the values in the data set under Humidity
for sensorvalue in sensor_data["temperature"]:
    #Interpolate the current value
    pin = int(np.interp(sensorvalue, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,21]))
    #Turn on the number of pins up to the interpolated value
    #print(pin)
    for pins in range(18, pin+1):
        GPIO.output(pins,GPIO.HIGH)
#        print(pin)
    time.sleep(.75)
    #Turn all the pins off before checking the next value
    for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)
    time.sleep(.75)
# Turn all pins off
for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)

time.sleep(4)

datafile = 'site-4_Crevice.csv'
style.use('fivethirtyeight')
sensor_data = pd.read_csv(datafile)
sensor_data.head()

for pin in range(18,22):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.LOW)

max_temp = sensor_data["temperature"].max()
print("The maximum temperature in the data is: ", max_temp)
int(np.interp(max_temp, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,22]))

## Cycle through all the values in the data set under Humidity
for sensorvalue in sensor_data["temperature"]:
    #Interpolate the current value
    pin = int(np.interp(sensorvalue, [sensor_data["temperature"].min(),sensor_data["temperature"].max()], [18,21]))
    #Turn on the number of pins up to the interpolated value
    #print(pin)
    for pins in range(18, pin+1):
        GPIO.output(pins,GPIO.HIGH)
#        print(pin)
    time.sleep(.75)
    #Turn all the pins off before checking the next value
    for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)
    time.sleep(.75)
# Turn all pins off
for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)

GPIO.output(sun_2_pin,GPIO.LOW) ## Sets GPIO pin 21 output voltage low/off

print("End of program")
