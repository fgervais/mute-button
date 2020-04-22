import board
import digitalio
import time


button = digitalio.DigitalInOut(board.G0)
button.direction = digitalio.Direction.INPUT

while True:
    print(button.value)
    time.sleep(1)
