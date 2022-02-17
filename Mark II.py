import time
from time import sleep
import RPi.GPIO as GPIO

# Middle Motor Driver
# Right Motors
INM1 = 17
INM2 = 27
ENMA = 12
# Left Motors
INM3 = 14
INM4 = 15
ENMB = 13

# Front Motor Driver
# Right Motors
INF1 = 16
INF2 = 20
ENFA = 21
# Left Motors
INF3 = 5
INF4 = 6
ENFB = 26

# Back Motor Driver
# Right Motors
INB1 = 2
INB2 = 3
ENBA = 4
# Left Motors
INB3 = 10
INB4 = 9
ENBB = 11

# Ultrasonic Sensor
TRIG = 24
ECHO = 23
led = 19

GPIO.setwarnings(False)


def setup():
    GPIO.setmode(GPIO.BCM)  # GPIO Numbering
    GPIO.setup(INM1, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INM2, GPIO.OUT)
    GPIO.setup(ENMA, GPIO.OUT)
    GPIO.setup(INM3, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INM4, GPIO.OUT)
    GPIO.setup(ENMB, GPIO.OUT)

    GPIO.setup(INF1, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INF2, GPIO.OUT)
    GPIO.setup(ENFA, GPIO.OUT)
    GPIO.setup(INF3, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INF4, GPIO.OUT)
    GPIO.setup(ENFB, GPIO.OUT)

    GPIO.setup(INB1, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INB2, GPIO.OUT)
    GPIO.setup(ENBA, GPIO.OUT)
    GPIO.setup(INB3, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(INB4, GPIO.OUT)
    GPIO.setup(ENBB, GPIO.OUT)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)


def forward():
    print("Going Forwards")
    
    GPIO.output(ENMA, GPIO.HIGH)
    GPIO.output(ENMB, GPIO.HIGH)

    GPIO.output(ENFA, GPIO.HIGH)
    GPIO.output(ENFB, GPIO.HIGH)

    GPIO.output(ENBA, GPIO.HIGH)
    GPIO.output(ENBB, GPIO.HIGH)
    
    GPIO.output(INM1, GPIO.HIGH)
    GPIO.output(INM2, GPIO.LOW)

    GPIO.output(INF1, GPIO.HIGH)
    GPIO.output(INF2, GPIO.LOW)

    GPIO.output(INB1, GPIO.HIGH)
    GPIO.output(INB2, GPIO.LOW)

    GPIO.output(INM3, GPIO.HIGH)
    GPIO.output(INM4, GPIO.LOW)

    GPIO.output(INF3, GPIO.HIGH)
    GPIO.output(INF4, GPIO.LOW)

    GPIO.output(INB3, GPIO.HIGH)
    GPIO.output(INB4, GPIO.LOW)


def backward():
    print("Going Backwards")
    GPIO.output(INM1, GPIO.LOW)
    GPIO.output(INM2, GPIO.HIGH)

    GPIO.output(INF1, GPIO.LOW)
    GPIO.output(INF2, GPIO.HIGH)

    GPIO.output(INB1, GPIO.LOW)
    GPIO.output(INB2, GPIO.HIGH)

    GPIO.output(INM3, GPIO.LOW)
    GPIO.output(INM4, GPIO.HIGH)

    GPIO.output(INF3, GPIO.LOW)
    GPIO.output(INF4, GPIO.HIGH)

    GPIO.output(INB3, GPIO.LOW)
    GPIO.output(INB4, GPIO.HIGH)

    GPIO.output(ENMA, GPIO.HIGH)
    GPIO.output(ENMB, GPIO.HIGH)

    GPIO.output(ENFA, GPIO.HIGH)
    GPIO.output(ENFB, GPIO.HIGH)

    GPIO.output(ENBA, GPIO.HIGH)
    GPIO.output(ENBB, GPIO.HIGH)


