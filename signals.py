import numpy as np
import common


class Water(common.Common):
    def get_signals(self, r, phi):
        time = np.arange(0, self.tc, 1/self.fd)
        signalleft = np.random.randn(time.size)/10
        signalright = np.random.randn(time.size)/10

        delay = r/1500
        dr = self.d/1500 * np.sin(phi/100.0*np.pi)
        for i in range(time.size):
            if time[i] > delay and time[i] < delay*self.ti:
                signalleft[i] += np.sin(i*np.pi*self.fs*time[i])
                signalright[i] += np.sin(i * np.pi * self.fs * (time[i] - dr))

        return((time, signalleft, signalright))


water = Water()
(time, signalleft, signalright) = water.get_signals(500, 30)