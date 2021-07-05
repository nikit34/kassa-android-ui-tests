from subprocess import Popen
from time import sleep


def reboot_emulator():
    p = Popen('adb -s emulator-5554 emu kill', shell=True)
    sleep(5)
    if p.wait() != 0:
        print("[ERROR] adb ended incorrectly")
    Popen('/home/npermyakov/Android/Sdk/emulator/emulator -avd Pixel_3a_API_30 -memory 3072', shell=True)
    Popen('/Users/n.permyakov/Library/Android/sdk/emulator/emulator -avd Pixel_3a_API_30 -memory 3072', shell=True)
    sleep(120)