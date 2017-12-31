#!/usr/bin/python3

import ev3dev.ev3 as ev3
import ev3dev.core as ev3core

def main():
    lmotor = ev3core.LargeMotor(ev3.OUTPUT_B)
    rmotor = ev3core.LargeMotor(ev3.OUTPUT_C)  
    lmotor.stop(stop_action='brake')
    rmotor.stop(stop_action='brake')

if __name__ == "__main__":
  main()
