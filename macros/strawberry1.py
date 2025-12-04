import time
import core  # We import our tools


def run():
    print("--- Loaded Macro: Strawberry 1 ---")

    while True:
        print("\n--- STARTING NEW GLOBAL CYCLE ---")

        # 1. ESC + R + ENTER + wait 5s (Repeat 3 times)
        for i in range(3):
            core.reset_character()

        print("   -> Main Navigation Path...")
        core.hold_key("w", 3)
        core.hold_key("d", 10)
        core.hold_key("a", 2.5)
        core.hold_key("s", 20)

        print("   -> Jump + Backwards...")
        core.hold_dual_keys("space", "s", 2)

        core.hold_key("d", 7)
        core.hold_key("s", 4)
        core.hold_key("a", 1.2)
        core.hold_key("w", 1.2)

        print("   -> Using Item 1...")
        core.press_key("1")

        core.hold_key("s", 2)
        core.hold_key("d", 2)

        print("   -> Entering 10 minute farming loop...")
        start_time = time.time()
        ten_minutes = 600

        while (time.time() - start_time) < ten_minutes:
            core.hold_key("w", 1.5)
            core.hold_key("a", 1.5)
            core.hold_key("d", 3)
            core.hold_key("s", 3)

        print("   -> 10 Minutes up! Restarting Global Cycle.")
