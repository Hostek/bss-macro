import os
import time
import subprocess
import sys

# --- CONFIGURATION ---
TARGET_DISPLAY = ":2"


def setup_display():
    os.environ["DISPLAY"] = TARGET_DISPLAY
    print(f"[Core] Target Display set to {TARGET_DISPLAY}")


# --- HELPER FUNCTIONS ---
def hold_key(key, duration):
    subprocess.run(["xdotool", "keydown", key])
    time.sleep(duration)
    subprocess.run(["xdotool", "keyup", key])
    time.sleep(0.1)


def press_key(key):
    subprocess.run(["xdotool", "key", key])
    time.sleep(0.1)


def hold_dual_keys(key1, key2, duration):
    subprocess.run(["xdotool", "keydown", key1])
    subprocess.run(["xdotool", "keydown", key2])
    time.sleep(duration)
    subprocess.run(["xdotool", "keyup", key2])
    subprocess.run(["xdotool", "keyup", key1])
    time.sleep(0.1)


def mouse_down():
    subprocess.run(["xdotool", "mousedown", "1"])


def mouse_up():
    subprocess.run(["xdotool", "mouseup", "1"])


def reset_character():
    print("   -> [Core] Resetting Character...")
    press_key("Escape")
    time.sleep(0.5)
    press_key("R")
    time.sleep(0.5)
    press_key("Return")
    time.sleep(5)


def emergency_cleanup():
    print("\n[Core] Emergency Stop! Releasing all keys...")
    os.system("xdotool keyup w a s d space 1")
    os.system("xdotool mouseup 1")
