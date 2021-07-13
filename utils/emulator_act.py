from subprocess import Popen
from time import sleep



def shut_down_emulator():
    p = Popen('adb -s emulator-5554 emu kill', shell=True)
    sleep(5)
    if p.wait() != 0:
        print("[ERROR] adb ended incorrectly")


def run_emulator():
    Popen(
        '/home/npermyakov/Android/Sdk/emulator/emulator -avd Pixel_3a_XL_API_30 -no-snapshot-load -gpu guest -memory 3072',
        shell=True)
    Popen(
        '/Users/n.permyakov/Library/Android/sdk/emulator/emulator -avd Pixel_3a_XL_API_30 -no-snapshot-load -gpu guest -memory 3072',
        shell=True)


def reboot_emulator():
    shut_down_emulator()
    run_emulator()
