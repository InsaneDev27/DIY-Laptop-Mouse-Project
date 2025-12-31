"""
MIT License

Copyright (c) 2025 InsaneDev27

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import usb_hid
from adafruit_hid.mouse import Mouse
import time
import digitalio
import analogio
import rotaryio
import board

mouse = Mouse(usb_hid.devices)

lClick = digitalio.DigitalInOut(board.GP2)
lClick.switch_to_input(pull=digitalio.Pull.UP)
rClick = digitalio.DigitalInOut(board.GP3)
rClick.switch_to_input(pull=digitalio.Pull.UP)
cClick = digitalio.DigitalInOut(board.GP28)
cClick.switch_to_input(pull=digitalio.Pull.UP)

xRaw = analogio.AnalogIn(board.A1)
yRaw = analogio.AnalogIn(board.A0)
encoder = rotaryio.IncrementalEncoder(board.GP0, board.GP1, 1)

#variables for scroll and fast scroll functions
lastPosition = 0 # the last registered postion of the rotary encoder
lastTime = time.monotonic() # last time scroll wheel was moved
lastTimeFast = time.monotonic() # last time we scrolled speedily
lastTimeSet = time.monotonic() # last time the fast scrolling was initialized
lastScrollDirection = 1 # 1 for scrolling up, -1 for down
numOfIncrementsRecently = 0 # how many scroll wheel movements were registered recently ( within .03 seconds of each other )
encoderFactorBaseValue = 1
maxTimeBetweenIncrements = .01
maxTimeBetweenFastScroll = .6

tempDPI = False # temporary sensitivity for precision movements
dpi = 0.5 # sensitivity, not actual dpi measurement
encoderFactor = 2.0

lClickOn = False
rClickOn = False
cClickOn = False
dpiChangedThisPress = False

def get_voltage(raw):
    return (raw * 33) / 65536

def sameScrollDirection(deltaPosition):
    return ((lastScrollDirection == 1 and deltaPosition > 0) or (lastScrollDirection == -1 and deltaPosition < 0))

while True:
    deltaPosition = encoder.position - lastPosition;
    
    x=0
    y=0
    
    if (not tempDPI):
        x = int(int(get_voltage(xRaw.value) - 16.5) * dpi)
        y = int((int(get_voltage(yRaw.value) - 16.5) * dpi) * (-1)) #inverted out of neccessity
    else:
        x = int(int(get_voltage(xRaw.value) - 16.5) * .1)
        y = int((int(get_voltage(yRaw.value) - 16.5) * .1) * (-1))
        
    #     move(x, y,                wheel                )
    mouse.move(x, y, int((deltaPosition) * encoderFactor))

    #psuedo fast-scrolling (similar to how touchscreen scroll speed increases the more times in rapid succession the user scrolls)
    
    #making variables for the time elapsed since lastTime, lastTimeFast, and lastTimeSet were updated
    currTime = time.monotonic()
    timeSinceLast = currTime - lastTime
    timeSinceLastFast = currTime - lastTimeFast
    timeSinceLastSet = currTime - lastTimeSet
    
    # if any scroll wheel movement registered
    if (int(deltaPosition) != 0):
        # UNCOMMENT BELOW if you want data on scroll speed to adjust time settings for your preferences
        #print("num of increments: ", numOfIncrementsRecently, " lastTime: ", timeSinceLast, " lastTimeFast: ", timeSinceLastFast, " lastTimeSet: ", timeSinceLastSet, " encoderFactor: ",  encoderFactor)
        
        # if this change was close in time to the last, and the scroll direction has not changed
        if (timeSinceLast <= maxTimeBetweenIncrements and sameScrollDirection(deltaPosition)): # (doesn't register anything in between 1 and zero)
            numOfIncrementsRecently += 1
            # increase encoder factor to 1.5 to give a more horsepower at the start
            if (encoderFactor == encoderFactorBaseValue):
                # this declares the last time that fast scrolling started is now
                lastTimeSet = time.monotonic()
            # we just went fast, so set lastTimeFast to now
            lastTimeFast = time.monotonic()

            # after horsepower boost, if still eligible, feel free to keep increasing within the limit of 10x speed
            if((numOfIncrementsRecently > 1) and (timeSinceLastFast <= maxTimeBetweenFastScroll)):
                if (encoderFactor <= 10):
                    encoderFactor = encoderFactor + .5
                numOfIncrementsRecently = 0
            # we just went fast, so set lastTimeFast to now
            lastTimeFast = time.monotonic()
        # elif ineligible to go fast
        elif (((timeSinceLastFast > maxTimeBetweenFastScroll) and (timeSinceLastSet >= 1)) or not sameScrollDirection(deltaPosition)):
            numOfIncrementsRecently = 0
            encoderFactor = encoderFactorBaseValue
            
        #we recieved scroll wheel input, so we will update lastTime to match
        lastTime = currTime
        
        #updating lastScrollDirection to match new direction regardless if different or just ran out of time.
        if (deltaPosition < 0):
            lastScrollDirection = -1
        else:
            lastScrollDirection = 1
            
    lastPosition = int(encoder.position) #hopefully this will not reset the last position until it has been registered in mouse.move()
    
    # the .value properties of the buttons are inversely assigned (pushed is registered as false), so this code makes it easier to read
    lCV = not lClick.value
    rCV = not rClick.value
    cCV = not cClick.value
    
    # if all 3 buttons pressed, change dpi
    if lCV and rCV and cCV and not dpiChangedThisPress:
        if (dpi != 2.0):
            dpi += 0.5
        else:
            dpi = 0.5
        
        # do no other functions on this press
        dpiChangedThisPress = True
    
    # if left and right click pressed, engage temporary DPI
    elif (lCV and rCV and not dpiChangedThisPress):
        tempDPI = not tempDPI
        dpiChangedThisPress = True
                 
    elif (not dpiChangedThisPress):
        # if not being held, send left click input to computer:
        if lCV and not lClickOn:
            mouse.press(mouse.LEFT_BUTTON)
            lClickOn = True
              
        # if not being held, send right click input to computer:
        if rCV and not rClickOn:
            mouse.press(mouse.RIGHT_BUTTON)
            rClickOn = True      
        
        # if not being held, send center click input to computer:
        if cCV and not cClickOn:
            mouse.press(mouse.MIDDLE_BUTTON)
            cClickOn = True
    
        
    # release if not being pressed
    if not lCV and lClickOn:
        lClickOn = False
        dpiChangedThisPress = False
        mouse.release(mouse.LEFT_BUTTON)
    if not rCV and rClickOn:
        rClickOn = False
        dpiChangedThisPress = False
        mouse.release(mouse.RIGHT_BUTTON)
    if not cCV and cClickOn:
        cClickOn = False
        dpiChangedThisPress = False
        mouse.release(mouse.MIDDLE_BUTTON)
        
    #FAILSAFE
        #if you are stuck, press ctrl+c to stop program
        
    
    time.sleep(0.001)