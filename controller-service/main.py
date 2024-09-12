import random
import time
from controller import Controller

def main():
    random.seed(int(time.time()))  # Seed random number generator
    controller = Controller()

    keep_running = True
    while keep_running:
        controller.run_day()
        keep_running = int(input("Run another day? (1: yes, 0: no): "))
        print("-----------------------------------")

if __name__ == "__main__":
    main()
