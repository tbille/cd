#!/usr/bin/env python3

import os, time
import signal
import sys
from multiprocessing import Process


os.system("clear")
BASE_DIR = os.getenv("SNAP", ".") + "/"

p1 = None
p2 = None


def animate():
    frames = []
    for i in range(23):
        with open(f"{BASE_DIR}frames/frame{i+1}", "r", encoding="utf8") as f:
            frames.append(f.readlines())

    for repeat in range(1000000):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.4)
            os.system("clear")


def sing():
    import pyttsx3

    engine = pyttsx3.init()

    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 50)

    with open(f"{BASE_DIR}frames/lyrics", "r") as ifile:
        for line in ifile:
            engine.say(line)
            engine.runAndWait()

    p1.terminate()


def signal_handler(sig, frame):
    p1.terminate()
    p2.terminate()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    p1 = Process(target=animate)
    p1.start()
    p2 = Process(target=sing)
    p2.start()
    p1.join()
    p2.join()
