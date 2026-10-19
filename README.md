Drone Flight Simulation
Overview
A simple Python program that simulates a drone's flight, speed, location, altitude, and battery life.

Features
Takeoff: Launches the drone and increases its altitude.
Speed Control: Increases speed at the cost of battery.
Flight Movement: Moves the drone in a specified direction.
Battery Check: Displays remaining battery and low-battery warnings.
Requirements
Python 3.x
math module (built into Python)
How to Use

my_drone.fly()                  # Take off
my_drone.increase_speed(10)     # Increase speed by 10 m/s
my_drone.fly_time(10, 0)        # Fly for 10 minutes at 0 degrees
my_drone.check_battery()        # Check battery level
Notes
This is a basic simulation for learning Python. It does not control a real drone.
