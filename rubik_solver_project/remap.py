from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent

motor_grab = LargeMotor(OUTPUT_A)
motor_rotate = LargeMotor(OUTPUT_B)
motor_lift = MediumMotor(OUTPUT_C)

# Definim miscarile fizice pentru fiecare mutare Rubik

def grab_soft():
    motor_grab.on_for_degrees(SpeedPercent(20), 100)
    sleep(0.3)

def release_soft():
    motor_grab.on_for_degrees(SpeedPercent(20), -100)
    sleep(0.3)

def grab_full():
    motor_grab.on_for_degrees(SpeedPercent(20), 240)
    sleep(0.3)

def release_full():
    motor_grab.on_for_degrees(SpeedPercent(20), -240)
    sleep(0.3)

def rotate_base_to_face(turns=0):
    motor_rotate.on_for_degrees(SpeedPercent(30), turns * 270)
    sleep(0.3)

def turn_face():
    grab_soft()
    motor_rotate.on_for_degrees(SpeedPercent(30), 270)
    sleep(0.3)
    release_soft()

def turn_face_ccw():
    grab_soft()
    motor_rotate.on_for_degrees(SpeedPercent(30), -270)
    sleep(0.3)
    release_soft()

def remap_U(face):
    return [face[i] for i in [5,4,3,6,0,2,7,8,1]]

def remap_R(face):
    return [face[i] for i in [5,4,3,6,0,2,7,8,1]]

def remap_F(face):
    return [face[i] for i in [7,6,5,8,0,4,1,2,3]]

def remap_D(face):
    return [face[i] for i in [5,4,3,6,0,2,7,8,1]]

def remap_L(face):
    return [face[i] for i in [1,8,7,2,0,6,3,4,5]]

def remap_B(face):
    return [face[i] for i in [7,6,5,8,0,4,1,2,3]]

def apply_move_logic(move):
    print("[MOVES] Aplicam mutarea: {}".format(move))
    face_turn_map = {
        'U': 0,
        'R': 1,
        'F': 2,
        'D': 3,
        'L': 4,
        'B': 5,
    }

    move = move.strip()
    if not move:
        return

    base_move = move[0]
    prime = len(move) > 1 and move[1] == "'"

    if base_move in face_turn_map:
        turns = face_turn_map[base_move]
        rotate_base_to_face(turns)
        if prime:
            turn_face_ccw()
        else:
            turn_face()

