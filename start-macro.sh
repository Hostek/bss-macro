#!/bin/bash

# 1. Start Xephyr (Sandbox)
echo "Starting Sandbox..."
Xephyr :2 -ac -screen 1024x768 &
XEPHYR_PID=$!
sleep 2

# 2. Start Sober inside Xephyr
echo "Starting Sober..."
DISPLAY=:2 flatpak run org.vinegarhq.Sober &

echo "-------------------------------------------"
echo "   Setup Complete."
echo "   1. Log in to Roblox inside the window."
echo "   2. Go to your game."
echo "   3. Position your camera/character."
echo "-------------------------------------------"
echo "Press ENTER when you are ready to start the macro..."
read

# 3. Run the Python Macro
# We pass the python script to handle the complex logic
python3 main.py

# Cleanup when python script finishes (Ctrl+C)
kill $XEPHYR_PID
