import time
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
    

def forward():
    print("Going Forwards")
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

    GPIO.output(ENMA, GPIO.HIGH)
    GPIO.output(ENMB, GPIO.HIGH)

    GPIO.output(ENFA, GPIO.HIGH)
    GPIO.output(ENFB, GPIO.HIGH)

    GPIO.output(ENBA, GPIO.HIGH)
    GPIO.output(ENBB, GPIO.HIGH)


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


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        forward()
        delay()
        backward()
        delay()
        left()
        delay()
        right()
        delay()
        stop()
        GPIO.cleanup()
    except KeyboardInterrupt:
        destroy()