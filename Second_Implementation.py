pin18 = 18
pin19 = 19
pin20 = 20
pin21 = 21

max_temp = sensor_data["temperature"].max()
min_temp = sensor_data["temperature"].min()

mean1_temp = sensor_data["temperature"].mean()-2
mean2_temp = sensor_data["temperature"].mean()-6

print(max_temp)
print(min_temp)
print(mean1_temp)
print(mean2_temp)

for sensorvalue in sensor_data["temperature"]:
    if sensorvalue == max_temp:
        GPIO.output(pin18,GPIO.HIGH)
        GPIO.output(pin19,GPIO.HIGH)
        GPIO.output(pin20,GPIO.HIGH)
        GPIO.output(pin21,GPIO.HIGH)
    if (sensorvalue < max_temp) & (sensorvalue >= mean2_temp):
        GPIO.output(pin18,GPIO.HIGH)
        GPIO.output(pin19,GPIO.HIGH)
        GPIO.output(pin20,GPIO.HIGH)
    if (sensorvalue > min_temp) & (sensorvalue < mean1_temp):
        GPIO.output(pin18,GPIO.HIGH)
        GPIO.output(pin19,GPIO.HIGH)
    if sensorvalue == min_temp:
        GPIO.output(pin18,GPIO.HIGH)
    
    time.sleep(2)
    #Turn all the pins off before checking the next value
    for pins in range(18,22):
        GPIO.output(pins,GPIO.LOW)
    time.sleep(1)
    
    
# Turn all pins off
for pin_off in range(18,22):
        GPIO.output(pin_off,GPIO.LOW)
