from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent

motor_grab   = LargeMotor(OUTPUT_A)
motor_rotate = LargeMotor(OUTPUT_B)
motor_lift   = MediumMotor(OUTPUT_C)

def grab_soft():
    motor_grab.on_for_degrees(SpeedPercent(13), 100)
    sleep(0.3)

def release_soft():
    motor_grab.on_for_degrees(SpeedPercent(13), -100)
    sleep(0.3)

def grab_and_release():
    motor_grab.on_for_degrees(SpeedPercent(13), 225)
    sleep(0.4)
    motor_grab.on_for_degrees(SpeedPercent(13), -225)
    sleep(0.4)

def rotate_cw():
    motor_rotate.on_for_degrees(SpeedPercent(30), 270)
    sleep(0.3)

def rotate_ccw():
    motor_rotate.on_for_degrees(SpeedPercent(30), -270)
    sleep(0.3)

# define U, D, F, B, R, L moves using the above primitives:
def move_U():
    grab_and_release(); grab_and_release()
    grab_soft(); rotate_ccw(); release_soft()
    grab_and_release(); grab_and_release()

def move_U_prime():
    grab_and_release(); grab_and_release()
    grab_soft(); rotate_cw(); release_soft()
    grab_and_release(); grab_and_release()

def move_U2():
    move_U(); move_U()

def move_D():
    grab_soft(); rotate_ccw(); release_soft()

def move_D_prime():
    grab_soft(); rotate_cw(); release_soft()

def move_D2():
    move_D(); move_D()

def move_F():
    rotate_ccw(); rotate_ccw()
    grab_and_release()
    grab_soft(); rotate_ccw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release()

def move_F_prime():
    rotate_ccw(); rotate_ccw()
    grab_and_release()
    grab_soft(); rotate_cw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release()

def move_F2():
    move_F(); move_F()

def move_B():
    grab_and_release()
    grab_soft(); rotate_ccw(); release_soft()
    grab_and_release(); grab_and_release(); grab_and_release()

def move_B_prime():
    grab_and_release()
    grab_soft(); rotate_cw(); release_soft()
    grab_and_release(); grab_and_release(); grab_and_release()

def move_B2():
    move_B(); move_B()

def move_R():
    rotate_ccw()
    grab_and_release()
    grab_soft(); rotate_ccw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release(); rotate_ccw()

def move_R_prime():
    rotate_ccw()
    grab_and_release()
    grab_soft(); rotate_cw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release(); rotate_ccw()

def move_R2():
    move_R(); move_R()

def move_L():
    rotate_cw()
    grab_and_release()
    grab_soft(); rotate_ccw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release(); rotate_cw()

def move_L_prime():
    rotate_cw()
    grab_and_release()
    grab_soft(); rotate_cw(); release_soft()
    rotate_ccw(); rotate_ccw()
    grab_and_release(); rotate_cw()

def move_L2():
    move_L(); move_L()

def apply_move_logic(move, facelets_lit=None):
    {
        'U': move_U, "U'": move_U_prime, 'U2': move_U2,
        'D': move_D, "D'": move_D_prime, 'D2': move_D2,
        'F': move_F, "F'": move_F_prime, 'F2': move_F2,
        'B': move_B, "B'": move_B_prime, 'B2': move_B2,
        'R': move_R, "R'": move_R_prime, 'R2': move_R2,
        'L': move_L, "L'": move_L_prime, 'L2': move_L2,
    }[move]()
