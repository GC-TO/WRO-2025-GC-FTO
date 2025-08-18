# WRO README

                                            Introduction

Our robot is designed for the Future Engineers self-driving robot category. In this category the robot has to do two challenges: Open Challenge and Obstacle Avoidance. The Open Challenge involves three laps of a circuit, in which the size, starting position, and direction of travel are determined randomly. The Obstacle Avoidance challenge has a fixed circuit that the robot has to navigate while avoiding obstacles that are placed randomly.
------------------------------------------------------------------------------------------------------------------
                                                  Team

The name of our team is Future TO and we are from El Salvador. The team members are Antonio Borst, Daniel Salazar and Manuel Vasquez. We are coached by Sergio Cuellar.

------------------------------------------------------------------------------------------------------------------
                                               Hardware Specifications            

The robot is built using mostly Lego Technic but components from other companies are also utilized. Lego Technic has the advantage that it comes with a differential piece that allows the wheels to spin at different rates when the car turns. This is important because, if the wheels were directly connected to each other, one of them would have to spin more or less than the other, leading to less stable turns. The differential solves that by using a system of gears that allow the wheels to spin at different rates, while still sending power to each wheel, something that is especially useful when dealing with tight turns.

The rules state that the robot can only use two motors, one to move forwards and one to steer. For the design of our robot's steering system we were inspired by a Haltenberger Linkage. We felt that an advantage of using that linkage would reside in the steering gearbox, since it uses a gear reduction which makes the steering more precise and more stable. For example, if the motor needs to turn ten degrees for the tires to turn one degree, then even if the motor misses by one or two degrees the effect is negligible. 

Our robot has the following list of components: 

one Lego Mindstorms Inventor Hub. This includes an internal gyroscope which we use to make sure each turn is precise, rather than just doing it via distance or time. 
a Lego Mindstorms Inventor Hub battery
two Lego Mindstorms motors
one Lego Mindstorms color sensor. We use this to detect the blue and orange lines on the track. The order in which we detect them tells us which way the robot is going
two Lego Mindstorms ultrasonic sensors. These let the robot know if it is approaching a wall.
one Huskylens AI camera. This allows us to detect the color and shape of objects from a much greater distance than that of the color sensor. 
one LMS-ESp32 board to allow the use of the VL53LOx Time-of-Flight sensors and the use of the Huskylens AI camera.
three VL53LOx Time-of-Flight laser ranging sensors. One faces forwards, and two at 45 degrees from the front of the robot. This allows us to read the distance from the wall even if the robot is turning.

------------------------------------------------------------------------------------------------------------------
                                           Software Specifications  

Our robot uses Pybricks(programed with python), which is installed on the Lego Mindstorms Inventor Hub.       

There is also a separate program for the LMS-ESp32. This code allows the board to extract the data from the sensors and devices connected to it. We then send the data to be used in the main code, which is running on the Lego Mindstorms Inventor Hub. The coding language is also python, and it is coded with Thonny.                                                   
                                                                                                                 
------------------------------------------------------------------------------------------------------------------
                                        Installation and Usage Instructions  

The repository consists of two parts. One is the code used for the Lego Mindstorms Inventor Hub, and the other is the code that runs on the LMS-ESp32. Both programs are coded using Python, the Lego Mindstorms Inventor Hub using Pybricks, and the LMS-ESp32 using Thonny. 

To use the code with the robot, it is necessary to make sure that the LMS-ESp32 has its code and is running it. This only needs to be done once, since afterwards it is already downloaded and runs automatically when the robot is on. It is necessary for the Lego Mindstorms Inventor Hub to be running the Pybricks code. That is done by connecting the Lego Mindstorms Inventor Hub to a device via Bluetooth and running the code. The code downloads onto the robot once it is run, so that step only needs to be repeated once if the code has not been changed.

------------------------------------------------------------------------------------------------------------------
