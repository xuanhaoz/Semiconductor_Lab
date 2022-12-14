'''!
  @file demo_read_voltage.py
  @brief connect ADS1115 I2C interface with your board (please reference board compatibility)
  @n  The voltage value read by A0 A1 A2 A3 is printed through the serial port.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [luoyufeng](yufeng.luo@dfrobot.com)
  @version  V1.0
  @date  2019-06-19
  @url https://github.com/DFRobot/DFRobot_ADS1115
'''

import sys
import os
import time
import numpy as np

sys.path.append('../')
# import sys.path.dirname(os.path.dirname(os.path.realpath(__file__)))
from DFRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()
Temp=[]
Iset=[]
Volt=[]

for i in range(700):
                                                                                                                                                                              #Set the IIC address
    ads1115.set_addr_ADS1115(0x48)
    #Sets the gain and input voltage range.
    # ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
    ads1115.set_gain(ADS1115_REG_CONFIG_PGA_4_096V)
    #Get the Digital Value of Analog of selected channel
    adc0 = ads1115.read_voltage(0)
    adc1 = ads1115.read_voltage(1)
    
    #measuring voltage across Rset to find temperature 
    V0=adc0['r']
    I0=adc0['r']*(1E-3)/(9.72E3)
    T0=(I0*1E4)/(227E-6)
    V1=adc1['r']-adc0['r']
    Temp.append(T0)
    Iset.append(I0)
    Volt.append(V1)
    print("V1",V1,"Td",T0,"I",I0)
    time.sleep(5)
    
data=np.array([[Temp],[Volt],[Iset]]).T
    
sys.stdout=open("TVlast-Rd.txt","w")
print(data)
sys.stdout.close()

with open("TVlast.txt","w") as outfile:
   for t,v,i in zip(Temp, Iset, Volt):
        #lineout = str(t)+";"+str(v)+";"+str(i)+"\n"
        lineout = "{}, {}, {}\n".format(t,v,i)
        #outfile.write((";").join([str(t),str(v),str(i)])+"\n")
        outfile.write(lineout)
 
    
    
    #I1=(adc1['r']-adc0['r'])*(10**-3)/10**4
    #print ("A0:%dmV A1:%dmV A2:%dmV A3:%dmV"%{adc0['r'],adc1['r'],adc2['r'],adc3['r']})
    #print("A0",adc0['r'],"I0",I0, '\n',"A1",adc1['r']-adc0['r'],"I1",I1)
    