def right():
    print("Going Right")
    GPIO.output(INM1, GPIO.LOW)
    GPIO.output(INM2, GPIO.LOW)
    GPIO.output(INF1, GPIO.LOW)
    GPIO.output(INF2, GPIO.LOW)
    GPIO.output(INB1, GPIO.LOW)
    GPIO.output(INB2, GPIO.LOW)

    GPIO.output(INM3, GPIO.HIGH)
    GPIO.output(INM4, GPIO.LOW)
    GPIO.output(INF3, GPIO.HIGH)
    GPIO.output(INF4, GPIO.LOW)
    GPIO.output(INB3, GPIO.HIGH)
    GPIO.output(INB4, GPIO.LOW)

    GPIO.output(ENMB, GPIO.HIGH)
    GPIO.output(ENFB, GPIO.HIGH)
    GPIO.output(ENBB, GPIO.HIGH)

    GPIO.output(ENMA, GPIO.LOW)
    GPIO.output(ENFA, GPIO.LOW)
    GPIO.output(ENBA, GPIO.LOW)


def left():
    print("Going Left")
    GPIO.output(INM1, GPIO.HIGH)
    GPIO.output(INM2, GPIO.LOW)
    GPIO.output(INF1, GPIO.HIGH)
    GPIO.output(INF2, GPIO.LOW)
    GPIO.output(INB1, GPIO.HIGH)
    GPIO.output(INB2, GPIO.LOW)

    GPIO.output(INM3, GPIO.LOW)
    GPIO.output(INM4, GPIO.LOW)
    GPIO.output(INF3, GPIO.LOW)
    GPIO.output(INF4, GPIO.LOW)
    GPIO.output(INB3, GPIO.LOW)
    GPIO.output(INB4, GPIO.LOW)

    GPIO.output(ENMB, GPIO.LOW)
    GPIO.output(ENFB, GPIO.LOW)
    GPIO.output(ENBB, GPIO.LOW)

    GPIO.output(ENMA, GPIO.HIGH)
    GPIO.output(ENFA, GPIO.HIGH)
    GPIO.output(ENBA, GPIO.HIGH)


def stop():
    print("Stop")
    GPIO.output(ENMB, GPIO.LOW)
    GPIO.output(ENFB, GPIO.LOW)
    GPIO.output(ENBB, GPIO.LOW)

    GPIO.output(ENMA, GPIO.LOW)
    GPIO.output(ENFA, GPIO.LOW)
    GPIO.output(ENBA, GPIO.LOW)

def delay():
    time.sleep(5)

def destroy():
    GPIO.cleanup()

def automaticmode():
    print("Initialising Automatic Mode Please Wait.....\n")
    try:
        count = 0
        i = 0
        while True:
            print("Automatic Mode Started\n")
            stop()
            GPIO.output(led, True)
            avgDistance = 0.0
            for i in range(5):
                GPIO.output(TRIG, False)  # Initialising trigger to LOW
                time.sleep(0.1)  # Delay
                
                GPIO.output(TRIG, True)  # Initialising trigger to HIGH
                time.sleep(0.00001)  # Delay of 0.00001 seconds
                GPIO.output(TRIG, False)  # Initialising trigger to LOW

                while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
                    GPIO.output(led, False)
                pulse_start = time.time()

                while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
                    GPIO.output(led, False)
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start  # time to get backward the pulse to sensor

                distance = pulse_duration * 17150  # Multiply pulse duration by 17150 (34300/2) to get distance
                distance = round(distance, 2)  # Round to two decimal points
                avgDistance = avgDistance + distance

            avgDistance = avgDistance / 5
            print(avgDistance)
            flag = 0
            if avgDistance > 15:# Check whether the distance is within 15 cm range
                time.sleep(1)
                forward()
                time.sleep(1)   
            else:
                count = count + 1
                stop()
                time.sleep(1)
                backward()
                time.sleep(1.5)
                stop()
                time.sleep(1)
                if (count % 3 == 1) & (flag == 0):
                    right()
                    time.sleep(1.5)
                    flag = 1
                else:
                    left()
                    flag = 0
                time.sleep(1.5)
                stop()
                time.sleep(1)
    except:
        print("Something Went Wrong/n")

if __name__ == '__main__':  # Program start from here
    print("Welcome to Android Controlled Surveillance Robot\n")
    setup()
    try:
        automaticmode()
    except KeyboardInterrupt:
        print("Surveillance Stopped\n")
        destroy()