#!/usr/bin/env python

# from adatools import config_generator as cg
from adatools import plotting_tools as pt
from spatialmath import SE3
import numpy as np  
import time
import roboticstoolbox as rtb
from math import pi
import spatialgeometry as sg

# This example shows how to check if your robot can reach all the corners of the base plate.
# If you see that the translational o andular distance is too large, the manipulability is close to zero or the Jacobian of the robot loses rank (rank < 5), you should consider changing the robot's link lengths and offsets.

# Create a robot based on config1
# Base til å sjekke
plate = sg.Cuboid(scale=[0.75, 0.55, 2],
                  pose=SE3(0.225, 0, -0.01),
                  color=(0.27, 0.51, 0.71, 1.0))

robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.2, a=0.0, alpha=pi/2, qlim=[-110 *pi/180, 110 *pi/180]), 
        rtb.RevoluteDH(a=0.20, d=0.0, qlim=[-80 *pi/180, 260 *pi/180]),
        rtb.RevoluteDH(a=0.28, d=0.0, qlim=[-170 *pi/180, 170 *pi/180]),
        rtb.RevoluteDH(alpha=pi/2,qlim=[-170 *pi/180, 170 *pi/180]),
        rtb.RevoluteDH(d=0.05, a=0.0, qlim=[-2*pi, 2*pi]),
       
    ], name="My Config 1 Robot")
robot.tool = SE3(0, 0.05, 0.05)
robot.qr = [0, 0, 0, 0, 0]

print(robot)
# print(robot.links)

robot.teach(robot.qr)


robot_plot = robot.plot(robot.qr, backend='pyplot') # plot the robot in its home position
robot_plot.add(plate)
input("Press Enter in terminal to continue...")
q = np.array(robot.qr, dtype=float)
# for angle in np.linspace(0, 2*pi, 100):
    
#     q[3] = angle
#     robot.q = q
#     robot_plot.step()
#    # time.sleep(0.003)
# input("Press Enter in terminal to continue...")

# for angle in np.linspace(0, 2*pi, 100):
#     q[4] = angle
#     robot.q = q
#     print(q)
#     robot_plot.step()
#     #time.sleep(0.003)
# input("Press Enter in terminal to continue...")

Tgoal = SE3(0.3, 0.1, 0.2)
Tgoal.plot(ax=robot_plot.ax, length=0.1, style='rgb')
print(robot.iscollided(robot.q, plate))
sol =robot.ikine_LM(
    Tgoal, 
    q0=robot.q, 
    mask=[1, 1, 1, 0, 0, 0.2]#Can add tol to get more acurate position, but need to see if motor are can do bether
    )
print(sol.q)
robot.q = sol.q
robot_plot.step()
input("Press Enter in terminal to continue...")
# pt.plot_baseplate(robot_plot)  # plot the base plate

# # Define the goal poses
# Tgoals = SE3([SE3(0.3, 0, 0.2),
#               SE3(0.3, 0, 0),
#               SE3(0, 0.55/2, 0.2),
#               SE3(0, 0.55/2, 0),
#               SE3(0, -0.55/2, 0.2),
#               SE3(0, -0.55/2, 0),
#               SE3(0.6, 0.55/2, 0.2),
#               SE3(0.6, 0.55/2, 0),
#               SE3(0.6, -0.55/2, 0.2),
#               SE3(0.6, -0.55/2, 0)]) * SE3.Rx(180, 'deg')

# Tgoals.plot(ax=robot_plot.ax, length=0.1, style='rgb') # plot all goal poses
# print(robot.qlim)
# # robot.plot(robot.qlim)
# # Check if robot can reach the goal poses
# sol = []
# i = 0
# for Tg in Tgoals:
#     sol.append(robot.ikine_LM(Tg, q0=robot.qr, mask=[1,1,1,0,0,0])) # inverse kinematics
#     robot.q = sol[i].q
#     robot_plot.step()

#     T = robot.fkine(robot.q) # forward kinematics
#     angular_distance = Tg.angdist(T)
#     trans_distance = np.linalg.norm(Tg.t - T.t)
#     manip = robot.manipulability(robot.q, method='minsingular', axes='all')
#     J_rank = np.linalg.matrix_rank(robot.jacob0(robot.q))
#     print("Pose %03d : Translational distance (norm): %0.4f, Angular distance (geodesic norm): %0.4f, Manipulability: %.4g, Jacobian Rank: %d" \
#            %(i, trans_distance, angular_distance, manip, J_rank))
#     i = i + 1
#     input("Press Enter in terminal to continue...")
#     #time.sleep(2)

