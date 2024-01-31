from adafruit_circuitplayground.bluefruit import cpb
import time

cpb.pixels.brightness = 0.1

cpb.pixels.fill((0, 0, 0))

while True:
    cpb.pixels.fill((255, 0, 0)) 
    time.sleep(1)
    cpb.pixels.fill((0, 0, 0)) 
    time.sleep(1)
    cpb.pixels.fill((0, 255, 0)) 
    time.sleep(1)
    cpb.pixels.fill((0, 0, 0)) 
    time.sleep(1)
    cpb.pixels.fill((0, 0, 255))  
    time.sleep(1)
    cpb.pixels.fill((0, 0, 0)) 
    time.sleep(1)
