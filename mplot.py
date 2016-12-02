#import serial
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import * 

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#ser = serial.Serial('COM9', 115200)
ser = open("pdd3.dat","rw+")
line = ser.readlines()
for i in line:
	arr=i.split(':')
	print arr[0]

yaw = 0.0
pitch =0.0
roll =0.0
ax =0.0
ay =0.0
az =0.0
o_yaw= [0]
o_pitch= [0]
o_roll= [0]
o_ax= [0]
o_ay= [0]
o_az= [0]
plt.ion()
cnt=0
def makeFig(): 
    plt.ylim(-3000,3000)                                 
    plt.grid(True)
    plt.ylabel('Magnitude')  
    plt.plot(o_ax, 'ro-', label='ax') 
    plt.plot(o_ay, 'bo-', label='ay')  
    plt.plot(o_az, 'go-', label='az')                               
    plt.legend()
                      

while True:
    for i in line:
    	arr=i.split(':')
    	o_ax.append(arr[3])                    
    	o_ay.append(arr[4])    
    	o_az.append(arr[5])
    	o_yaw.append(arr[0])
    	o_pitch.append(arr[1])
    	o_roll.append(arr[2])              

    	drawnow(makeFig)                       
    	plt.pause(.00001)                     
    	cnt=cnt+1
    	if(cnt>50):                            
        	o_ax.pop(0)
        	o_ay.pop(0)                     
        	o_az.pop(0)

