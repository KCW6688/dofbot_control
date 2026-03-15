import threading
import time
from arm_controller import ArmController

arm = ArmController()

running = True
motion = {
    "base": 0,
    "shoulder": 0,
    "elbow": 0,
    "wrist": 0,
    "rotate": 0,
    "grip": 0
}

STEP = 3


def motion_loop():
    global running
    while running:
        if motion["base"] == -1:
            arm.base_left()
        elif motion["base"] == 1:
            arm.base_right()

        if motion["shoulder"] == -1:
            arm.shoulder_up()
        elif motion["shoulder"] == 1:
            arm.shoulder_down()

        if motion["elbow"] == -1:
            arm.elbow_up()
        elif motion["elbow"] == 1:
            arm.elbow_down()

        time.sleep(0.25)


threading.Thread(target=motion_loop, daemon=True).start()

arm.home()

print("""
Toggle Control Mode

a = base left toggle
d = base right toggle
w = shoulder up toggle
s = shoulder down toggle

h = home
x = STOP ALL
q = quit
""")

while True:
    cmd = input("cmd: ").strip().lower()

    if cmd == "a":
        motion["base"] = 0 if motion["base"] == -1 else -1

    elif cmd == "d":
        motion["base"] = 0 if motion["base"] == 1 else 1

    elif cmd == "w":
        motion["shoulder"] = 0 if motion["shoulder"] == -1 else -1

    elif cmd == "s":
        motion["shoulder"] = 0 if motion["shoulder"] == 1 else 1

    elif cmd == "x":
        for k in motion:
            motion[k] = 0
        print("STOP ALL")

    elif cmd == "h":
        for k in motion:
            motion[k] = 0
        arm.home()

    elif cmd == "q":
        running = False
        break
