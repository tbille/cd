import os, time
import signal
import sys

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

os.system('clear')

def animate(delay = 1, repeat = 10):
    frames = []
    for i in range(23):
        with open(f"frame{i+1}", "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for repeat in range(repeat):
        toto = 1
        for frame in frames:
            print(toto)
            toto=toto+1
            print("".join(frame))
            time.sleep(delay)
            os.system('clear')

animate(delay=0.4)
