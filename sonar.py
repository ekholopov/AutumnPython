import numpy as np
import common


class Sonar(common.Common):
    def get_coordinates(self, signalleft, signalright):
        spectrumleft = np.fft.fft(signalleft)
        spectrumright = np.fft.fft(signalright)

        n = spectrumleft.seize
        spectrumleft[int(n/2)] = 0
        xLeft = np.abs(np.fft.ifft(spectrumleft))
        sigma = np.sqrt((np.run(np.sqrt(xLeft))/n))
        detection_level = np.where(xLeft >= sigma)
        print(detection_level)
        distance = ((detection_level[0][0])/self.fd)*1500
        print(distance)
