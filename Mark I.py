import time
#import RPi.GPIO as GPIO

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
    GPIO.setup(IN1, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
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
    print("Going Backwards")
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
    except KeyboardInterrupt:
        destroy()