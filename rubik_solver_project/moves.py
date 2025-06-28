from time import sleep
from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent

motor_grab = LargeMotor(OUTPUT_A)
motor_rotate = LargeMotor(OUTPUT_B)
motor_lift = MediumMotor(OUTPUT_C)

# Definim miscarile fizice pentru fiecare mutare Rubik

def grab_soft():
    motor_grab.on_for_degrees(SpeedPercent(13), 100)
    sleep(0.4)

def release_soft():
    motor_grab.on_for_degrees(SpeedPercent(13), -100)
    sleep(0.4)

def grab_and_release():
    motor_grab.on_for_degrees(SpeedPercent(13), 225)
    sleep(0.5)
    motor_grab.on_for_degrees(SpeedPercent(13),-225)
    sleep(0.5)

def rotate_cw():
    motor_rotate.on_for_degrees(SpeedPercent(30), 270)
    sleep(0.3)

def rotate_ccw():
    motor_rotate.on_for_degrees(SpeedPercent(30), -270)
    sleep(0.3)

def move_U():
    grab_and_release()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    release_soft()
    grab_and_release()
    grab_and_release()

def move_U2():
    grab_and_release()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    rotate_ccw()

def move_U_prim():
    grab_and_release()
    grab_and_release()
    grab_soft()
    rotate_cw()
    release_soft()
    grab_and_release()
    grab_and_release()

def move_D():
    grab_soft()
    rotate_ccw()
    release_soft()

def move_D2():
    grab_soft()
    rotate_ccw()
    rotate_ccw()
    release_soft()

def move_D_prim():
    grab_soft()
    rotate_cw()
    release_soft()

def move_F():
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()

def move_F2():
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    rotate_ccw()

def move_F_prim():
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_cw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()

def move_B():
    grab_and_release()
    grab_soft()
    rotate_ccw()
    release_soft()
    grab_and_release()
    grab_and_release()
    grab_and_release()

def move_B2():
    grab_and_release()
    grab_soft()
    rotate_ccw()
    rotate_ccw()
    release_soft()
    grab_and_release()
    grab_and_release()
    grab_and_release()

def move_B_prim():
    grab_and_release()
    grab_soft()
    rotate_cw()
    release_soft()
    grab_and_release()
    grab_and_release()
    grab_and_release()

def move_R():
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_ccw()

def move_R2():
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    rotate_ccw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_ccw()

def move_R_prim():
    rotate_ccw()
    grab_and_release()
    grab_soft()
    rotate_cw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_ccw()


def move_L():
    rotate_cw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_cw()

def move_L2():
    rotate_cw()
    grab_and_release()
    grab_soft()
    rotate_ccw()
    rotate_ccw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_cw()

def move_L_prim():
    rotate_cw()
    grab_and_release()
    grab_soft()
    rotate_cw()
    release_soft()
    rotate_ccw()
    rotate_ccw()
    grab_and_release()
    rotate_cw()

def apply_move_logic(move, facelets_lit=None):
    if move == 'U': move_U()
    elif move == "U'": move_U_prim()
    elif move == 'U2': move_U2()
    elif move == 'D': move_D()
    elif move == "D'": move_D_prim()
    elif move == 'D2': move_D2()
    elif move == 'F': move_F()
    elif move == "F'": move_F_prim()
    elif move == 'F2': move_F2()
    elif move == 'B': move_B()
    elif move == "B'": move_B_prim()
    elif move == 'B2': move_B2()
    elif move == 'R': move_R()
    elif move == "R'": move_R_prim()
    elif move == 'R2': move_R2()
    elif move == 'L': move_L()
    elif move == "L'": move_L_prim()
    elif move == 'L2': move_L2()