from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2

motor_grab = LargeMotor(OUTPUT_A)
motor_rotate = LargeMotor(OUTPUT_B)
motor_lift = MediumMotor(OUTPUT_C)
sensor = ColorSensor(INPUT_2)

# Pozitii scanare pentru o fata
init_centru = -715
O_L_FIRST = 170
O_L_NEXT = 70
O_R = 135

scan_positions = [
    (0, init_centru),
    (O_R, O_L_FIRST),
    (O_R, -O_L_NEXT),
    (O_R, O_L_NEXT),
    (O_R, -O_L_NEXT),
    (O_R, O_L_NEXT),
    (O_R, -O_L_NEXT),
    (O_R, O_L_NEXT),
    (O_R, -O_L_NEXT),
]

initial_positions = {}

def save_initial_positions():
    initial_positions['lift'] = motor_lift.position
    initial_positions['rotate'] = motor_rotate.position

def return_lift_to_initial_position(threshold=10):
    current = motor_lift.position
    target = initial_positions.get('lift', 0)
    if abs(current - target) > threshold:
        motor_lift.on_to_position(SpeedPercent(30), target)
        sleep(0.3)

def rotate_cube(direction='cw'):
    deg = 270 if direction == 'cw' else -270
    motor_rotate.on_for_degrees(SpeedPercent(30), deg)
    sleep(0.3)

def grab_and_release():
    return_lift_to_initial_position()
    motor_grab.on_for_degrees(SpeedPercent(13), 225)
    sleep(0.3)
    motor_grab.on_for_degrees(SpeedPercent(13), -225)
    sleep(0.2)

def scan_face():
    colors = []
    for x, y in scan_positions:
        motor_lift.on_for_degrees(SpeedPercent(40), y)
        motor_rotate.on_for_degrees(SpeedPercent(45), x)
        sleep(0.3)
        colors.append(sensor.color)
        sleep(0.3)
    return_lift_to_initial_position()
    return colors

from remap import (
    remap_U,
    remap_R,
    remap_F,
    remap_D,
    remap_L,
    remap_B,
)

def scan_all_faces():
    save_initial_positions()
    face_labels = ['U', 'R', 'F', 'D', 'L', 'B']
    directions = ['cw', 'ccw', 'cw', 'ccw', 'cw', 'ccw']
    remap_functions = {
        'U': remap_U,
        'R': remap_R,
        'F': remap_F,
        'D': remap_D,
        'L': remap_L,
        'B': remap_B,
    }

    all_faces = []

    for label, direction in zip(face_labels, directions):
        print("Scanam fata {}".format(label))
        raw_face = scan_face()
        mapped = remap_functions[label](raw_face)
        if mapped is None or len(mapped) != 9:
            print("[EROARE] remap pentru fata {} a returnat invalid: {}".format(label, mapped))
            return None
        print("[DEBUG] Fata{} returnata de remap: {}".format(label, mapped))
        all_faces.append(mapped)
        rotate_cube(direction)
        grab_and_release()

    return all_faces