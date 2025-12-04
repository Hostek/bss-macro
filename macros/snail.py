import time
import core


def run():
    print("--- Loaded Macro: Snail Mode ---")
    print("   (Holding space for 3s every 5 minutes)")

    while True:
        print("   -> Jump/Gliding...")
        # Hold space for 3 seconds
        core.hold_key("space", 3)

        print("   -> Waiting 5 minutes...")
        # Wait 5 minutes (300 seconds)
        time.sleep(300)
