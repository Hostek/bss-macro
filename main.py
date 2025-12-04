import sys
import core
import importlib

# List your available macros here (must match filename without .py)
AVAILABLE_MACROS = {"1": "strawberry1", "2": "snail"}


def main():
    core.setup_display()

    print("\n==============================")
    print("   LINUX AFK FARMER v2.0")
    print("==============================")
    print("Choose a macro to run:")

    for key, name in AVAILABLE_MACROS.items():
        print(f" [{key}] {name}")

    choice = input("\nEnter number > ")

    if choice not in AVAILABLE_MACROS:
        print("Invalid selection.")
        return

    macro_name = AVAILABLE_MACROS[choice]

    try:
        # Dynamically import the chosen file from macros folder
        macro_module = importlib.import_module(f"macros.{macro_name}")

        print(f"\n>>> Launching {macro_name}...")
        print(">>> Press Ctrl+C to STOP safely.\n")

        # Run the run() function inside that file
        macro_module.run()

    except KeyboardInterrupt:
        # This handles the Ctrl+C for ALL macros
        core.emergency_cleanup()
    except Exception as e:
        print(f"Error: {e}")
        core.emergency_cleanup()


if __name__ == "__main__":
    main()
