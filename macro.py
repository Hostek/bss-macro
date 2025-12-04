import os
import time
import subprocess
import random

# --- CONFIGURATION ---
# This must match the Xephyr display ID in your shell script
TARGET_DISPLAY = ":2"

# Set the environment variable so xdotool affects Xephyr, not your main screen
os.environ["DISPLAY"] = TARGET_DISPLAY


# --- HELPER FUNCTIONS ---
def hold_key(key, duration):
    # Holds a key down, waits, then lifts it
    subprocess.run(["xdotool", "keydown", key])
    time.sleep(duration)
    subprocess.run(["xdotool", "keyup", key])
    time.sleep(0.2)  # Tiny pause between actions


def press_key(key):
    # Taps a key instantly
    subprocess.run(["xdotool", "key", key])
    time.sleep(0.2)


def hold_dual_keys(key1, key2, duration):
    # Holds two keys simultaneously
    subprocess.run(["xdotool", "keydown", key1])
    subprocess.run(["xdotool", "keydown", key2])
    time.sleep(duration)
    subprocess.run(["xdotool", "keyup", key2])
    subprocess.run(["xdotool", "keyup", key1])
    time.sleep(0.2)


def reset_character():
    print("   -> Resetting Character (Esc R Enter)...")
    # Roblox Reset Sequence
    press_key("Escape")
    time.sleep(0.5)
    press_key("R")
    time.sleep(0.5)
    press_key("Return")
    time.sleep(5)  # Wait for respawn


# --- MAIN MACRO LOOP ---
print(f"Starting Macro on Display {TARGET_DISPLAY}")
print("Press Ctrl+C in the terminal to stop.")

try:
    while True:
        print("\n--- STARTING NEW GLOBAL CYCLE ---")

        # 1. ESC + R + ENTER + wait 5s (Repeat 3 times)
        for i in range(3):
            reset_character()

        print("   -> Main Navigation Path...")
        # 2. Navigation Sequence
        hold_key("w", 3)
        hold_key("d", 10)
        hold_key("a", 2.5)
        hold_key("s", 20)

        # 3. Hold Space and S simultaneously for 2 seconds
        print("   -> Jump + Backwards...")
        hold_dual_keys("space", "s", 2)

        # 4. Continued navigation
        hold_key("d", 7)
        hold_key("s", 4)
        hold_key("a", 1.2)
        hold_key("w", 1.2)

        # 5. Use Item
        print("   -> Using Item 1...")
        press_key("1")

        hold_key("s", 2)
        hold_key("d", 2)

        # 6. The 10 Minute Sub-Loop
        print("   -> Entering 10 minute farming loop...")
        start_time = time.time()
        ten_minutes = 600  # 600 seconds

        while (time.time() - start_time) < ten_minutes:
            # This runs repeatedly for 10 mins
            hold_key("w", 1.5)
            hold_key("a", 1.5)
            hold_key("d", 3)
            hold_key("s", 3)

        print("   -> 10 Minutes up! Restarting Global Cycle.")

except KeyboardInterrupt:
    print("\nMacro stopped by user.")
    # Safety: Ensure all keys are released so they don't get stuck 'down'
    os.system("xdotool keyup w a s d space")
