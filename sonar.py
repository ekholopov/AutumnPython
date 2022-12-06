import numpy as np
import common


class Sonar(common.Common):
    def get_coordinates(self, signalleft, signalright):
        spectrumL = np.fft.fft(signalleft)
        spectrumR = np.fft.fft(signalright)

        n = spectrumL.size
        spectrumL[int(n/2):] = 0
        spectrumR[int(n/2):] = 0
        signalleft = np.fft.ifft(spectrumL)
        signalright = np.fft.ifft(spectrumR)

        # z_Left = np.abs(np.fft.ifft(spectrumL))
        # sigma = np.sqrt((np.sum(np.sqrt(z_Left))/n))
        # detection_level = np.where(z_Left >= sigma)

        # print(detection_level)
        # скорость звука в воде 1500
        # distance = ((detection_level[0][0])/self.fd) * 1500
        # print(distance)

        phiL = np.angle(signalleft)
        phiR = np.angle(signalright)
        dphi = phiR - phiL

        dphi[np.where(dphi > np.pi)] -= 2 * np.pi
        dphi[np.where(dphi < -np.pi)] += 2 * np.pi
        # среднее значение phi
        dphi_mean = sum(dphi) / dphi.size
        print("Sredn phasa = ", dphi_mean)
        peleng = np.arcsin((self.c * dphi_mean) / (2 * np.pi * self.fs * self.d))
        # вывод угла в градусах
        print("Itogoviy ugol = ", peleng * (180 / np.pi))
