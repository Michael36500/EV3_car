#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D
from time import sleep

levy_zadni = LargeMotor(OUTPUT_C)
pravy_zadni = LargeMotor(OUTPUT_B)

zataceci_motor = MediumMotor(OUTPUT_D)
zataceci_motor.reset()

def dopredu(power):
    global levy_zadni, pravy_zadni

    power *= -1

    levy_zadni.on(power)
    pravy_zadni.on(power)


def zatoc(kam):
    global zataceci_motor

    zataceci_motor.run_to_abs_pos(position_sp = kam, speed_sp = 300, stop_action = "hold")


# dopredu(100)
# sleep(3)
# dopredu(0)