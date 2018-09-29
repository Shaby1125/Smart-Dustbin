import RPi.GPIO as GPIO

import time
GPIO.setwarnings(False)
trig = 17
echo = 24
echo1 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(9,GPIO.OUT)
pwm = GPIO.PWM(9,50)
pwm.start(1)
GPIO.output(trig,False)
#GPIO.output(trig1,False)
time.sleep(2)

#start_time1 = 0
#end_time1 = 0


def dist(tri, ech):
    start_time = 0
    end_time = 0
    
    GPIO.output(tri,True)
    time.sleep(0.00001)
    GPIO.output(tri,False)
    
    while(GPIO.input(ech)==0):
        start_time = time.time()
    while(GPIO.input(ech)==1):
        end_time = time.time()

    depth_duration = end_time - start_time
    dist = depth_duration * 17150
    #print("depth",dist)
    time.sleep(2)
    return dist

    
    
    
    
man = dist(trig,echo1)
time.sleep(2)
    
print(man)
    
depth = dist(trig,echo)
time.sleep(2)

print(depth)

        
        
if((depth > 10) and (man < 30)):
    angle = 90        # blank
            
elif((depth <= 10) and (man < 30)):
    angle = 0 # full
        
    
else:
    angle = 0
            
DC = (1/20*(angle)) + 1
pwm.ChangeDutyCycle(DC)


