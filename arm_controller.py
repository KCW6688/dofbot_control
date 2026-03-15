from Arm_Lib import Arm_Device
import time


class ArmController:
    def __init__(self):
        self.arm = Arm_Device()

        self.angles = {
            1: 90,   # base
            2: 90,   # shoulder
            3: 90,   # elbow
            4: 90,   # wrist
            5: 90,   # rotate
            6: 90    # gripper
        }

        self.min_angle = 0
        self.max_angle = 180
        self.step = 5
        self.move_time = 300

    def clamp(self, angle):
        return max(self.min_angle, min(self.max_angle, angle))

    def move_servo(self, sid, delta):
        self.angles[sid] = self.clamp(self.angles[sid] + delta)
        self.arm.Arm_serial_servo_write(sid, self.angles[sid], self.move_time)
        print(f"Servo {sid} -> {self.angles[sid]}")

    def set_servo(self, sid, angle):
        self.angles[sid] = self.clamp(angle)
        self.arm.Arm_serial_servo_write(sid, self.angles[sid], self.move_time)
        print(f"Servo {sid} -> {self.angles[sid]}")

    def home(self):
        for sid in self.angles:
            self.angles[sid] = 90
        self.arm.Arm_serial_servo_write6(
            self.angles[1],
            self.angles[2],
            self.angles[3],
            self.angles[4],
            self.angles[5],
            self.angles[6],
            1000
        )
        print("Home position")


    def base_left(self):
        self.move_servo(1, -self.step)

    def base_right(self):
        self.move_servo(1, self.step)

    def shoulder_up(self):
        self.move_servo(2, -self.step)

    def shoulder_down(self):
        self.move_servo(2, self.step)

    def elbow_up(self):
        self.move_servo(3, -self.step)

    def elbow_down(self):
        self.move_servo(3, self.step)

    def wrist_up(self):
        self.move_servo(4, -self.step)

    def wrist_down(self):
        self.move_servo(4, self.step)

    def rotate_left(self):
        self.move_servo(5, -self.step)

    def rotate_right(self):
        self.move_servo(5, self.step)

    def grip_open(self):
        self.move_servo(6, -self.step)

    def grip_close(self):
        self.move_servo(6, self.step)
