import numpy as np
import math

class controller():

    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.Vxr = 0
        self.VMAX = 0.1
        self.WMAX = 0.1



    # def set_PID(self,Kp_n,Ki_n,Kd_n):
    #     Kp = Kp_n
    #     Ki = Ki_n
    #     Kd = Kd_n

    def xy_ToAngular(Pos1,Pos2):
        Pos1 = 0
        #converter aqui para angular

    def CalVelocity(self, PositionX, PositionY, OrientatioA):
        #converter as posições para as velocidades
        Gain_Vx = 0.6
        Gain_W = 0.4
        raiz = PositionX * PositionX + PositionY * PositionY
        Vx = np.sqrt(raiz)
        # V1x = (PositionX)/math.sqrt(raiz)
        # V1y = (PositionY)/math.sqrt(raiz)
        # V1 = np.array([[V1x],[V1y]])
        # U1 = np.array([[(np.cos(OrientatioA))],[np.sin(OrientatioA)]])
        # modv1 = np.sqrt(V1x * V1x + V1y * V1y)
        # modu1 = np.sqrt(np.cos(OrientatioA) * np.cos(OrientatioA) + np.sin(OrientatioA) * np.sin(OrientatioA) )
        # cosTheta = (U1.T @ V1)
        # cosTheta = np.arccos(cosTheta)
        # cosTheta = cosTheta.ravel()[0]
        Vx = Gain_Vx * Vx
        if(np.abs(Vx) > self.VMAX):
            Vx = self.VMAX * np.sign(Vx)
        W = math.atan2(PositionY, PositionX)
        r = 0.195
        L = 0.51901
        W = Gain_W * W
        if(np.abs(W)> self.WMAX):
            W = self.WMAX * np.sign(W)
        thetaL = (Vx/r) - ((L * W)/(2*r))
        thetaR = (Vx/r) + ((L * W)/(2*r))
        return thetaL, thetaR


