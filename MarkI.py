import time
from time import sleep
import RPi.GPIO as GPIO

#Right Motors
IN1 = 17
IN2 = 27
ENA = 22
#Left Motors
IN3 = 14
IN4 = 15
ENB = 18
#Ultrasonic Sensor
TRIG = 24
ECHO = 23


def setup():
    GPIO.setmode(GPIO.BCM)  # GPIO Numbering
            #MOTORS
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
        #ULTRASONIC SENSOR
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

def forward():
    print("Going Forwards")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def backward():
    print("Going backwardwards")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

def right():
    print("Going Right")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENB, GPIO.HIGH)

def left():
    print("Going Left")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)

def stop():
    print("Stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)

def delay():
    time.sleep(5)

def destroy():
    GPIO.cleanup()

def automaticmode():
    print("Initialising Automatic Mode Please Wait...../n")
    try:
        while True:
            print("Automatic Mode Started/n")
            stop()
            count = 0
            i = 0
            avgDistance = 0.0
            for i in range(5):
                GPIO.output(TRIG, False)  # Initialising trigger to LOW
                time.sleep(0.1)  # Delay

                GPIO.output(TRIG, True)  # Initialising trigger to HIGH
                time.sleep(0.00001)  # Delay of 0.00001 seconds
                GPIO.output(TRIG, False)  # Initialising trigger to LOW

                #while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
                    #GPIO.output(led, False)
                    
                pulse_start = time.time()

                #while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
                    #GPIO.output(led, False)
                    
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start  # time to get backward the pulse to sensor

                distance = pulse_duration * 17150  # Multiply pulse duration by 17150 (34300/2) to get distance
                distance = round(distance, 2)  # Round to two decimal points
                avgDistance = avgDistance + distance

            avgDistance = avgDistance / 5
            print(avgDistance)
            flag = 0
            if avgDistance < 15:  # Check whether the distance is within 15 cm range
                count = count + 1
                stop()
                time.sleep(1)
                backward()
                time.sleep(1.5)
                if (count % 3 == 1) & (flag == 0):
                    right()
                    flag = 1
                else:
                    left()
                    flag = 0
                time.sleep(1.5)
                stop()
                time.sleep(1)
            else:
                forward()
                flag = 0
    except:
        print("Something Went Wrong/n")

if __name__ == '__main__':  # Program start from here
    print("Welcome to Android Controlled Surveillance Robot/n")
    setup()
    try:
        automaticmode()
    except KeyboardInterrupt:
        destroy()