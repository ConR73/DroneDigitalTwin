##Drone
import math
from math import cos
from math import sin


class Drone:
    def __init__(self, name, battery, speed, location_x,location_y,altitude,take_off_time,is_flying):
        self.name = name
        self.battery = battery
        self.speed = speed
        self.location_x = location_x
        self.location_y = location_y
        self.altitude = altitude
        self.take_off_time = take_off_time
        self.is_flying = is_flying
    def fly(self):
        self.battery -= 5
        self.altitude += 50
        self.speed = 5
        self.location_x += self.speed * self.take_off_time
        self.is_flying = True
        print(self.name, "is flying at",self.altitude,"meters above sea level","Taking off from (",self.location_x,",",self.location_y,")")
    def increase_speed(self,increase):
        if self.is_flying:
            self.speed=self.speed+increase
            self.battery -= increase/5
            print("speeds increased by",increase,"m/s to",my_drone.speed,"m/s")
        else:
            print(my_drone.name,"Is not flying")
    def fly_time(self,time_min,direction_degrees):
        if self.is_flying :
            self.battery -= (self.speed/2)*time_min
            self.location_x += (self.speed*time_min*60)*cos(math.radians(direction_degrees))
            self.location_y += (self.speed*time_min*60)*sin(math.radians(direction_degrees))
            print(my_drone.name,"is located at (",my_drone.location_x,",",my_drone.location_y,") After flying for",time_min,"minutes at",direction_degrees,"degrees")
        else:
            print(my_drone.name,"Is not flying")
    def check_battery(self):
        print(my_drone.battery,"% battery remaining")
        if my_drone.battery <= 15 and (my_drone.battery>0):
            print(my_drone.name,"Has low battery, Charge soon")
        if my_drone.battery <= 0:
            print(my_drone.name,"Has lost power and is probably falling out of the sky right now")

my_drone = Drone("MQ-9",100,0,100,28,7.8,5,False)

##Control Panel:
##Use my_drone.fly() to launch the drone into the air with a takeoff speed of 5m/s and default altitude of 50 meters above the runway
##Use my_drone.increase_speed(x) to increase the speed of the drone at the cost of battery (x = the increase speed in m/s)
##Use my_drone.fly_time(time_min,direction_degrees) to tell the drone to fly in a straight line for x minutes at a set degree relative to the X-axis
    ## this returns the Location of the drone in (x,y)
##Use my_drone.check_battery() to check the battery of the drone - may produce some fun results depending on the battery left

##Example test of My_drone system:
my_drone.fly()
my_drone.increase_speed(8)
my_drone.fly_time(10,0)
my_drone.check_battery()
