#!/usr/bin/env python3
import random, math

def blackbox(i):
    return math.sin(i*2*math.pi/200) + 0.3*math.cos(i*2*math.pi/10)

def main():
    for i in range(10000):
        print(blackbox(i))

if __name__ == "__main__":
    main()
