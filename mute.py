import board
import digitalio
import time
import subprocess
import logging
import argparse


button = digitalio.DigitalInOut(board.G0)
button.direction = digitalio.Direction.INPUT

muted = False


def mute():
    global muted

    logging.info("muting")
    subprocess.run(["amixer", "-c", "1", "set", "Mic", "nocap"],
                   stdout=subprocess.DEVNULL)
    muted = True

def unmute():
    global muted

    logging.info("unmuting")
    subprocess.run(["amixer", "-c", "1", "set", "Mic", "cap"],
                   stdout=subprocess.DEVNULL)
    muted = False


parser = argparse.ArgumentParser(description='Mute/unmute microphone.')
parser.add_argument("-d", "--debug", action="store_true",
                    help="enable debug")
args = parser.parse_args()

logging.basicConfig(
    format='[%(asctime)s] [%(name)-12s] %(levelname)-8s %(message)s',
    level=logging.DEBUG if args.debug else logging.WARNING,
    datefmt='%Y-%m-%d %H:%M:%S')


mute()

try:
    while True:
        # logging.debug(button.value)
        if button.value == False and muted:
            unmute()

        if button.value == True and not muted:
            mute()
            muted = True

        time.sleep(0.01)
except KeyboardInterrupt:
    pass

unmute()
