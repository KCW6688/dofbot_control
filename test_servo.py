from Arm_Lib import Arm_Device
import time

Arm = Arm_Device()

print("Start slow servo test")
time.sleep(2)

for sid in [1, 2, 3, 4, 5, 6]:
    print(f"\n=== Testing servo {sid} ===")
    time.sleep(2)

    Arm.Arm_serial_servo_write(sid, 30, 1200)
    print(f"Servo {sid} -> 30")
    time.sleep(3)

    Arm.Arm_serial_servo_write(sid, 150, 1200)
    print(f"Servo {sid} -> 150")
    time.sleep(3)

    Arm.Arm_serial_servo_write(sid, 90, 1200)
    print(f"Servo {sid} -> 90")
    time.sleep(3)

print("\nTest finished")
