from zmqRemoteApi import RemoteAPIClient
import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
from controller import*

client = RemoteAPIClient()
sim = client.getObject('sim')

# client.setStepping(True)
# Dar uma olhada na documentação

# Set and create the controller

Control = controller(2.3, 0.5, 0.7)

Rolling_Right = sim.getObject('/rightMotor')
Rolling_Left = sim.getObject('/leftMotor')
Object = sim.getObject('/PioneerP3DX')
Reference = sim.getObject('/Reference')
sim.startSimulation()
i = 0
while(i != 1 ):
    positionObject = sim.getObjectPosition(Reference, Object)
    print(positionObject)
    while(not( 0.001 > positionObject[0] > -0.001 ) or not(0.001 > positionObject[1] > -0.001 )):
        Orientation = sim.getObjectOrientation(Object,-1)
        VelocityR,VelocityL = Control.CalVelocity(positionObject[0],positionObject[1],Orientation[2])
        sim.setJointTargetVelocity(Rolling_Right, VelocityR)
        sim.setJointTargetVelocity(Rolling_Left, VelocityL)
        positionObject = sim.getObjectPosition(Reference, Object)
        print(positionObject, '-------', VelocityL, VelocityR)
        print(Orientation)


    i = i + 1
sim.stopSimulation()

