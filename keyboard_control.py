from arm_controller import ArmController

arm = ArmController()
arm.home()

print("""
Keyboard control:
a / d  -> base left / right
w / s  -> shoulder up / down
i / k  -> elbow up / down
j / l  -> wrist up / down
u / o  -> rotate left / right
n / m  -> gripper open / close
h      -> home
q      -> quit
""")

while True:
    cmd = input("Command: ").strip().lower()

    if cmd == "a":
        arm.base_left()
    elif cmd == "d":
        arm.base_right()
    elif cmd == "w":
        arm.shoulder_up()
    elif cmd == "s":
        arm.shoulder_down()
    elif cmd == "i":
        arm.elbow_up()
    elif cmd == "k":
        arm.elbow_down()
    elif cmd == "j":
        arm.wrist_up()
    elif cmd == "l":
        arm.wrist_down()
    elif cmd == "u":
        arm.rotate_left()
    elif cmd == "o":
        arm.rotate_right()
    elif cmd == "n":
        arm.grip_open()
    elif cmd == "m":
        arm.grip_close()
    elif cmd == "h":
        arm.home()
    elif cmd == "q":
        print("Bye")
        break
    else:
        print("Unknown command")
