from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2
from remap import remap_U, remap_R, remap_F, remap_D, remap_L, remap_B

motor_grab   = LargeMotor(OUTPUT_A)
motor_rotate = LargeMotor(OUTPUT_B)
motor_lift   = MediumMotor(OUTPUT_C)
sensor       = ColorSensor(INPUT_2)

# scan positions (x for rotate, y for lift)
scan_positions = [
    (0, -715),
    (135, 170),
    (135, -70),
    (135, 70),
    (135, -70),
    (135, 70),
    (135, -70),
    (135, 70),
    (135, -70),
]

initial_positions = {}
def save_initial_positions():
    initial_positions['lift']   = motor_lift.position
    initial_positions['rotate'] = motor_rotate.position

def return_lift_to_initial_position():
    target = initial_positions['lift']
    if abs(motor_lift.position - target)>10:
        motor_lift.on_to_position(SpeedPercent(30), target)
        sleep(0.3)

def rotate_cube(direction='cw'):
    deg = 270 if direction=='cw' else -270
    motor_rotate.on_for_degrees(SpeedPercent(30), deg); sleep(0.3)

def grab_and_release():
    return_lift_to_initial_position()
    motor_grab.on_for_degrees(SpeedPercent(13), 225); sleep(0.3)
    motor_grab.on_for_degrees(SpeedPercent(13), -225); sleep(0.2)

def scan_face():
    colors = []
    for x,y in scan_positions:
        motor_lift.on_for_degrees(SpeedPercent(40), y)
        motor_rotate.on_for_degrees(SpeedPercent(45), x)
        sleep(0.3)
        colors.append(sensor.color)
        sleep(0.2)
    return_lift_to_initial_position()
    return colors

def scan_all_faces():
    save_initial_positions()
    labels_funcs = [
        remap_U, remap_R, remap_F,
        remap_D, remap_L, remap_B,
    ]
    directions = ['cw','ccw','cw','ccw','cw','ccw']
    all_faces = []
    for func, dirn in zip(labels_funcs, directions):
        raw = scan_face()
        all_faces.append(func(raw))
        rotate_cube(dirn)
        grab_and_release()
    return all_faces
