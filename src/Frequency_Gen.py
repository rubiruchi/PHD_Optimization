'''
Author : Aneirin John Baker
Date : 10/12/2018
Description: Script to generte the frequencies table
'''
from Constants import *
from math import *
import numpy as np
#import matplotlib.pyplt as plt

#Calculations of the Freuencies of the Qbits within a specific range

omega   = 0
phi_bar =0
file = open("../Data/Frequency.dat","w")

for i in range(0,100):
	for j in range(1,150):
		omega = (1 / (hbar * 2 * PI)) * sqrt(8 * E_CQ(j) * (E_J(i) + (8 * E_L(100e-9)))) * (1e-9)
		phi_bar = ((2*E_CQ(j))/(E_J(i) + (8 * E_L(100e-9))))**0.25
		
		if(omega > 2 and omega < 30):
			file.write(str(i) + " " + str(j) + " " + str(omega) + " " + str(phi_bar) + "\n")
file.close()