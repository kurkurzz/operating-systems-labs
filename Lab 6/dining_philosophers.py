'''
Write a program to simulate the Dining Philosophers Problem.
'''
import threading
import random
import time

class Philosopher(threading.Thread):
    running = True 

    def __init__(self, index, forkLeft, forkRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkLeft = forkLeft
        self.forkRight = forkRight
    
    def run(self):
        while self.running:
            time.sleep(1)
            print(f'Philosopher {int(self.index + 1)} is hungry')
            self.try_eat()

    def try_eat(self):
        fork1, fork2 = self.forkLeft, self.forkRight
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print("Philosopher %s swaps forks " % int(self.index + 1))
            fork1, fork2 = fork2, fork1
        else:
            return
        # Philosopher is eating
        print(f"Philosopher {int(self.index + 1)} starts eating")
        time.sleep(1)
        print(f"Philosopher {int(self.index + 1)} finishes eating and leaves to think")
       
        # Release both fork
        fork2.release()
        fork1.release()

def main():
    forks = [threading.Semaphore() for i in range(5)]
    philosophers = [Philosopher(i, forks[i%5], forks[(i+1)%5]) for i in range(5)]

    Philosopher.running = True
    for philosopher in philosophers:
        philosopher.start()
    time.sleep(10)
    Philosopher.running = False
    print("Now we're finishing")

main()