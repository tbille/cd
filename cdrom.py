#!/usr/bin/env python3

import os, time
import signal
import sys
from multiprocessing import Process
import requests
import pyttsx3



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
    engine = pyttsx3.init()

    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 70)

    try:
        quote = requests.get(
            "https://api.kanye.rest/?format=text"
        ).content.decode("utf-8")
    except Exception:
        quote = "The cow is in the house"

    engine.say(quote)
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
