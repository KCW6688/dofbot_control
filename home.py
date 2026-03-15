from Arm_Lib import Arm_Device
import time

Arm = Arm_Device()

Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 1500)
time.sleep(2)

print("Robot Ready")
