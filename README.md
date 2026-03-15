# DOFBOT Control System (Raspberry Pi)

Manual and realtime toggle control scripts for Yahboom DOFBOT robotic arm.

---

## Hardware Required

- Raspberry Pi
- Yahboom DOFBOT robotic arm
- External 5V power supply (IMPORTANT)
- I2C cable connection

---

## 1. Clone Project

```bash
git clone https://github.com/KCW6688/dofbot_control.git
cd dofbot_control

2. Enable I2C
sudo raspi-config

Go to:

Interface Options -> I2C -> Yes

Then reboot:

sudo reboot
3. Check I2C
ls /dev/i2c*
sudo i2cdetect -y 1

You should see address 15.

4. Install Dependencies
sudo apt update
sudo apt install -y i2c-tools python3-smbus python3-smbus2 python3-setuptools
5. Install Arm_Lib

Go to Yahboom Arm_Lib folder:

cd ~/Downloads/Arm/Arm_Lib
sudo python3 setup.py install

Test:

python3 -c "from Arm_Lib import Arm_Device; print('Arm_Lib OK')"
6. Move Arm Home
python3 home.py
7. Test Servos
python3 test_servo.py
8. Basic Keyboard Control
python3 keyboard_control.py
9. Realtime Toggle Control
python3 realtime_toggle_control.py

Keys:

a / d -> base toggle

w / s -> shoulder toggle

i / k -> elbow toggle

j / l -> wrist toggle

u / o -> rotate toggle

n / m -> gripper toggle

h -> stop and go home

x -> emergency stop

q -> quit
